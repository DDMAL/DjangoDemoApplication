# Writing Our Application

## Models

You typically start development by writing the database models. These will identify and store the data that we will use to populate our website with content.

Start by creating three files in your `models` directory, one for each model we will write: `snippet.py`, `tag.py`, and `person.py`. You should always use the singular form for naming models.

Let's start with the Snippet model. In `snippet.py` add the following code. Make sure you read it and understand what's going on before copying and pasting.

    from django.db import models


    class Snippet(models.Model):
        class Meta:
            app_label = "codekeeper"

        title = models.CharField(max_length=256, blank=True, null=True)
        snippet = models.TextField()
        tags = models.ManyToManyField("codekeeper.Tag", blank=True, null=True)
        creator = models.ForeignKey("codekeeper.Person")

        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return "{0}".format(self.title)

If you are familiar with Django models, this looks pretty straightforward. There may just be a few things that you are not aware of. The first is the Meta-class `app_label` attribute. When we break out our models into individual files, this is a necessary attribute that helps our application loader find a given model.

The `__str__` method determines what field Django uses to describe each model instance to the user. We've chosen the `title` field. This will make it easier to identify each model in the Django admin interface.

> In Python 2.7, the `__unicode__` method is used in place of `__str__`. This is because 2.7
> distinguishes between Unicode and ASCII, while 3+ uses Unicode for everything.

We will do the same thing for Tag and Person now.

person.py:

    from django.db import models


    class Person(models.Model):
        class Meta:
            app_label = "codekeeper"

        first_name = models.CharField(max_length=256, blank=True, null=True)
        last_name = models.CharField(max_length=256, blank=True, null=True)

        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return "{0}, {1}".format(self.last_name, self.first_name)

tag.py:

    from django.db import models


    class Tag(models.Model):
        class Meta:
            app_label = "codekeeper"

        name = models.CharField(max_length=255)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return "{0}".format(self.name)

Notice that we are using Foreign Key fields to relate each instance to another model. In the `Snippet` model we point to the Person and Tag objects that store data about that particular person and a reference to a list of tags.

One last thing we need to do is to add a reference to each of these in the `__init__.py` file in our `models` directory. Open up this file and add:

```
from codekeeper.models.snippet import Snippet
from codekeeper.models.person import Person
from codekeeper.models.tag import Tag
```

This allows Django to pick up on these models in the database synchronization system.

## Serializers

We will need at least one serializer for every model we create. In the `serializers` folder you created earlier, create three new files named the same as the models: `activity.py`, `person.py` and `place.py`. These will be pretty simple to start with.

`snippet.py`

    from rest_framework import serializers
    from codekeeper.models.snippet import Snippet


    class SnippetSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Snippet

`person.py`

    from rest_framework import serializers
    from codekeeper.models.person import Person


    class PersonSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Person

`tag.py`

    from rest_framework import serializers
    from codekeeper.models.tag import Tag


    class TagSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Tag

## Views

Next, let's create a couple basic views so that we can work with our system. In your `views` folder create a file, home.py.

    from django.views.generic import TemplateView


    class HomePageView(TemplateView):
        template_name = "index.html"

        def get_context_data(self, **kwargs):
            context = super(HomePageView, self).get_context_data(**kwargs)
            return context


This sets up our homepage view, which we will eventually hook up in our `urls.py`.

## Templates

For now, let's use a very simple HTML5 template. Create a new file in your `templates` directory called "base.html". In it put the following code:

```
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Time Keeper: Keep Your Time</title>

  <link rel="stylesheet" href="{{ STATIC_URL }}css/styles.css">

  <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
  <script src="{{ STATIC_URL }}js/scripts.js"></script>
</head>

<body>
{% block body %}

{% endblock %}
</body>
</html>
```

While we're at it, let's create some folders to hold our static JavaScript and CSS assets. Create two folders in the `static` directory, `css` and `js`. Since we reference files in these directories in our template, create `styles.css` in the css directory, and `scripts.js` in the js directory. We can leave them blank for now.

Let's now create the template snippet for our website's front page. Create a new file, `index.html` in your templates directory. In it place the following:

```
{% extends "base.html" %}

{% block body %}
    <h1>Hello World</h1>
{% endblock %}
```

This will be a temporary front page for our website.

# Connect the views

