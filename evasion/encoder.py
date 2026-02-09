import base64

# -----------------------
# Base64 Encoding
# -----------------------
def encode_base64(payload: str) -> str:
    encoded = base64.b64encode(payload.encode())
    return encoded.decode()


# -----------------------
# XOR Encoding
# -----------------------
def encode_xor(payload: str, key: int = 5) -> str:
    encoded_chars = []
    for char in payload:
        encoded_chars.append(chr(ord(char) ^ key))
    return "".join(encoded_chars)


# -----------------------
# ROT13 Encoding
# -----------------------
def encode_rot13(payload: str) -> str:
    result = []
    for char in payload:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return "".join(result)


# Default encoder used by main.py
def encode_payload(payload: str) -> str:
    return encode_base64(payload)

