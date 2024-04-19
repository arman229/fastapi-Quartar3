Questions
1)query parameters adn string validation 1 deprecated ...  
2) path parameters and numeric validation Note So, you should declare , neverthless,even if

exotic(egzotik: غیر ملکی/اجنبی)

# Module

In Python, a file is simply a module.

# Package

In Python, if a folder contains a file named **init**.py(This file may or may not be empty), then that folder will behave as a package.
Schema
A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

A "path" is also commonly called an "endpoint" or a "route".
"Path" here refers to the last part of the URL starting from the first /.
So, in a URL like:
https://example.com/items/foo
...the path would be:
/items/foo
"Operation" here refers to one of the HTTP "methods".
POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.

Pydantic¶
All the data validation is performed under the hood by Pydantic,

Note That
if we define two same paths route than the first one will be executed since the path matches the first
Note that:
When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

- Request Body
  A request body is data sent by the client to your API.
- Response Body
  A response body is the data your API sends to the client.
  Note: Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.

- Difference between Query paramerters and request body ?
  Query paramerters:
  Query parameters are part of the URL and are visible in the address bar of a browser. They are typically used for filtering or providing additional information to the endpoint. Query parameters are passed in the URL after a ? character and are in the form of key=value pairs separated by & symbols.
  Request body:
  The request body contains data that needs to be sent to the server as part of the HTTP request. This data is typically in JSON format, but it can also be in other formats like form data or XML. Request bodies are commonly used for creating or updating resources.

  Note:
  If the parameter is also declared in the path, it will be used as a path parameter.
  If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
  If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.

* Regular expression
  We can define a regular expression pattern that the parameter should match
  Embed a single body parameter¶
  Let's say you only have a single item body parameter from a Pydantic model Item.

By default, FastAPI will then expect its body directly.

But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters, you can use the special Body parameter embed