Now, let's connect the view we created and map it to a URL we can visit in a web browser. Open up the `urls.py` file and change it to this:

    from django.conf.urls import patterns, include, url
    from django.contrib import admin

    from codekeeper.views.home import HomePageView

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'codekeeper.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^$', HomePageView.as_view(), name="home"),
        url(r'^admin/', include(admin.site.urls)),
    )

Note in particular the two lines that reference our view: The first when we import it from our views folder, and the second where we connect it to the root of our website. The regular expression `r'^$'` indicates the base URL and `HomePageView.as_view()` is the code that handles it.

# Running our application

## Set the database

Django has a number of convenient functions for managing databases and keeping it in sync with the code we write. Our "models" that we write will be automatically turned into database tables used for storing the data, and match the structure of the fields we describe in our models.

Before starting our application we must first synchronize our database. This process converts the models that we just wrote into the database structure.

First, we need to indicate which database engine we are using. By far, the easiest to develop with is SQLite. This will create a single database file in your project directory and allow you to get up and running quickly.

Open your `settings.py` file and look for the `DATABASES` section. Change it to the following:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'codekeeper.sqlite3'),
        }
    }

This will create a file, `codekeeper.sqlite3` in our project directory.

## Migrations

A migration is a method of updating a database without needing to wipe and re-create a database from scratch if we change our models. Remember that our models are directly tied to the database structure, so if we edit our models—for example, adding or removing a field—we must also make sure the data contained in the database reflects these edits.

Without migrations, updating our website with existing data is an awkward and error-prone process. If we wanted to make a change to our models in a production website we would need to dump the data, re-structure it according to a new structure, and then re-import it into the new database structure. This is a lot of work, and can lead to loss of data if you're not careful.

Migrations keep track of your model changes and helps synchronize your database without dumping your data. (You should have a backup on hand, though, in case it fails!)

To begin, we must first describe the initial state of our database models.

    $> python manage.py makemigrations codekeeper

This tells Django to create an initial migration for our application.

If successful you should now see a 'migrations' folder in your project. As you change your models you will run a similar command and the changes to the database structure will be kept in Python files in this folder.

For now, however, let's continue with getting our database set up.

## Synchronizing our database (the first time)

Synchronizing the database converts the Python models to actual database tables and fields. To synchronize your database, run the following command:

    $> python manage.py syncdb

If this is the first time you run it, it will ask you to create a new superuser. You should do so using an easy username and password (you will have to enter it a lot!). (I typically use something like "foo".)

Notice that part of this process checks to see if there are any existing migrations and applies them.

That's it! We should have a perfectly synchronized database now.

## Running our Application

If all has gone well we can fire up our application and take it for a spin. Type:

`python manage.py runserver`

You should see this:

```
Performing system checks...

System check identified no issues (0 silenced).
February 23, 2015 - 17:25:57
Django version 1.7.4, using settings 'codekeeper.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you open Chrome and navigate to `http://localhost:8000/` you should be greeted with "Hello World" in big letters. Success!

## Writing Views

In our previous example we wrote a generic Django class-based view to handle a simple request for "Hello World". However, in keeping with the idea of creating a Browseable API, we should think about making our home page useful for both humans *and* computers.

One of the best ways to start with this is to ensure our API is *self-describing*; that is, a machine can visit our site and configure its behaviour dynamically, according to the types of data it can retrieve. The easiest way to do this is to ensure that we provide hints on our machine-readable version of the places it can look for more information.

At the same time, we are still building a human-readable website, so we need to ensure our system is useable for people too. In many other packages, the API and human versions of the site needed completely different systems, but with Django REST framework its easy to build one view that adapts its behaviour to deliver either human or machine-readable data, as needed.

Let's first start with a look at the snippet view.

`snippet.py`

    from rest_framework import generics
    from rest_framework import renderers
    from codekeeper.models.snippet import Snippet
    from codekeeper.serializers.snippet import SnippetSerializer
    from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


    class SnippetList(generics.ListCreateAPIView):
        template_name = "snippet/snippet_list.html"
        renderer_classes = (CustomHTMLRenderer,
                            renderers.JSONRenderer,
                            renderers.BrowsableAPIRenderer)
        model = Snippet
        serializer_class = SnippetSerializer
        queryset = Snippet.objects.all()


    class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
        template_name = "snippet/snippet_detail.html"
        renderer_classes = (CustomHTMLRenderer,
                            renderers.JSONRenderer,
                            renderers.BrowsableAPIRenderer)
        model = Snippet
        serializer_class = SnippetSerializer
        queryset = Snippet.objects.all()

