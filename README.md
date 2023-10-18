#  Veraleo Capital Partners Coding Test

 This repository contains three files:

 - check.py
 - query.py
 - research.py

 Each of these has been deployed to its own AWS Lambda function. Those Lambdas have been connected to AWS API Gateway so that we can query these API routes to run the code.

 API BASE URL (which does not have any unctionality and will throw an error): https://2vrfp12l60.execute-api.us-east-1.amazonaws.com

 Endpoints:

 1. Check: make a GET request to https://2vrfp12l60.execute-api.us-east-1.amazonaws.com/check.
 This will return a basic response that has my name.
 

 2. Query: make a POST request to https://2vrfp12l60.execute-api.us-east-1.amazonaws.com/query. This will return some data parsed and cleaned from the wikipedia API. I tested using [Postman](https://www.postman.com), which is a convenient tool for testing public APIs and making custom HTTP requests. Some sample URLs to test with in Postman are below. Please note that these URLs are formatted by Postman, the query value should be set in the query params fo the POST request where the key is "query" and the value is whatever the search is for.

    a. POST https://2vrfp12l60.execute-api.us-east-1.amazonaws.com/query

    - Query Parameters: {"query": "Facebook"}

    b. POST https://2vrfp12l60.execute-api.us-east-1.amazonaws.com/query

    - Query Parameters: {"query": "Superman"}

    c. POST https://2vrfp12l60.execute-api.us-east-1.amazonaws.com/query

    - Query Parameters: {"query": "NYC"}

 3. Research: make a GET request to https://2vrfp12l60.execute-api.us-east-1.amazonaws.com/research. This endpoint calls a public API to see which stocks are being talked about on Reddit the most and what the sentiments are towards those ticker symbols. It also calls another API to see stock trades made by Congressmen from the House
 Stock Watcher API. It then cross-references the results of these two calls to find the common ticker symbols that
 are actively being traded and talked about, and that should be investigated further. The API endpoint returns a list of these stocks and the corresponding sentiments towards them from Reddit.
