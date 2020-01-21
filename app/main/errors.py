from flask import render_template, request
from . import main
from .. import db

@main.app_errorhandler(404)
def notfound(error):
    """
    Function to render the 404 error page
    """
    if request.method == "POST":
        
        welcome_message("Thank you for visiting to the Blog")
    return render_template("notfound.html"),404