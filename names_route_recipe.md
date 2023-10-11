## names route recipe

# 1. Design Route Signature

```python
# names route
GET /names?add=<string>
```

# 2. Create Example as Tests

```python

"""
When: we request GET /names
With: a query parameter add=Eddie
Then: we should get a 200 response and "Alice, Eddie, Julia, Karim"
"""
def test_get_names_with_one_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Eddie, Julia, Karim"

"""
When: we request GET /names
With: mulitple names add=Eddie,Leo
Then: we should get a 200 response and "Alice, Eddie, Julia, Karim, Leo"
"""
def test_get_names_with_multiple_names(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Eddie, Julia, Karim, Leo"

"""
When: we request GET /names
With: no query parameters
Then: we should get a 400 response and "You didn't submit names to add to the list 'Alice, Julia, Karim'"
"""
def test_get_names_with_no_parameters(web_client):
    response = web_client.get('/names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You didn't submit names to add to the list 'Alice, Julia, Karim'"



```