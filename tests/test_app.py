# Tests for your routes go here

"""
When I send a request GET /wave?name=Natalie
We get the status code 200 OK
And the response "I am waving at Natalie"
"""
def test_get_wave_with_argument(web_client):
    response = web_client.get("/wave?name=Natalie")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I am waving at Natalie"


"""
When I send a request POST /submit
With arguments name = "Andy" and message = "Hello!"
We get the response to be 'Thanks Andy, you sent this message: "Hello!"'
"""
def test_post_submit_with_arguments(web_client):
    response = web_client.post("/submit", data={
        "name": "Andy", 
        "message": "Hello!"
    })
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Thanks Andy, you sent this message: "Hello!"'

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
