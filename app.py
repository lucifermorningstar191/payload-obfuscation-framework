import streamlit as st
import base64

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key)) for c in data)

def rot13(data):
    result = ""
    for char in data:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

st.title("Payload Encoder & Obfuscation Tool")

payload = st.text_input("Enter Payload")

option = st.selectbox("Choose Method", ["Base64", "XOR", "ROT13"])

key = st.text_input("Enter XOR Key (only for XOR)", value="K")

if st.button("Encode"):
    if payload:
        if option == "Base64":
            result = base64.b64encode(payload.encode()).decode()
        elif option == "XOR":
            result = xor_encrypt(payload, key)
        elif option == "ROT13":
            result = rot13(payload)

        st.success("Result:")
        st.code(result)
    else:
        st.warning("Enter payload first")


