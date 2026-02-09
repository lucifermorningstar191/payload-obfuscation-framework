import base64

def encode_payload(payload):
    encoded = base64.b64encode(payload.encode())
    return encoded.decode()
