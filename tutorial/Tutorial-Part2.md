# System architecture

Now that we have Django set up, let's step back for a minute and consider the web application we want to build. For the purposes of this example, we want to build a web application that keeps track of a person's time spent doing a particular activity. We will start by identifying the principle functional requirements of this web application.

To start, we should identify the different data types that we want to track. To keep this example simple, we will track just three data types: Activities, Places, and People. An Activity (like exercising, or talking on the phone) can occur in many Places (gym, living room), and with different People (a friend, a colleague). These data types will form the core functionality of our application.

Next, we know that we would like this web application to serve data for both humans and computers to consume. That is, we want to create both a website and a web service API to allow our data to be used by other systems. Fortunately, the Django REST Framework (which we have already installed) takes a lot of the work out of constructing such a site. By the end of this tutorial we will have a system where you can query the same URL and, depending on the "content type" that is requested, be returned either HTML (for web browsers) or JSON (for computer consumption).

Finally, we will want to add a Solr search engine to this application, to allow us to search and retrieve items in our database quickly. In the real world, a system of this scale will not need Solr, but we will construct one anyway as an example.

## Model-View-Controller (or Model-Template-View in Django)

Django uses the Model-View-Controller (MVC) paradigm, but it is important to note that it renames the concepts to Model-Template-View (MTV). Despite the change in name, the way they work is the same. (I will use the Django version of the names, just so you don't get confused, but I will include the "traditional" name for them in parentheses).

A Model (Model) allows you to model the data that we have in the system. These can be thought of as the structure of your database, and the way you would store your data in that database. For example, one of our data types that we have identified is a "Place". Accordingly, we will create a "Place" model to store information about Places (location, name).

A Template (View) allows you to display the data to a user in a way that makes sense. A template for all Places might have a table listing all the places you keep track of, while a template for a specific place may display extensive information about that place, including all the activities that you have done there. Templates are the "look and feel" portion of your website, and control how users interact with the data on your site.

Views (Controllers) are what tie Models and Templates together. In Django, views respond to requests from users and retrieve data from the models, and then apply the templates to these requests. Views are mapped in the `urls.py` file, where you establish patterns (via regular expressions) that determine which view should respond to which request. If a user asks for '/place/123', this is mapped to the view that manages places, and the ID (123) is passed along as the particular place to render in your view.

![Figure 2 (From Apple's developer documentation)](figures/figure2.gif)

## MVC Extended in the Django REST Framework

In the application we will build, there are two other components that supplement the MTV (MVC) architecture. These are Serializers and Renderers. You may not have heard of them before -- these are specific to the Django REST Framework module that we installed earlier.

Serializers sit between the Model and the View. A serializer determines which fields from the model will be passed along to the view, and how these fields should be represented. For example, a field that references a relationship (for example, the relationship between an Activity and a Place) can be retrieved as an array of data, representing each Place. Or, it could be retrieved as a list of URLs that point to the record of that Place.

Renderers sit between the View and the Template. Their job is to automatically choose which template to apply to a request. In our application we will want both humans and computers to access the same data at the same URL. If a human visits "/place/123" in their browser, they will expect to see an HTML version of the page. However, if a computer visits "/place/123" as part of an automated system, they will expect to retrieve JSON data. A Renderer is the layer that manages this process. Renderers will respond to a request for a particular content type (we will see more on this later) and deliver the appropriate rendered template (HTML or JSON) back.

## REST (REpresentational State Transfer)

REST is not a technology. It is a way to organize the structure of a site as an architectural principle. While the theory behind REST is quite dense, there are four main components that we will use in our application.

The first is that everything is a resource. To understand why this is important, consider the following URL:

`http://example.com/res.cgi?recordId=123&type=place&action=retrieve&format=html`

I'm sure we have all seen examples of this type of URL. This URL uses _query parameters_ to pass in actions that are executed by the server. Consider a second example:

`http://example.com/res.cgi?type=place&action=list&format=json`

Rather than giving an ID, this request asks for a list of places to be returned, but rendered in JSON.

Finally, to round out our examples of non-RESTful URLs, consider this URL:

`http://example.com/res.cgi?recordId=123&type=place&action=edit&format=html`

This set of query parameters sets the system to do something quite different -- edit a place record.

## Problems

The problems associated with these URLs are not a question of whether or not they will *work*. Even the most inexperienced coder can read in the parameters from the URL and cause their application to react appropriately from the input.

However, this is a lot of work that does not need to be done. It turns out that a lot of this behaviour is *already* defined in the HyperText Transfer Protocol (HTTP) specification. Creating a web application that performs standard Create/Read/Update/Destroy functions with a custom URL routing, permissions, and lookup functionality reinvents most of HTTP — and often very badly!

Since our web applications will always run over HTTP, then, we should leverage this fact and delegate as much of our application’s behaviour to adhere to the protocol. In the long run, it will produce easier, more maintainable, and more secure code.

## Resources

REST places the emphasis on identifying resources in your application and using logical URL construction to provide an intuitive way of identifying resources. Consider this alternative to the first URL example:

`http://example.com/place/123`

This provides the exact same functionality as the first example, but is more readable and more logical. It follows a pattern:

`http://example.com/:coll/:id`

Where `:coll` is a particular collection and `:id` is the ID of a resource in this collection.

To retrieve all records in a collection, it is reasonable to assume that we can follow the same pattern:

`http://example.com/:coll/`

Without passing a particular ID, our system should respond by giving us all pieces. Similarly:

`http://example.com/places/`

`http://example.com/place/123`

We would expect that these would both respond in similar ways, retrieving a list of places in our application, or one particular place. This architecture is the first component of a RESTful system.

You may have noticed, however, that there are two parts missing from this. We can retrieve a place, but what if we want to edit an existing place? Or delete a place? In our previous examples there was an "&action=" query parameter that determined the action our application would take; however, this has gone missing from our RESTful examples. We will address this next.

## Verbs

All web clients operate over the HTTP. This protocol is stateless, meaning that for each request enough information must be sent from the client to the server so that the server can fulfill the request -- no context information about the state of a client is "stored" on the server. To send this information, each HTTP request contains several "header" fields that describe the client and the nature of the content being requested.

One of the most important request parameters is the action that is sent with a request (which we will call “verbs”, but you may already know them as the “HTTP Methods”). Two of these will be familiar to you if you have done any form processing on the web, while the other two will likely not:

 * `GET`
 * `POST`
 * `PATCH` (`PUT`)
 * `DELETE`

> In the application we will build, we will use the newer `PATCH`
> method instead of the older `PUT` method. The reasons for
> this will be explained later in this section.

The `GET` verb tells the server that the client is asking to retrieve the resource identified at a particular URL. The important thing to recognize about using `GET` is that it should *never* change the state of the resources on the server. You must never pass in commands that will alter or remove resources on the server using the GET method.

So our first example can be rewritten to show the implicit HTTP verb:

`GET http://example.com/place/123`

We will skip `POST` for a moment and discuss `PATCH` and `DELETE`. These are used to send commands for editing ("PATCHing") a record, and deleting a record. This is applied rather intuitively:

`PATCH http://example.com/place/123`

`DELETE http://example.com/place/123`

Similarly, if you wanted to delete all pieces you could send a request to the collection level:

`DELETE http://example.com/place/`

With `PATCH` requests we must also send along the data that is used to edit the record. This is done in the "body" of the request, which we will look at later, but for now just imagine that it is like an e-mail attachment.

> The difference between `PATCH` and `PUT` is that `PATCH` can 
> perform a partial record update, returning only the changed
> fields on a record to the server, while `PUT` must return the
> entire modified record to the server.

Finally, `POST` is used to create a record. This is typically done by sending a request to the collection level, rather than individual records:

`POST http://example.com/piece/`

Like `PATCH`, the data used to create the record with a POST request is sent along in the body of the request.

As you can see, `PATCH`, `DELETE`, and `POST` can delete or alter your data, while `GET` requests, beyond allowing people to see a record, cannot change the state of the server. If you design a system such that no data on the server can be altered with a `GET` request, and that `PATCH`, `DELETE`, and `POST` requests are only allowed by authorized users, it is easier to guard against unauthorized access to your application.

### Searching and Filtering

One use of query parameters is for limiting results within a collection of objects. For example:

`http://example.com/places/?title=home`

might retrieve only those places that have the word "home" in the title. Multiple facets could be combined to further restrict this:

`http://example.com/activities/?place=home&time=10:00`

might retrieve all activities that took place at home at 10am.

## Request and Response types

The third component to our RESTful architecture is the response type. In our non-REST examples, we needed to pass in `&format=html` or `&format=json` to identify which format we would like to recieve our response in. However, like the Verbs, the HTTP protocol has a built-in mechanism for content negotiation, the `Accepts` header.

To understand and view request headers, we will use the cURL tool. This is a powerful command-line utility that allows us to query a URL and receive a response in our terminal. This will become an important part of our toolbox as we build our API, so let's see how it works. I will pass in a simple command to retrieve the Google homepage using the GET method:

`curl -XGET -L http://google.com`

The `-L` parameter tells curl to follow any automated redirects. If this is successful, you will see a dump of the Google homepage in raw HTML printed to your console.

Let's look at it a bit more in-depth. Add the "-v" flag to curl and try again. We'll use the McGill homepage, since it's a little easier to parse than the Google request:

`curl -XGET -L -v http://www.mcgill.ca`

What we receive in response looks like this:

```
~|⇒ curl -XGET -v http://www.mcgill.ca
* Adding handle: conn: 0x7fa6ca804000
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x7fa6ca804000) send_pipe: 1, recv_pipe: 0
* About to connect() to www.mcgill.ca port 80 (#0)
*   Trying 132.216.177.160...
* Connected to www.mcgill.ca (132.216.177.160) port 80 (#0)
> GET / HTTP/1.1
> User-Agent: curl/7.30.0
> Host: www.mcgill.ca
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Thu, 30 Feb 2015 17:13:16 GMT
* Server Apache/2.2.0 (Fedora) is not blacklisted
< Server: Apache/2.2.0 (Fedora)
< X-Powered-By: PHP/5.3.3
< Set-Cookie: SESSdbe2636110680a18092a41d7f7cf0fc3=f3nko19tvok7cpafsp38tufm01; path=/; domain=.mcgill.ca
< Last-Modified: Thu, 30 Feb 2015 17:13:16 GMT
< ETag: "eb7507bbe1e6a1e28f9dcaa840c82cbc"
< Expires: Sun, 19 Nov 1978 05:00:00 GMT
< Cache-Control: must-revalidate
< X-Cnection: close
< Transfer-Encoding: chunked
< Content-Type: text/html; charset=utf-8
< Set-Cookie: BIGipServer~CCS_Sties~DRUPAL=867293316.20480.0000; path=/
<
```

Lines marked with an ">" indicate a *request* header; lines marked with a "<" indicate a *response* header. The request header tells the server a bit about the client we're using -- in this case, it's curl (`User-Agent: curl/7.30.0`). The server responds with a bit about what's being used to send it back (`Server: Apache/2.2.0 (Fedora)`) and then some other information about the nature of the content being sent.

Notice here that one of the request headers is the `Accept:` header. A `*/*` indicates that our client will accept all types of responses. The corresponding response header is the `Content-Type:` header, which tells our client that the server is responding with a content type of `text/html; charset=utf-8`.

Using the `Accept:` header we can alert a server to the content type our client is willing to accept. This is specified using mimetypes: unique identifiers that identify a certain computer format. If we supply `application/json` as the mimetype for an accept header, a properly-configured web service would serve back a JSON-encoded response. Similarly, an `Accept:` request for `text/html` would tell the server to respond with HTML. Fortunately all modern web browsers send this Accept type by default, so users browsing normally will not notice this process.

## Status Codes

The final RESTful principle we will adhere to is the use of HTTP Status Codes to communicate the state of our request and permit a client to act, or fail gracefully, on the result of a request.

The most familiar HTTP Status Code is the ubiquitous “404 Not Found”, but there are many, many more status codes. They are broken into groups which broadly define the type of status they are communicating:

    1XX Informational
    2XX Success
	  3XX Redirection
    4XX Client Error
    5XX Server Error

So, the 404 code is actually the server saying “I understood the request, but the page you (the client) is requesting is not on this server.”

Returning an appropriate status code to a request is a key element in allowing a client to gracefully handle a response. For example, if a client requests something that requires authentication, the server can respond with a “401 Unauthorized” response. Upon receiving this response, a client can then prompt the user to enter their authentication credentials, and then re-try the request. If the user is _authenticated_, but still not _authorized_ to perform the action, the server can then respond with a “403 Forbidden” response, which is like the server saying “I know who you are now, but I still can’t open the pod bay doors, Hal.” `</nerd>`

Ok, enough talking. Let’s get to coding!