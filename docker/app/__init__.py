'''The application package'''
# pylint: disable=import-error
from flask import Flask

app = Flask(__name__)
# pylint: disable=wrong-import-position, cyclic-import
from app import views