`SnippetList` and `SnippetDetail` each deal with delivering the requested data back to the user; the list view returns a list of all snippets, while the detail view returns a single snippet.

The `renderer_classes` on each of these views determines the types of data each view will return. These particular views have three possible returns: `CustomHTMLRenderer` (more on this in a moment), `JSONRenderer` and `BrowsableAPIRenderer`. This means that each view is available in HTML, JSON, and REST Framework's built-in browseable API view.

The `CustomHTMLRenderer` is an extension of the REST Framework's `TemplateHTMLRenderer`. Create a file in your `renderers` directory called `custom_html_renderer.py` and add to it the following code:

`custom_html_renderer.py`

    from rest_framework.renderers import TemplateHTMLRenderer


    class CustomHTMLRenderer(TemplateHTMLRenderer):
        def render(self, data, accepted_media_type=None, renderer_context=None):
            """
            Renders data to HTML, using Django's standard template rendering.
            The template name is determined by (in order of preference):
            1. An explicit .template_name set on the response.
            2. An explicit .template_name set on this class.
            3. The return result of calling view.get_template_names().
            """
            renderer_context = renderer_context or {}
            view = renderer_context['view']
            request = renderer_context['request']
            response = renderer_context['response']

            if response.exception:
                template = self.get_exception_template(response)
            else:
                template_names = self.get_template_names(response, view)
                template = self.resolve_template(template_names)

            context = self.resolve_context({'content': data}, request, response)
            return template.render(context)

The purpose of this custom renderer is simple, and can be found on the second-last line of the `render` method:

    context = self.resolve_context({'content': data}, request, response)

This exposes the `content` variable in the templates containing the response data. (Without this it is difficult to get to the particular data in the response in the template).

For the templates, you should create a folder in your `templates` folder called `snippets` and in this folder create two files: `snippet_list.html` and `snippet_detail.html`. These will contain the code for templating the list and detail views, respectively.

For now, you can do a very simple placeholder template.

`snippet_list.html`

    {% extends "base.html" %}

    {% block body %}
    <h1>List</h1>
    <ul>
    {{ content }}
    {% for snippet in content %}
        <li><a href="{{ snippet.url }}">{{ snippet.title }}</a></li>
    {% endfor %}
    </ul>

    {% endblock %}

`snippet_detail.html`

    {% extends "base.html" %}

    {% block body %}
        <h1>Detail</h1>
        <h2>Snippet title: {{ content.title }}</h2>
        <p>{{ content.snippet }}</p>
        <p>{{ content.creator }}</p>

    {% endblock %}

> Notice that in the List template, we are iterating through a list of snippets in "content", while in the detail template,
> "content" is the snippet object itself.

Next, let's wire this up in our `urls.py`. 

`urls.py`

    from django.conf.urls import patterns, include, url
    from django.contrib import admin

    from codekeeper.views.home import HomePageView
    from codekeeper.views.snippet import SnippetList, SnippetDetail

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'codekeeper.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^$', HomePageView.as_view(), name="home"),
        url(r'^snippets/$', SnippetList.as_view(), name="snippet-list"),
        url(r'^snippet/(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name="snippet-detail"),
        url(r'^admin/', include(admin.site.urls)),
    )

Before we continue, we'll need to also create the same view for our `Person` objects. This is because in order to render a `Snippet`, Django REST Framework needs to *also* need to know how to render a `Person` since they are related through a ForeignKey relationship.

Our `views/person.py` file looks very similar to our `snippet.py`

`person.py`

    from rest_framework import generics
    from rest_framework import renderers
    from codekeeper.models.person import Person
    from codekeeper.serializers.person import PersonSerializer
    from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


    class PersonList(generics.ListCreateAPIView):
        template_name = "person/person_list.html"
        renderer_classes = (CustomHTMLRenderer,
                            renderers.JSONRenderer,
                            renderers.BrowsableAPIRenderer)
        model = Person
        serializer_class = PersonSerializer
        queryset = Person.objects.all()


    class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
        template_name = "person/person_detail.html"
        renderer_classes = (CustomHTMLRenderer,
                            renderers.JSONRenderer,
                            renderers.BrowsableAPIRenderer)
        model = Person
        serializer_class = PersonSerializer
        queryset = Person.objects.all()

