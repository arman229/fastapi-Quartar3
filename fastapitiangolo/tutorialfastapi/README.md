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