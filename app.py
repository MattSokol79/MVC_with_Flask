from flask import Flask

# Create an instance of our app
app = Flask(__name__)

# Put dict into a list to make it easier to transfer it into json
students = [
    {'id': 0, 'title': 'Mr.', 'firstname': 'Matt', 'lastname': 'Sokol', 'course': 'DevOps'}
]

# Decorator - To create our API/URL for user to access our data in the browser
@app.route('/') # localhost:5000 is default port for Flask -> / goes to homepage in browser

# This function runs when the URL/API is accessed
def home():
    return 'This is a dream team of DevOps Consultants!'

if __name__ == "__main__":
    app.run(debug=True)