Add these lines to your `urls.py` (making sure you import the views!):

    url(r'^people/$', PersonList.as_view(), name="person-list"),
    url(r'^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name="person-detail"),


`place.py`
```
from codekeeper.models.place import Place
from codekeeper.serializers.place import PlaceSerializer
from rest_framework import generics

class PlaceList(generics.ListCreateAPIView):
    model = Place
    serializer_class = PlaceSerializer


class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Place
    serializer_class = PlaceSerializer
```

Now, let's hook up these new views in our `urls.py` file. It should look like this:

```
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from codekeeper.views.activity import ActivityList, ActivityDetail
from codekeeper.views.place import PlaceList, PlaceDetail
from codekeeper.views.person import PersonList, PersonDetail

urlpatterns = []

urlpatterns += format_suffix_patterns(
    patterns('codekeeper.views.main',
        url(r'^$', 'home'),
        url(r'^browse/$', 'api_root'),

        url(r'^activities/$', ActivityList.as_view(), name="activity-list"),
        url(r'^activity/(?P<pk>[0-9]+)/$', ActivityDetail.as_view(), name="activity-detail"),
        url(r'^places/$', PlaceList.as_view(), name="place-list"),
        url(r'^place/(?P<pk>[0-9]+)/$', PlaceDetail.as_view(), name="place-detail"),
        url(r'^people/$', PersonList.as_view(), name="person-list"),
        url(r'^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name="person-detail"),

        url(r'^admin/', include(admin.site.urls)),
))
```

*Note*: Notice the differences in plurals (for lists) and singulars, especially for "people" and "activities."

Finally, let's add a temporary configuration parameter in our `settings.py` to define the default renderer. Scroll to the bottom and add the following:

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}
```

Once all of this is in place, make sure your develoment server is still running and then refresh the page. You should see something like this:

![Figure 5](figures/figure5.png)


Note: Make sure to use Google Chrome because the links may not work in Safari.
This is the beginning of our API! Clicking on any of the links will bring you to a blank page, but that's because we have no content in our system yet.

# The Django Admin interface

Before we continue, let's look at the Django Admin interface. This will allow us to directly enter data into our database with a tool that comes with Django.

Finally, create a new folder, 'codekeeper/admin' and add two new files, `__init__.py` and `admin.py`.

Create the following in this file:

```
from django.contrib import admin

from codekeeper.models.activity import Activity
from codekeeper.models.person import Person
from codekeeper.models.place import Place


class ActivityAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Place, PlaceAdmin)
```

In the `__init__.py` file add the following line:

`from codekeeper.admin.admin import *`

Start your development server and point your web browser to `http://localhost:8000/admin`. You should be brought to a log-in page, where you should enter the username and password you entered when you synchronized your database.

Once in you should be at a screen that looks like this:

![Figure 6](figures/figure6.png)

Clicking on any of the content types will bring you to a screen where we can add or edit records.

Before continuing, notice that "Activitys" and "Persons" are not properly named -- they should be "Activities" and "People". Django did its best to guess the plural form, but sometimes it gets it wrong. Let's fix this up.

Go to your `models/activity.py` file and change your `Meta` class to the following:

```
class Meta:
    app_label = "codekeeper"
    verbose_name_plural = "activities"
```

Do the same type of change for your `models/person.py` file. If you did not quit your development server in your terminal, you should now just be able to refresh the page and see your changes.

![Figure 6b](figures/figure6b.png)

Now, let's create some dummy data to play with.

## Entering data

Start with the Activity entry and create a couple activities and time. It doesn't matter what you enter -- jogging, answering e-mails, browsing facebook -- this is just to get a feel for how this site will work.

You will notice that you need to specify both a location and a partner for this activity. The "+" sign next to each of these fields allows you to add new entries to these tables in place.

After you've got all of your data entered, go to `http://localhost:8000/browse` to see what data is reflected in your API.

## Review

Let's pause for a moment and review where we are now.

We have an application with some basic testing data in it that allows us to view and browse the site in a raw data form. We have the Django Admin interface up and running.

This is a good start, but it's not very human friendly. In our next section let's focus on getting our "look and feel" up and running.

# Creating the user interface

