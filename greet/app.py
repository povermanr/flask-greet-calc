from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """welcome"""
    return "Welcome"


@app.route('/welcome/home')
def welcome_home():
    """home"""
    return "Welcome Home"


@app.route('/welcome/back')
def welcome_back():
    """back"""
    return "Welcome Back"
