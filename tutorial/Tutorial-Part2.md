# Extended Serializers

It's time we took a closer look at serializers. Until now they have been mostly transparent, serving out the content from the models almost transparently.

However, let's imagine that I would like to display the title of the book for each piece in my views. Currently, the only data the serializer is giving me is a URL to retrieve the data about the book -- not the actual data itself.

Here is a JSON record of a Piece to illustrate:

```
{
    "url":"http://localhost:8000/piece/1/",
    "book_id":"http://localhost:8000/book/1/",
    "title":"Blah blah",
    "composer_src":"",
    "forces":"SATB",
    "print_concordances":"",
    "ms_concordances":"",
    "pdf_link":""
}
```

To get the book title, we can embed a book serializer within our piece serializer. Open up `serializers/piece.py` and import your `BookSerializer` from `serializers/book.py`. Then change your `PieceSerializer` to this:

```
class PieceSerializer(serializers.HyperlinkedModelSerializer):
    book_id = BookSerializer()

    class Meta:
        model = Piece
```

Now the request for the same piece results in this:

```
{
    "book_id":{
        "url":"http://localhost:8000/book/1/",
        "title":"Book 1",
        "publisher":"Someone",
        "published":"1501-01-10",
        "rism_id":"1",
        "cesr_id":"2",
        "remarks":"3",
        "num_pages":100,
        "created":"2013-11-08T00:29:36.956Z",
        "updated":"2013-11-08T00:29:36.956Z"
    },
    "url":"http://localhost:8000/piece/1/",
    "title":"Blah blah",
    "composer_src":"",
    "forces":"SATB",
    "print_concordances":"",
    "ms_concordances":"",
    "pdf_link":""
}
```

We can now access the title from our piece through the `book_id` field. Open your `templates/piece/piece_list.html` and add a column for the book that a given piece is in.

## Computed Fields

In our models we can define methods that can be used to process and extract information stored in that model. We have already seen a very simple example of this with the `__unicode__` method, returning the `title` field as a representation of that model.

A computed field is a model method that acts like a field. To illustrate, let's make a computed field that takes a the 'composer_src' field in Piece and, if it contains a comma, splits it and reverses it to show the composer's name as Firstname Lastname, rather than Lastname, Firstname. Open your `Piece` model and add the following method:

```
@property
def composer_name(self):
    name = self.composer_src.split(",")
    if len(name) > 1:
        return u"{0} {1}".format(name[1], name[0])
    else:
        return u"{0}".format(self.composer_src)
```

Again, this is a really simple method, and probably needs to be made bit more robust to different types of information in the `composer_src` field.

We can now use this in our serializer to show the composers's full name, as well as their "sorting" name.

Add the following field to your `serializers/piece.py`.

```
    composer_name = serializers.Field(source="composer_name")
```

Now we have a new field in our output, `composer_name` which we can use to display a more natural, human-friendly version of the person's name.

# Solr

Let's shift gears for a bit and talk about Solr. Solr is a search engine designed for fast retrieval of records. It also provides handy tools for creating faceted searching. We will be setting up Solr to use as a search engine in our Digital Goudimel project.

## Getting Started

If you haven't already, you should download the code from my "ToursDemoApplication" folder. In there you will find a `solr` folder. In there you will find one file, `pom.xml` and one folder, `src`. We will build a full instance of Solr using these two files and the `maven` package.

### Install prerequisites

Before we begin, you should make sure you have Tomcat and Maven installed. I find the easiest way to do this is with the `homebrew` package system on OSX, or `apt-get` on Ubuntu.

`$> brew install tomcat`
`$> brew install maven`

### Customize the package

The `pom.xml` file contains the build instructions for building a Solr instance with Maven. Before doing this, however, you should make sure you customize it to your specific project. Open it up and change some values for the following tags at the top:

 * groupId
 * artifactId
 * name
 * url

Next, look down to the `build` section and change the `finalName` tag to match what you put in the `artifactId`.

Next, let's look in the `src` directory. There are quite a few files in `src/main/resources`, but we will only look at two: `solrconfig.xml` and `schema.xml`. Open up `solrconfig.xml`.

I have had quite a few problems in the past with the value in the `dataDir` tag. Solr tries to be smart about where it stores its data, which may not work due to permissions problems. To prevent problems I find it easiest to specify a folder on my system that Solr can read and write to.

Typically, I set the value to `/var/db/solr/` and then a sub-folder for the specific instance of solr I'm creating. So we should set the value of this to `/var/db/solr/goudimel-solr`. You can put it whereever you like, but it should be a location that is readable and writeable by the same user that owns and runs the `tomcat` server (this varies from system to system, depending on how you have installed tomcat).