Recall the role of the "Renderers" that we discussed earlier. Their job is to do "content negotiation" -- essentially deciding which format the client (human or computer) wishes to see. 

Since our web application will be primarily focused on human users, we should make sure that the HTML interface is the default interface.

Let's begin by creating a very simple renderer. In your `renderers` folder create a file called `custom_html_renderer.py` with the following code:

```
from rest_framework.renderers import TemplateHTMLRenderer


class CustomHTMLRenderer(TemplateHTMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders data to HTML, using Django's standard template rendering.

        The template name is determined by (in order of preference):

        1. An explicit .template_name set on the response.
        2. An explicit .template_name set on this class.
        3. The return result of calling view.get_template_names().
        """
        renderer_context = renderer_context or {}
        view = renderer_context['view']
        request = renderer_context['request']
        response = renderer_context['response']

        if response.exception:
            template = self.get_exception_template(response)
        else:
            template_names = self.get_template_names(response, view)
            template = self.resolve_template(template_names)

        context = self.resolve_context({'content': data}, request, response)
        return template.render(context)
```

This will form the basis for our view renderers.

Open your `views/activity.py` and add the following code:

```
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer

class ActivityListHTMLRenderer(CustomHTMLRenderer):
    template_name = "activity/activity_list.html"


class ActivityDetailHTMLRenderer(CustomHTMLRenderer):
    template_name = "activity/activity_detail.html"
```

Repeat this for both Place and Person, editing the name of the class and the template name as needed.

Next, let's create our templates that we have defined for our renderers. In our `templates` directory create the `activity`, `place` and `person` directories, and then create each of the template files that you referenced (e.g., 'activity/activity_list.html' and 'activity/activity_detail.html')

Now, let's edit each of our views to tie in the HTML renderers. For each one of your views add the following lines, customizing as necessary:

`renderer_classes = (JSONRenderer, JSONPRenderer, ActivityListHTMLRenderer)`

or 

`renderer_classes = (JSONRenderer, JSONPRenderer, ActivityDetailHTMLRenderer)`

At the top of each views file you should import the built-in JSON and JSONP renderers as well:

`from rest_framework.renderers import JSONRenderer, JSONPRenderer`

Now you should be able to start your development server and navigate to `http://localhost:8000/activities/`. However, you are only seeing a blank page! Let's try adding some text to `activity/activity_list.html`.

```
{% extends "base.html" %}

{% block body %}
    <h4>Hello World</h4>
{% endblock %}
```

If you refresh your page. "Hello World" should show up for you now.

However, there's something important going on here. Remember that our web site *should* respond to either request for HTML content, or requests for JSON content. What happens if we try and query the same URL with an `Accept: application/json` header? Open up a new terminal window (make sure your development server is still running) and use curl to query the server:

`$> curl -XGET -H "Accept: application/json" http://localhost:8000/activites/`

You should get the following response:

```
~|⇒ curl -XGET -H "Accept: application/json" http://localhost:8000/activities/
[{"url": "http://localhost:8000/activity/1/", "title": "Answering E-mail", "start_time": "2014-04-25T21:28:03Z", "end_time": "2014-04-25T00:00:00Z", "place": "http://localhost:8000/place/1/", "partner": null, "created": "2014-04-25T21:28:15.953Z", "updated": "2014-04-25T21:28:15.953Z"}, {"url": "http://localhost:8000/activity/2/", "title": "Browsing Facebook", "start_time": "2014-04-25T12:00:00Z", "end_time": "2014-04-25T21:28:48Z", "place": "http://localhost:8000/place/1/", "partner": null, "created": "2014-04-25T21:28:51.205Z", "updated": "2014-04-25T21:28:51.205Z"}, {"url": "http://localhost:8000/activity/3/", "title": "Jogging", "start_time": "2014-04-24T12:00:00Z", "end_time": "2014-04-24T13:00:00Z", "place": "http://localhost:8000/place/3/", "partner": "http://localhost:8000/person/1/", "created": "2014-04-25T21:29:34.652Z", "updated": "2014-04-25T21:38:36.355Z"}]
```

Just for fun, let's change our Accept header to text/html and try again:

```
$> curl -XGET -H "Accept: text/html" http://localhost:8000/activities/
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>codekeeper: Keep your Time</title>

  <link rel="stylesheet" href="/static/css/styles.css">

  <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
  <script src="/static/js/scripts.js"></script>
</head>

<body>

    <h4>Hello World</h4>

</body>
</html>
```

