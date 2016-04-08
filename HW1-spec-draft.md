# Assignment 1 (still a draft)

### Updates since first commit (See history to check for what changed)
1. 4/7, 6:54pm - Fixed error in resource name - echo vs echobot. All echobot replaced with echo.

For the first assignment, you will create a REST API service that is able to differentiate between GET and POST requests, and responds to GET requests for the resources 'hello' and 'echo'.

You will use Docker to create an image which must expose a web server at port 8080 that implements the REST interface below.

## REST API

### hello

Method: GET  
Resource Identifier: http://localhost:8080/hello  
Response message-body: Hello world!  

### echo 

Method: GET  
Resource Identifier: http://localhost:8080/echo  
Query parameters: msg  
Parameter format: Alphanumeric  

Call example: http://localhost:8080/echo?msg=DistributedSystems  
Response message-body: DistributedSystems  
Call example: http://localhost:8080/echo?msg=CMPS128  
Response message-body: CMPS128  


## Notes

It is important that your app understands the distinction between a GET and POST, as you will see in the Unit Tests below.

## UNIT TESTS:

Please note the importance of running and testing their submissions locally before turning them in. We can't give you a passing grade on the assignment if your container doesn't respond to these requests!

We have written unit test files in python and ruby. The cURL+shell equivalent of the unit tests are given below.

#### Installing cURL
Choose your binary for installing cURL from here:  
https://curl.haxx.se/dlwiz/?type=bin

#### Installing Unirest
http://unirest.io/ruby.html

$ sudo docker run -p 49160:8080 -d nkini/hw1  

$ curl -X GET http://localhost:49160/hello  
Hello world!

$ curl -X GET http://localhost:49160/echo?msg=AnyColourYouLike  
AnyColourYouLike

$ curl -s -i GET http://localhost:49160/anUnknownMethod | head -n 1  
HTTP/1.0 404 File not found

$ curl -s -i -X POST http://localhost:49160/hello | head -n 1  
HTTP/1.0 405 METHOD NOT ALLOWED  
Note for this POST test: Based on your library the response above may be different, what is returned may vary. However, what should NOT be returned is "HTTP/1.0 200 OK"


### Background:

Any two entities need a common vocabulary to communicate - to convey and understand. For humans, that's a language. For machines, we call this common vocabulary a protocol. It's why two machines that were created independently, with possibly different architectures can still 'understand' each other. You need more than one language to communicate. Confused? Say you have questions about making a cash deposit to your account. Not only do you need a common language (say English) to be able to ask questions, you also need to have the common vocabulary to talk about "bank", "account", "deposit", "balance" etc. So not only does communication require a language/protocol, it requires more than one - at various levels. Distributed systems would be impossible without protocols.

**HTTP:**  
HTTP is a protocol at the topmost (well, almost) level, called the application layer. It is incredibly simple, which I personally believe is the reason for its success and popularity. It consists of specifications on how a client makes a request and how a server responds. It helps to think of the internet as a file system with files stored on specific computers (servers), and HTTP defining the set of commands and handshakes that allow clients to request or manipulate files on the server. Requests are made for *resources*, which are, in case of static web pages, HTML (or indeed, any kind of media/text) files. Consider for example, when you type https://en.wikipedia.org/wiki/Quicksort into your browser window. You are the client requesting for a unique file. The address of this unique file happens to be the URL. You're basically requesting for a resource called Quicksort which resides on a server that has the name en.wikipedia.org.

**Resource:**  
The concept of a web resource has evolved during the web history, from the early notion of static addressable documents or files, to a more generic and abstract definition, now encompassing every 'thing' or entity that can be identified, named, addressed or handled, in any way whatsoever, in the web at large, or in any networked information system [1].

**HTTP Request and Response [2]:**  
The request message consists of the following:
+ A request line (e.g., GET /images/logo.png HTTP/1.1, which requests a resource called /images/logo.png from the server).  
+ Request header fields (e.g., Accept-Language: en).  
+ An empty line.  
+ An optional message body.  