Change it and close `solrconfig.xml`.

We will focus most of our customization work on the `schema.xml` but initially we just need to change one line. Look for the `<schema name=...>` tag and change the name to something descriptive (I use the same value as the `artifactId`).

Now we will try to build our Solr instance. Change to the `solr` directory in your project folder (the one with `pom.xml` in it) and run the following command:

`$> mvn package`

If this is the first time it is run, it will probably take a few minutes to download and install all the dependencies. If not, it will only take a few seconds.

After this is finished you will have a new directory, 'target'. In this directory will be a number of files, but the one we are interested in is the .war file. It will be named after the value you supplied for `finalName` in `pom.xml`

This `.war` file (for "Web Archive") is the built Solr web application, suitable for deployment with Tomcat. Any time we make a change in the `src` directory we will need to re-build this `.war` file by re-running `mvn package`.

On my system the Tomcat `webapps` directory is at `/usr/local/opt/tomcat/libexec/webapps`. We will either need to copy our `.war` file to this, or, even better, create a symbolic link between it so that when we re-build our Solr package it will automatically be re-deployed. To symlink it, change to your tomcat webapps directory and run:

`$> ln -s /path/to/your/project/solr/target/goudimel-solr.war .`

Now let's start up Tomcat and see if it worked. On my system I start Tomcat with the following command:

`$> catalina start`

(Similarly you can stop Tomcat with `catalina stop`)

Open a web browser and enter the URL: `http://localhost:8080/goudimel-solr/admin/`

If all went well, you should see something like this:

![Figure 9](figures/figure9.png)

We're now ready to go!

## Understanding the Solr schema file

Open up `schema.xml` and find the `<fields>` section (This should be towards the end of the file). This section defines the fields that are present in Solr, and determine the data that we want to index.

There are several field types. All field types present in your schema must be defined above. It is possible to define new, custom fields that (for example) deal with non-English searching rules.

In general there are three different field definitions possible. The first is a regular `field`. A field defined like this might look like:

`<field name="type" type="string" indexed="true" stored="true" />`

In this example, we have a field named "type", with a content type of "string". This field will be both indexed (for searching) and stored (so we can retrieve it later). These last two parameters can be handy for optimizing a search engine. For example, we can index a field, but not store it. This means that we can use it in queries, but we don't necessarily want to be able to retrieve it. The opposite, storing but not indexing, means we can store data in a Solr record but not make it available for searching.

The second field definition is a `dynamicField`. Its definition looks like this:

`<dynamicField name="voice_*" type="string" indexed="true" stored="true"/>`

This looks like the regular field definition, but notice that instead of a regular field name it has a wildcard ('*') as part of the name. This means that this field will accept any fields with a name that matches the prefix.

In the DuChemin project this is used to index a number of "Voice Role" fields. For example, we have indexes for the following fields:

voice_role_above, voice_role_below, voice_role_com1, voice_role_com2, voice_role_dux1, voice_role_dux2, voice_role_fifth, voice_role_fourth... 

and several others. Rather than defining a field for each of these, the `dynamicField` allows us to create new fields "on the fly" as we index our data.

Finally, the last field definition is the `copyField`. This is not a field, but rather a way of re-purposing existing fields to process them in a different manner. Consider the following definitions:

`<field name="book_title" type="string" indexed="true" stored="true" />`
`<field name="tg_book_title" type="text_general" indexed="true" />`
`<field name="tg_fr_book_title" type="text_fr" indexed="true" />`

In the first definition we define a field for the book title that stores a book title as a "string" type. This is useful for when we want to display the book title, but not very useful if we want to do full-text search of the fields and do all the things we expect full-text searching to do -- namely, understand that words can have different endings (for plurals). This is called "stemming".

In the second definition we define a "text_general" field that provides these sorts of full-text searching tools. Note that while we index it, we are not storing it for retrieval later.

However, our 'text_general' field is defined using English grammar rules! This means that it assumes the text in the field is English, and applies the stemming rules accordingly. However, we know that the book titles we are indexing are in French, so we need another field to index this properly.

The last definition uses a "text_fr" field definition that applies proper French grammar and language rules. You can look above in your `schema.xml` file to find the exact definition of this field:

