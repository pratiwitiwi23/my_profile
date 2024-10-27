from flask import Flask, url_for, redirect
import os

def index():
    """ The function returns the text of a document """
    return redirect(url_for('static', filename='index.html'))

folder = os.getcwd() # remembering the current working folder
# Creating a web application object:
app = Flask(__name__, static_folder=folder) # the first parameter is the name of the module for web app, 
                        # the parameter named static_folder defines the name of the folder containing the static files 
# creating a rule for URL '/': 
app.add_url_rule('/', 'index', index)   # when receiving a GET request to the '/' address on this site,
                                        # the index function will be run, and its value will be the response to the request.
if __name__ == "__main__":
    # Starting the web server:
    app.run()