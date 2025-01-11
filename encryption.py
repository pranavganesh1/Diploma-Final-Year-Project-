from flask import Flask, jsonify
from Crypto.Cipher import AES
import base64
import os

app = Flask(__name__)

# Function to pad the text to a multiple of 16 bytes
def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

# Function to encrypt text using AES
def aes_encrypt(text, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padded_text = pad(text)
    encrypted_bytes = cipher.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

@app.route('/hello', methods=['GET'])
def hello():
    text = "Hello World!"
    key = 'mysecretaeskey12'  # Must be 16, 24, or 32 bytes long
    encrypted_text = aes_encrypt(text, key)
    response = {'message': encrypted_text}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
