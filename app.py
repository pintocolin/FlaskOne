# import the Flask class from the flask module
from flask import Flask, render_template

# create the appliacation object
app = Flask(__name__)

# use decorators to link the funciton to a url
@app.route('/')
def home():
    # return "Hello Flask world"  # return a string
    return render_template('home.html')  # render the home template


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')   # Make server externally available 