Now we have the beginnings of a database-driven website AND API. You should give yourself a pat on the back for getting this far.

## Displaying data in the templates

Let's take a closer look at the `renderers/custom_html_renderer.py` file and the class we defined in it. You'll notice that towards the end it looks like this:

```
context = self.resolve_context({'content': data}, request, response)
return template.render(context)
```

The `context` variable is what is responsible for passing along the data from our view to the template. The most important thing to note here is the `content` key word. This is the variable that will allow us to access all the data that has been passed through this renderer and into our template system.

> Note: If you're ever wondering what fields, exactly, are available in your
> template, you can print the `content` variable directly by rendering it
> in a Django template. Just put `{{ content }}` in your template and refresh.

To see how this might work, open up the `activity/activity_list.html` template file and replace the content of the "body" block with the following Django template code:

```
{% block body %}
    <ul>
    {% for activity in content %}
        <li>{{ activity.title }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```
This will render a list of the activities we have in our database in our web browser. It doesn't look like much, but we know it works.

![Figure 8](figures/figure8.png)

Let's bring in some CSS and JavaScript libraries to start making this look a little better.

## Bootstrap and jQuery

Twitter Bootstrap is a collection of CSS styles and JavaScript scripts that make creating a good-looking website relatively easy. It has styles for buttons and other form controls, as well as a powerful grid system for creating a pleasing layout.

