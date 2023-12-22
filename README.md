# Hello Web Project

## Introduction

- This is my first project for Makers Module 4 - Web Applications
- It is based on a Makers Flask web & database starter project, so it contains quite a lot of example code!!
- It runs a simple web application that shows a smiley face emoji in the browser

## Objectives

I used this project to:
- [x] Learn how to set up a Flask project
- [x] Learn how to build routes
- [x] Learn how to test-drive routes

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

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv 

# Run the web server
; python app.py
# Now visit http://localhost:5001/emoji in your browser

# Or in a new terminal
curl http://localhost:5001/emoji

# When you want to stop the server program, hit Ctrl+c
```
