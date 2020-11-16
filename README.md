# MVC with Flask in Python
MVC - Model View Controller

### Display
**Display data on the browser using HTML, CSS, JS and Bootstrap**

- HTML - Hyper Text Markup Language
- CSS - Cascading Style Sheets
- JS - JavaScript
- BOOTSTRAP

Objectives
- Build API
- Display data from python flask to specific
API call/URL/end point

**Why FLASK?**
- Flask is a VERY powerful web app framework
- Interact with DB and user interface -> Browsers etc.
- It can be used to create an API 
- Allows us to integrate with HTML, CSS, JS etc.
- Allows us to map HTTP requests to python 
functions -> URL - HTTP 'GET'
- Allows us to set the API path as URL to view
in the browser

**Running Flask**

- First install flask `pip install flask`
- How to run the Flask app `flask run`

### Creating a basic API
- First we need to import all relevant modules 
from Flask and add a dict with data for students
```python
from flask import Flask, jsonify, redirect, url_for

# Create an instance of our app
app = Flask(__name__)

# Put dict into a list to make it easier to transfer it into json
students = [
    {'id': 0, 'title': 'Mr.', 'firstname': 'Matt', 'lastname': 'Sokol', 'course': 'DevOps'}
```
- We can then use @app.route which can use URL
to go to specific areas of code in the browser
- This is the first page off the localhost
```python
# Decorator - To create our API/URL for user to access our data in the browser
@app.route('/') # -> http://127.0.0.1:5000/ ----> localhost:5000 is default port for Flask -> / goes to homepage in browser

# This function runs when the URL/API is accessed - ADDED HTML
def home():
    return '<h1>This is a dream team of DevOps Consultants!</h1>'
```
- We can then add different URL with different
functions
- Importing the data into the URL:
```python
# Creating our own API to display data on the specific route/URL/end point
# This will add this API/URL to the home above ->  http://127.0.0.1:5000/api/v1/student/data
@app.route('/api/v1/student/data/', methods = ['GET'])

# Using ETL - Extract Transform Load
def customised_api():
    return jsonify(students) # Transforms data in the dit into Json
```
- Welcome Page
```python
@app.route('/welcome/') # -> http://127.0.0.1:5000/welcome/
def greet_user():
    return "<h1>Welcome to DevOps</h1>"
```
- Can also redirect to a different URL if a specific URL
e.g. login is typed into the browser
- If you want to redirect based off an error, can use the 
errorhandler function
```python
# Find out the module to redirect the user back to specific page (welcome page)
# In this case, we are creating a login url which redirects to the welcome page when accessed
@app.route('/login/') # -> http://127.0.0.1:5000/login/
def login():
    return redirect(url_for("greet_user")) # Redirects to the function greet user which has URL /welcome/

# For errors do below code
#@app.errorhandler(Exception)
#def handle_not_found(error):
    #return redirect(url_for("greet_user"))
```
- A funtional URL which will display a message
based on what username was inputted in the URL
```python
@app.route('/user/<username>/') # -> http://127.0.0.1:5000/user/<username>/ ----> Need to input the username in the URL in browser
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps {username}!</h1>"
```
- To run the API
```python
if __name__ == "__main__":
    app.run(debug=True)
```