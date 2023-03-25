from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/<string:text>')
def encode(text):
    encoded = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encoded += chr((ord(char) - 97 + 5) % 26 + 97)
            else:
                encoded += chr((ord(char) - 65 + 5) % 26 + 65)
        elif char.isdigit():
            encoded += str((int(char) + 5) % 10)
        else:
            encoded += char
    return jsonify({'result': encoded})

@app.route('/status')
def status():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=80)
