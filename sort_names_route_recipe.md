# {{ sort-names }} Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Sort-names route
POST /sort-names
    names: a string of comma separated names
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

"""
When: I make a POST request to /sort-names
And: I send "Natalie" as the body parameter
Then: I should get a 200 response and "Natalie"
"""
def test_post_sort_names_with_single_name(web_client):
    response = web_client.post('/sort-names', data={'names': 'Natalie'})
    response.status_code #=> 200
    response.data.decode('utf-8') #=> "Natalie"


"""
When: I make a POST request to /sort-names
And: I send "Joe,Alice,Zoe,Julia,Kieran" as the body parameter
Then: I should get a 200 response and "Alice,Joe,Julia,Kieran,Zoe"
"""
def test_post_sort_names_with_list_of_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    response.status_code #=> 200
    response.data.decode('utf-8') #=> "Alice,Joe,Julia,Kieran,Zoe"

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
```
