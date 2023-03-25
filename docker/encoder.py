"""
This module contains a Flask app that encodes alphanumeric strings
"""

import os
from flask import Flask, jsonify

flask_app = Flask(__name__)

@flask_app.route('/<string:plaintext>')
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

@flask_app.route('/status')
def status() -> jsonify:
    """Returns the status of the server."""
    return jsonify({'status': 'ok'})

@flask_app.route('/help')
def show_help() -> str:
    """Returns instructions on how to use the server."""
    return """
    <h1>Instructions</h1>
    <p>To encode a string, go to /{string}</p>
    <p>The input string can only contain alphanumeric characters (A-Z, a-z, 0-9)</p>
    """

class BadRequest(Exception):
    """Exception raised for invalid requests."""

@flask_app.errorhandler(BadRequest)
def handle_bad_request(error) -> jsonify:
    """Handles BadRequest exceptions."""
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_RUN_PORT', 80))
    flask_app.run(port=port)

# If a config file is used, the app can be started with:
# if __name__ == '__main__':
#     app.run(port=config['port'])

# The config file is a simple Python file that sets the config variables:
# config = {
#     'port': 80
# }
