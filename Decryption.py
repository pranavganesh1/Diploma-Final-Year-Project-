from Crypto.Cipher import AES
import base64

# Function to unpad the decrypted text
def unpad(text):
    return text[:-ord(text[-1])]

# Function to decrypt text using AES
def aes_decrypt(encrypted_text, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    return unpad(decrypted_bytes.decode('utf-8'))

# Example usage:
url = "http://65.0.179.193/hello"
import requests
response = requests.get(url)
if response.status_code == 200:
    response_dict = response.json()
    encrypted_text = response_dict["message"]
    print(f"Encrypted: {encrypted_text}")
    
    key = 'mysecretaeskey12'  # Same key used for encryption
    decrypted_text = aes_decrypt(encrypted_text, key)
    print("Decrypted:", decrypted_text)
else:
    print("Failed to fetch data. Status code:", response.status_code)
