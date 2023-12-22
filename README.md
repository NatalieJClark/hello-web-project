# Hello Web Project

## Introduction

- This is my first project for Makers Module 4 - Web Applications
- It includes a coach assessed challenge following the Challenge objectives below
- It is based on a Makers Flask web & database starter project, so it contains quite a lot of example code!!
- It contains lots of practise code for Flask routes in `app.py`. Requests can be made to these routes with curl (see [Setup](#setup))
- Some of these routes were test-driven. The tests can be found in `tests/test_app.py` and the design recipes in the relevant `route_recipe.md` file

## Objectives

I used this project to:
- [x] Learn how to set up a Flask project
- [x] Learn how to build routes
- [x] Learn how to test-drive routes

Challenge objectives:
- [x] Test-drive the following route:
```shell
# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
```
- [x] You should assert that the response status code is `200` and that the response body is the correct string.
- [x] For an extra challenge, add multiple names and sort them alphabetically.
```shell
# Request:
GET /names?add=Eddie,Leo

# Expected response (2OO OK):
Alice, Eddie, Julia, Karim, Leo
```

## Setup
```shell
# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/hello-web-project.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Run the tests (with extra logging)
; pytest tests/test_app.py -sv 

# Run the web server
; python app.py

# In a new terminal try these curl commands
; curl http://localhost:5001/hello\?name=Natalie
; curl -X POST -d "name=Alice" http://localhost:5001/goodbye
; curl "http://localhost:5001/wave?name=James"
; curl -X POST -d "name=Leo&message=Hello" http://localhost:5001/submit
; curl -X POST -d "text=How many vowels are here?" http://localhost:5001/count_vowels
; curl -X POST http://localhost:5001/sort-names
; curl -X POST -d "names=Joe,Alice,Zoe,Julia,Kieran" http://localhost:5001/sort-names
; curl "http://localhost:5001/names"
; curl "http://localhost:5001/names?add=Eddie"
; curl http://localhost:5001/emoji

# When you want to stop the server program, hit Ctrl+c
```
