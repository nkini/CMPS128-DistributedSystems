# Project 2: A single-site Key-value store

### Due: Tuesday, April 26, 2016 - 11:59pm

### Submission:  
HW1 instructions apply about members and contribution notes. Submit the Commit URL you want us to test at: http://goo.gl/forms/CgQiDjKunG. The person submitting the form needs to enter her/his ucsc id in the members field also. Strip your Commit URLs of #comment-None, ?at=master

### Instructions

Start with going over this post: https://piazza.com/class/ilzil5nx6mb2n8?cid=76 and this post  https://piazza.com/class/ilzil5nx6mb2n8?cid=80 - The latter says, you are expected to implement *your own* key value store, and not use an existing key value store such as Redis, Couch, Mongo etc.

For your second project you will implement a REST-accessible Key-value store (KVS).  This piece of infrastructure will form the foundation of all future projects, which will extend it to become fault-tolerance and scalable.

Key-value stores provide a simple storage API in which values (arbitrary data, often semi-structured documents in formats such as JSON) are stored and retrieved by *key*.  The typical KVS API looks like:

|Call|Parameters|Returns|Example|
|----|----------|-------|--------|
|put|     key, value   |  Success or failure    | put(foo, bar) |
|get| key | value | X = get(foo) # now X=bar|
|del| key | Success or failure | del(foo) # subsequent gets to foo will fail|

In this project, you will implement a KVS in whatever way you choose.  We will only be testing its adherence to certain *functional guarantees*, which we enumerate below.  As in the last assignment, you will also create a REST API that allows users (as well as our test scripts) to interact with it over HTTP.


### Input format restrictions
- key
  - charset: [a-zA-Z0-9_] i.e. Alphanumeric including underscore, and case-sensitive 
  - size:    1 to 250 characters

- value
  - size:    1.5MB  
  (Also, please check what your server's default POST data limit is, and how to change it. We are tempted to increase this for future assignments.)
  - application/x-www-form-urlencoded  
  (This is usually how a default server would handle posted data. As an aside, please check the handling of other kinds data. We are tempted to expand this to files for future assignments.)

### Functional guarantees
- service runs on port 8080 and is available as a resource named kvs. i.e. service listens at http://server-hostname:8080/kvs
- service listens to requests on a network
- get on a key that does not exist returns an error message
- get on a key that exists returns the last value successfully written (via put) to that key, or a more recent value, if one exists
- del on a key that does not exist returns an error message
- put on a key that does not exist (say key=foo, value=bar) creates a resource at kvs/foo. Subsequent gets return 'bar' until the next put at kvs/foo
- del on a key that exists (say foo) deletes the resource kvs/foo and returns success. Subsequent gets return a 404 until the next put at kvs/foo
- put on a key that exists (say key=foo) replaces the existing value with the new value (say baz), and acknowledges a replacement in the response. Subsequent gets return 'baz' until the next put at kvs/foo.
- Even when multiple operations are being performed on the same key, their effect
(the results of GETs and the final state of the store) should be an effect 
that *could* have been produced by a single sequence of operations 
with no concurrency (this is called a "serializable" schedule of events).
(note that unless you do something crazy this shoud be trivially true for this homework, 
because we're only testing a single client, synchronous, non-distributed server setting)


### Request and Response formats

Pre-condition - localhost:49160 forwards to 8080 of the docker container running the kvs service

1. PUT localhost:49160/kvs/foo -d "value=bart"
    - case 'foo' does not exist
		  - status code : 201
		  - response type : application/json
		  - response body:
<pre>
		{
      'replaced': 0, // 1 if an existing key's value was replaced
      'msg': 'success'
		}
</pre>
    - case 'foo' exists
		  - status code : 200
		  - response type : application/json
		  - response body:
<pre>
		{
      'replaced': 1, // 0 if key did not exist
      'msg': 'success'
		}
</pre>
		
2. GET localhost:49160/kvs/foo
    - case 'foo' does not exist
      - status code : 404
      - response type : application/json
      - response body:
<pre>
			{
				'msg' : 'error',
				'error' : 'key does not exist'
			}
</pre>
    - case 'foo' exists
      - status code : 200
      - response type : application/json
      - response body:
<pre>
			{
				'msg' : 'success',
				'value': 'bart'
		 	}
</pre>

3. DELETE localhost:49160/kvs/foo
    - case 'foo' does not exist
      - status code : 404
      - response type : application/json
      - response body:
<pre>
			{
				'msg' : 'error',
				'error' : 'key does not exist'
		 	}
</pre>

    - case 'foo' exists
      - status code : 200
      - response type : application/json
      - response body:
<pre>
			{
				'msg' : 'success'
		 	}
</pre>

### Unit tests

Note that the unit tests file we provide (https://github.com/nkini/CMPS128-DistributedSystems/blob/master/HW2/HW2-unittests.py) is a subset of the test cases that we will eventually run and that you will be graded on. Please ensure you run unit tests, and we even encourage you to write your own tests up. Ask on Piazza when something isn't clear, and make no more assumptions than are necessary.

Grading this time will be strictly done on the basis of number of test cases passed. That is number of passed test cases = your grade on the assignment.
