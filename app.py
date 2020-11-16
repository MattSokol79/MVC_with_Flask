from flask import Flask, jsonify, redirect, url_for, render_template

# Create an instance of our app
app = Flask(__name__)

# Put dict into a list to make it easier to transfer it into json
students = [
    {'id': 0, 'title': 'Mr.', 'firstname': 'Matt', 'lastname': 'Sokol', 'course': 'DevOps'}
]

#########################################################################

# Decorator - To create our API/URL for user to access our data in the browser
@app.route('/') # -> http://127.0.0.1:5000/ ----> localhost:5000 is default port for Flask -> / goes to homepage in browser

# This function runs when the URL/API is accessed - ADDED HTML
def home():
    return '<h1>This is a dream team of DevOps Consultants!</h1>'

#def redirect():
    #return redirect("http://127.0.0.1:5000/welcome/", 200)

#########################################################################

# Creating our own API to display data on the specific route/URL/end point
# This will add this API/URL to the home above ->  http://127.0.0.1:5000/api/v1/student/data
@app.route('/api/v1/student/data/', methods = ['GET'])

# Using ETL - Extract Transform Load
def customised_api():
    return jsonify(students) # Transforms data in the dit into Json

#########################################################################

@app.route('/welcome/') # -> http://127.0.0.1:5000/welcome/
def greet_user():
    return "<h1>Welcome to DevOps</h1>"


#########################################################################

# Find out the module to redirect the user back to specific page (welcome page)
# In this case, we are creating a login url which redirects to the welcome page when accessed
@app.route('/logintest/') # -> http://127.0.0.1:5000/logintest/
def login():
    return redirect(url_for("greet_user")) # Redirects to the function greet user which has URL /welcome/

# For errors do below code
#@app.errorhandler(Exception)
#def handle_not_found(error):
    #return redirect(url_for("welcome_screen"))

#########################################################################

@app.route('/user/<username>/') # -> http://127.0.0.1:5000/user/<username>/ ----> Need to input the username in the URL in browser
def welcome_user(username):
    return f"<h1>Welcome to the dream team of DevOps {username}!</h1>"

#########################################################################

# Gets HTML into flask to be used
@app.route('/index/') # http://127.0.0.1:5000/index/
def index():
    return render_template('index.html')

#########################################################################

# Text boxes for login form

if __name__ == "__main__":
    app.run(debug=True)

