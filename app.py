import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']
    return f"Hello {name}!"

# Request:
#POST /goodbye
#   With body parameter: name=Alice

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name']
    return f"Goodbye {name}!"

# Request:
# GET /wave

@app.route('/wave',  methods=['GET'])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"

# Request:
# POST /submit

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

# Request:
# POST /count_vowels
@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_count = 0
    for char in text:
        if char in "aeiou":
            vowel_count += 1
    return f'There are {vowel_count} vowels in "{text}"'

# Request:
# POST /sort-names
@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return "You didn't submit any names!", 400
    names = request.form['names'].split(",")
    sorted_names = ",".join(sorted(names))
    return sorted_names

# Request:
# GET /names
@app.route('/names', methods=['GET'])
def get_names():
    if 'add' not in request.args:
        return "You didn't submit names to add to the list 'Alice, Julia, Karim'", 400
    add_name_list = request.args['add'].split(",")
    names = ['Alice', 'Julia', 'Karim']
    for name in add_name_list:
        names.append(name)
    sorted_names = sorted(names)
    return ", ".join(sorted_names)

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