The response message consists of the following:
+ A status line which includes the status code and reason message (e.g., HTTP/1.1 200 OK, which indicates that the client's request succeeded).
+ Response header fields (e.g., Content-Type: text/html).
+ An empty line.
+ An optional message body.

**HTTP Request methods [9]:**  

HTTP defines methods (sometimes referred to as verbs) to indicate the desired action to be performed on the identified resource. What this resource represents, whether pre-existing data or data that is generated dynamically, depends on the implementation of the server. Often, the resource corresponds to a file or the output of an executable residing on the server. The HTTP/1.0 specification defined the GET, POST and HEAD methods and the HTTP/1.1 specification added 5 new methods: OPTIONS, PUT, DELETE, TRACE and CONNECT. 
The official documentation is here: http://tools.ietf.org/html/draft-ietf-httpbis-p2-semantics-16#section-7.3


**REST:**  
[Personal opinion - A good name for something abstract can save about 50% of time and space of explaining IT, and I really don't like Representational State Transfer, because it conveys absolutely nothing (to me, anyway) about what it means.]

REST is a style of architecture for communication in distributed systems. It is best defined by the architectural properties [4] it induces on systems by the application of architectural constraints [5] on the components of the distributed system.

It's very hard to appreciate REST if one has not used other mechanisms like CORBA, RPC or SOAP to connect to other machines. Think of REST as being able to live your life in society interacting with others, asking for what you want and giving them what they need knowing only about 5 words (and the names of things that you want). Since the architect of REST - Roy Fielding - was also the architect of HTTP 1.1, the two are very closely related. It is not mandatory that a REST system use HTTP, but it is what is typically used. 

As simple as HTTP is, it is still powerful enough to allow you to do the 4 main operations you would do on data - Create, Read, Update, Delete.


**Web APIs [6]:**  
Web APIs are the defined interfaces through which interactions happen between an enterprise and applications that use its assets. 

In our first assignment, we will program to a specified Web API.

**Docker and Containers:**  
[7],[8]  
Docker containers wrap up a piece of software in a complete filesystem that contains everything it needs to run: code, runtime, system tools, system libraries – anything you can install on a server. This guarantees that it will always run the same, regardless of the environment it is running in. 

What docker allows us to do w.r.t. our assignments/project is provide a way of giving *you, the students* a high degree flexibility in development without the cost of having your own website/cluster running, and giving *us, the instructors* a unified way to test a number of different systems implemented in different ways. It essentially does what HTTP did - provide a way to hide the implementation and yet test the implemented system uniformly.
More details about Docker can be found in the links in the resources below.

**Resources**  
Here are a couple of docker help files that might come in handy:  
https://github.com/nkini/CMPS128-DistributedSystems/blob/master/Docker_Commands.md  
https://github.com/nkini/CMPS128-DistributedSystems/blob/master/Docker_Notes.md  
Unit tests in Python: https://github.com/nkini/CMPS128-DistributedSystems/blob/master/hw1-unittests.py
Unit tests in Ruby: https://github.com/nkini/CMPS128-DistributedSystems/blob/master/hw1-unittests.rb

Referenced links:  
[1] https://en.wikipedia.org/wiki/Web_resource  
[2] https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol  
[3] https://en.wikipedia.org/wiki/Representational_state_transfer  
[4] https://en.wikipedia.org/wiki/Representational_state_transfer#Architectural_properties  
[5] https://en.wikipedia.org/wiki/Representational_state_transfer#Architectural_constraints  
[6] https://en.wikipedia.org/wiki/Application_programming_interface#Web_APIs  
[7] https://www.docker.com/what-docker  
[8] https://docs.docker.com/mac/, https://docs.docker.com/linux/, https://docs.docker.com/windows/  
[9] https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods

The following are some of the REST server microframeworks that *might* be useful. We say *might* because, well, we haven't really used anything except Flask (python) and Sinatra. 

Java:
http://restx.io/

Python:
http://flask.pocoo.org/

Ruby:
http://www.sinatrarb.com/

Node.js:
http://restify.com/

C++11:
https://github.com/datasift/served

C:
http://www.linuxjournal.com/article/10680?page=0,0

C#:
http://nancyfx.org/

PHP:
http://www.slimframework.com/  
http://flightphp.com/

If you don't see your favorite programming language in the list above, just google "rest server your_fave_prog_lang" and look for a page that has an example that looks like the example on one of these pages: http://restx.io/, http://flask.pocoo.org/, http://www.sinatrarb.com/.

## Submission