```
    <!-- French -->
    <fieldType name="text_fr" class="solr.TextField" positionIncrementGap="100">
      <analyzer> 
        <tokenizer class="solr.StandardTokenizerFactory"/>
        <!-- removes l', etc -->
        <filter class="solr.ElisionFilterFactory" ignoreCase="true" articles="lang/contractions_fr.txt"/>
        <filter class="solr.LowerCaseFilterFactory"/>
        <filter class="solr.StopFilterFactory" ignoreCase="true" words="lang/stopwords_fr.txt" format="snowball" enablePositionIncrements="true"/>
        <filter class="solr.FrenchLightStemFilterFactory"/>
        <!-- less aggressive: <filter class="solr.FrenchMinimalStemFilterFactory"/> -->
        <!-- more aggressive: <filter class="solr.SnowballPorterFilterFactory" language="French"/> -->
      </analyzer>
    </fieldType>
```

When we import our documents into Solr, we would need to load the Book title into these three fields separately. This is where `copyField` comes in handy. We can define two `copyField` directives in our `fields` section:

`<copyField source="title" dest="tg_piece_title"/>`
`<copyField source="title" dest="tg_fr_piece_title"/>`

The `copyField` takes a single field and copies the contents to another field so that other rules may be applied to it.

Field types will store, and work, with specific types of data. For example, the "string" type will store a literal string, which makes it a useful field for faceted searches (where all records are grouped according to a string). Number fields, like "int" or "float" allows for sorting and arithmetic, while "date" fields allow for date-range searching ("Fetch records between date A and date B"). As mentioned earlier, "text" fields provide extra functionality for performing full-text searches.

## Writing a Solr Schema

So, now we have a Django database with our data stored, and a Solr instance waiting to index our data. So let's build a schema with fields to store our data.

Each document in Solr must have an unique identifier. Since we will (potentially) be loading many records in, the easiest way I have found to ensure that each record has a unique identifier is to use a Universially Unique ID (UUID). Fortunately it's very easy to generate UUIDs in Python. So, our first field will be 'id':

`<field name="id" type="string" indexed="true" stored="true" required="true" />`

While we have three Models in Django, we can't differentiate between records that easily in Solr. So we will define a field called "type" that contains one of three values that will identify our content types: "goudimel_book", "goudimel_piece" or "goudimel_phrase". Our next field will be "type".

`<field name="type" type="string" indexed="true" stored="true" />`

These two fields will be part of every record, no matter what other fields we choose to store in each document.

At this point you should add fields for every piece of data you wish to store from your Django models. As an example, here is what I have for the `Book` model fields:

```
<field name="publisher" type="string" indexed="true" stored="true"/>
<field name="published" type="date" indexed="true" stored="true" />
<field name="rism_id" type="string" indexed="true" stored="true" />
<field name="cesr_id" type="string" indexed="true" stored="true" />
<field name="remarks" type="text_general" indexed="true" stored="true" />
<field name="num_pages" type="int" indexed="true" stored="true" />
```

Do this for each of your models.

Using dynamic fields and copy fields we can create extra indexes for the data in your model fields.

```
<dynamicField name="text_fr_*" type="text_fr" indexed="true" stored="true" />
<dynamicField name="text_gen_*" type="text_general" indexed="true" stored="true" />

<copyField source="phrase_text" dest="text_fr_phrase_text" />
<copyField source="title" dest="text_fr_title" />
<copyField source="title" dest="text_gen_title" />

<copyField source="title" dest="text" />
<copyField source="publisher" dest="text" />
```

These definitions will automatically copy the contents of one field and re-index it according to the rules defined for the destination field type. This allows you to, for example, search the title field with both English and French stemming rules.

Re-build your Solr instance and check to make sure it is working in Tomcat.

## Automatically Indexing Content

The next thing we need to do is to start adding content to the Solr instance from our Django application. We can do this in two ways. The first is to have a separate "indexing" script that periodically runs and copies our data from Django into Solr. This is simple, but it requires manual intervention whenever data changes in our Django application.

A better solution is to automatically index content whenever a record is saved. To do this we will make use of Django's "Signals" feature.

### Signals

Django signals are an implementation of the 'notification' design pattern. This design pattern allows us to execute multiple actions when a single message, or signal, is triggered.

When a Django model instance is saved, either when it is created or when it is edited, it will send a notification out. This notification is picked up by any methods that are registered to receive this notification.

This is useful when we want to trigger many actions (like indexing in Solr) when a record is saved, but we don't want to override the `save()` method on that model.

### SolrPy

SolrPy is the Python module we will be using to get Django to talk to Solr. There are other, more complex modules but I find they obscure a lot of the work that Solr does in a way that makes it difficult to understand how to build a custom search system.

The first thing we need to do is create a setting in our Django application where we can store the address of our Solr server. Open up `settings.py` and add the following line:

`SOLR_SERVER = "http://localhost:8080/goudimel-solr/"`

That's really all we need to do for now. We will use this setting when we need to work with Solr in our indexing and querying methods.

