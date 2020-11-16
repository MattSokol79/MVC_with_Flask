from flask import Flask, jsonify

# Create an instance of our app
app = Flask(__name__)

# Put dict into a list to make it easier to transfer it into json
students = [
    {'id': 0, 'title': 'Mr.', 'firstname': 'Matt', 'lastname': 'Sokol', 'course': 'DevOps'}
]

#########################################################################
# Decorator - To create our API/URL for user to access our data in the browser
@app.route('/') # localhost:5000 is default port for Flask -> / goes to homepage in browser

# This function runs when the URL/API is accessed - ADDED HTML
def home():
    return '<h1>This is a dream team of DevOps Consultants!</h1>'

#########################################################################
# Creating our own API to display data on the specific route/URL/end point
# This will add this API/URL to the home above ->  http://127.0.0.1:5000/api/v1/student/data
@app.route('/api/v1/student/data', methods = ['GET'])

# Using ETL - Extract Transform Load
def customised_api():
    return jsonify(students) # Transforms data in the dit into Json


#########################################################################
if __name__ == "__main__":
    app.run(debug=True)

