from flask import render_template, request, session, redirect, url_for
from DiagnosticAI import app
from DiagnosticAI import situation


@app.route('/', methods=["POST", "GET"])
def home():
    """
    Displays the DiagnosticAI home page
    """
    return render_template('home.html')