### Indexing Content

Open up your `Book` model file (`models/book.py`). To start using Signals we will need to import some new methods at the top.

Import the following:

```
from django.dispatch import receiver
from django.db.models.signals import post_save
```

Now create a new function in this file. It should be its own function, and not part of the `Book` class.

```
@receiver(post_save, sender=Book)
def solr_index(sender, instance, created, **kwargs):
    import uuid
    from django.conf import settings
    import solr

    solrconn = solr.SolrConnection(settings.SOLR_SERVER)
    record = solrconn.query("type:goudimel_book item_id:{0}".format(instance.id))
    if record:
        # the record already exists, so we'll remove it first.
        solrconn.delete(record.results[0]['id'])

    book = instance
    d = {
        'type': 'goudimel_book',
        'id': str(uuid.uuid4()),
        'item_id': book.id,
        'title': book.title,
        'publisher': book.publisher,
        'published': book.published,
        'rism_id': book.rism_id,
        'cesr_id': book.cesr_id,
        'remarks': book.remarks,
        'num_pages': book.num_pages,
        'created': book.created,
        'updated': book.updated
    }
    solrconn.add(**d)
    solrconn.commit()
```

Let's look at this method a bit more in-depth. The first line of this function is called a Python "decorator". Decorators are handy to know about, but for now it's enough to know that this function is what "registers" the following function for notifications. Notice that the `@receiver` takes two arguments: the notification it will listen for (`post_save`), and the specific model that it listens for notifications from (`Book`).

This means that after a Book record has been saved, this `solr_index` function will be called.

The `solr_index` function takes a number of parameters. The first is a reference to the sender, in this case the Book model. The second is a reference to the specific `instance,` or record that was saved. The other arguments are optional and can be ignored for the moment.

The import lines are fairly self-explanatory. Notice that we are importing the `uuid` module to create universally unique IDs for our records.

`solrconn` is the call that establishes a connection to our Solr server. We can use the setting from our `settings.py` that we created earlier.

The next few lines will look for an existing record in our Solr system. If we are creating a new record, chances are it will not exist. However, if we are updating an older record the easiest way to deal with it is to delete the old record and then re-add a new one.

Finally, we index the content. We create a key/value dictionary that contains the Solr field that we want to push content into, and the content from our book instance that is being saved as the value. Notice that the keys in our dictionary match the fields that we established in our Solr schema.

This is concluded by calling `add` to our Solr server to add the document to the Solr server. It uses a Python idiom that you may not be familiar with:

`solrconn.add(**d)`

What this call does is expands the keys and values from our dictionary into arguments for the function call. So:

`d = {'title': "My great book title", "published": "1501-01-01"}`

becomes:

`solrconn.add(title="My great book title", published="1501-01-01")`

I find it a very handy thing to use.

Now that our indexing script is in place, let's test it out. Open a web browser and navigate to the Django admin interface. Add a new book.

Once you have added it, navigate to your Solr admin interface. You will see a field, "Make a Query" that is filled out with the Solr wildcard search (`*:*`). Click the search button.

You should see something like this:

```
<?xml version="1.0" encoding="UTF-8"?>
<response>
    <lst name="responseHeader">
      <int name="status">0</int>
      <int name="QTime">1</int>
      <lst name="params">
        <str name="q">type:goudimel_book</str>
        <str name="version">2.2</str>
        <str name="start">0</str>
        <str name="rows">10</str>
        <str name="indent">on</str>
      </lst>
    </lst>
    <result name="response" numFound="4" start="0">
      <doc>
        <str name="cesr_id">65543</str>
        <date name="created">2013-11-15T19:00:00Z</date>
        <str name="id">dea6ce59-c33a-4b55-a95d-fc734eb130a9</str>
        <str name="item_id">3</str>
        <date name="published">1999-03-01T00:00:00Z</date>
        <str name="publisher">Andrew Hankinson</str>
        <str name="rism_id">24532</str>
        <str name="text_fr_title">Oeuvres Completes, Volume 3</str>
        <str name="text_gen_title">Oeuvres Completes, Volume 3</str>
        <str name="title">Oeuvres Completes, Volume 3</str>
        <str name="type">goudimel_book</str>
        <date name="updated">2013-11-15T19:00:00Z</date>
      </doc>
    </result>
</response>
```

Success! To get your previously-added books into Solr you just need to go in and re-save them without changing anything. They will be automatically indexed as you save.

Proceed to do the same thing for your other two models. Remember that you *will* need to change the `type` field to match the record type.

You can see the state of this tutorial with the completed save signals in the "Tutorial-Part2" branch on GitHub.