You should begin by downloading the files from the [Bootstrap Website](http://getbootstrap.com).

You will have three folders, `css`, `js`, and `fonts`. You should move the contents of `css` and `js` to your existing folders in your `static` folder, and then copy the whole `fonts` directory to your `static` folder.

[jQuery](http://jquery.com) is a JavaScript library that makes dealing with JavaScript a lot easier. You should download both the 'compressed' and 'uncompressed' versions and put them in your `static/js` folder as `jquery.js` and `jquery.min.js`. jQuery will also complain if it can't find it's "map" file, so you should download the map file as well and put it in `static/js`.

To hook these up we just edit our `base.html` file and import the files.

Edit your `base.html` file to include these files like this:

```
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>codekeeper: Keep your Time</title>

  <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap.css">
  <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap-theme.css">
  <link rel="stylesheet" href="{{ STATIC_URL }}css/styles.css">

  <script src="{{ STATIC_URL }}js/jquery.js"></script>
  <script src="{{ STATIC_URL }}js/bootstrap.js"></script>
  <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
  <script src="{{ STATIC_URL }}js/scripts.js"></script>
</head>

<body>
    <div class="container">
        <div class="page-header">
            <div class="row">
                <div class="col-md-2">
                    <img src="{{ STATIC_URL }}img/timekeeper.jpg" />
                </div>
                <div class="col-md-10">
                    <h1>TimeKeeper</h1>
                    <p class="lead">Keep your Time</p>
                </div>
            </div>
        </div>
        {% block body %}

        {% endblock %}
    </div>
</body>
</html>
```

Note that we've added a little image of a clock in our `static/img` folder. You should do the same.

Just to round it out, let's update our `index.html` template to allow users to click links to browse our site:

```
{% extends "base.html" %}

{% block body %}
    <h1>Explore our site</h1>
    <ul>
        <li><a href="/activities">Activities</a></li>
        <li><a href="/places">Places</a></li>
        <li><a href="/people">People</a></li>
    </ul>
{% endblock %}
```

Visiting the website in a browser will now display our base template with the data from each of the other templates in the body region. Now it's starting to come together.

## Templating the detail and list pages

To save space and time writing this section, I won't go through every step of the customization and design of the pages, but I will demonstrate how to theme the "activity" list and detail pages. We can expand the templates created previously and add some basic information display. Remember that we are accessing everything on the model through the `content` variable. 

Open up the `activity/activity_list.html` page. We will make a small change to link each item in the list to an item page.

```
{% extends "base.html" %}

{% block body %}
    <ul>
    {% for activity in content %}
        <li><a href="{{ activity.url }}">{{ activity.title }}</a></li>
    {% endfor %}
    </ul>
{% endblock %}
```

If you refresh your activity list page now, the items in the list should be hyperlinked. Clicking on the link will show you a blank page. To customize this look, add the following code to `activity/activity_detail.html`.

```
{% extends "base.html" %}

{% block body %}
    <h2>{{ content.title }}</h2>
    <dl>
        <dt>Start Time</dt>
        <dd>{{ content.start_time }}</dd>
        <dt>End Time</dt>
        <dd>{{ content.end_time }}</dd>
    </dl>
{% endblock %}
```

Notice here that we use the `content` variable to access the fields of the model that we are displaying.

If you refresh the detail page for one of your activities, you should now see a display of the information contained in your database for each entry in your activity table.

You now have the basics for inserting data into a template, so you can build the list and detail views on your own. If you get stuck you should refer to the templates in the GitHub repository for this tutorial for any further changes and modifications.

# Extended Serializers

It's time we took a closer look at serializers.

Let's imagine that I would like to display the title of the place for each activity. Currently, the only data the serializer is giving me is a URL to retrieve the place record -- not the actual data itself.

Here is a cURL request and a JSON response of an activity to illustrate:

```
$> curl -XGET -H "Accept: application/json" http://localhost:8000/activity/1/

{
    "url": "http://localhost:8000/activity/1/",
    "title": "Jogging",
    "start_time": "2014-04-26T18:10:08Z",
    "end_time": "2014-04-26T18:10:11Z",
    "place": "http://localhost:8000/place/1/",
    "partner": "http://localhost:8000/person/1/",
    "created": "2014-04-26T18:10:55.376Z",
    "updated": "2014-04-26T18:10:55.376Z"
}
```

To get the place name, we can embed a place serializer within our activity serializer. Open up `serializers/activity.py` and create a new serializer for your place data. Your file should look like this:

    from timekeeper.models.activity import Activity
    from timekeeper.models.place import Place
    from rest_framework import serializers

    class PlaceActivitySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Place

    class ActivitySerializer(serializers.HyperlinkedModelSerializer):
        place = PlaceActivitySerializer()

        class Meta:
            model = Activity

Now the request for the same activity results in this:

    {
        place: {
            url: "http://localhost:8000/place/1/",
            name: "Gym",
            latitude: null,
            longitude: null,
            created: "2014-04-26T18:10:22.523Z",
            updated: "2014-04-26T18:10:22.523Z"
        },
        url: "http://localhost:8000/activity/1/",
        title: "Jogging",
        start_time: "2014-04-26T18:10:08Z",
        end_time: "2014-04-26T18:10:11Z",
        partner: "http://localhost:8000/person/1/",
        created: "2014-04-26T18:10:55.376Z",
        updated: "2014-04-26T18:10:55.376Z"
    }

We can now access the title of our place through the `place` field. Open your `templates/activity/activity_list.html` and add a column for the place.

    {% extends "base.html" %}

    {% block body %}
        <table class="table">
            <thead>
                <tr>
                    <th>Activity</th>
                    <th>Place</th>
                </tr>
            </thead>
            <tbody>
                {% for activity in content %}
                <tr>
                    <td><a href="{{ activity.url }}">{{ activity.title }}</a></td>
                    <td>{{ activity.place.name }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endblock %}

## Computed Fields

In our models we can define methods that can be used to process and extract information stored in that model. We have already seen a very simple example of this with the `__unicode__` method on the Person model:


    class Person(models.Model):
        ...
        def __unicode__(self):
            return u"{0}, {1}".format(self.last_name, self.first_name)

In other words, a computed field is a model method that acts like a field. To illustrate, let's make computed field that can display the person's name as "Firstname Lastname":

    @property
    def full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)

We can now use this in our serializer to deliver the person's full name in "natural" order:

Change your `serializers/person.py` to the following:

    from timekeeper.models.person import Person
    from rest_framework import serializers

    class PersonSerializer(serializers.HyperlinkedModelSerializer):
        full_name = serializers.Field(source="full_name")

        class Meta:
            model = Person

Now we have a new field in our output, `full_name` which we can use to display a more natural, human-friendly version of the person's name.

    $> curl -XGET -H "Accept: application/json" http://localhost:8000/person/1/

    {
        "full_name": "Kris Kringle",
        "url": "http://localhost:8000/person/1/",
        "first_name": "Kris",
        "last_name": "Kringle",
        "created": "2014-04-26T18:10:41.077Z",
        "updated": "2014-04-26T18:10:41.077Z"
    }

For now, we'll leave our Django web application alone and shift to looking at Solr.