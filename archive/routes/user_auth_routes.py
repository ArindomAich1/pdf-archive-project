from flask import Blueprint

def create_blueprint():
    auth = Blueprint("auth", __name__, url_prefix="/auth")

    #Write Your Code Here

    return auth