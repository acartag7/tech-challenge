'''This module contains a Flask app that encodes alphanumeric strings'''

# pylint: disable=import-error
from flask import jsonify
from app import app

@app.route('/<string:plaintext>')
def encode(plaintext: str) -> jsonify:
    """Encodes a given string with a simple cipher."""
    if not plaintext.isalnum():
        raise BadRequest("Input must contain only alphanumeric characters.")
    encoded = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encoded += chr((ord(char) - 97 + 5) % 26 + 97)
            else:
                encoded += chr((ord(char) - 65 + 5) % 26 + 65)
        elif char.isdigit():
            encoded += str((int(char) + 5) % 10)
    return jsonify({'result': encoded})

@app.route('/status')
def status() -> jsonify:
    """Returns the status of the server."""
    return jsonify({'status': 'ok'})

@app.route('/help')
def show_help() -> str:
    """Returns instructions on how to use the server."""
    return """
    <h1>Instructions</h1>
    <p>To encode a string, go to /{string}</p>
    <p>The input string can only contain alphanumeric characters (A-Z, a-z, 0-9)</p>
    <p>Example: /hello</p>
    <p>Result: {"result": "mjqqt"}</p>
    <p>To check the status of the server, go to /status</p>
    """

class BadRequest(Exception):
    """Exception raised for invalid requests."""

@app.errorhandler(BadRequest)
def handle_bad_request(error) -> jsonify:
    """Handles BadRequest exceptions."""
    return jsonify({'error': str(error)}), 400
