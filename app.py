import streamlit as st
import base64

st.title("Payload Encoder & Obfuscation Tool")

payload = st.text_input("Enter Payload")

option = st.selectbox("Choose Encoding Method", ["Base64"])

if st.button("Encode"):
    if payload:
        encoded = base64.b64encode(payload.encode()).decode()
        st.success("Encoded Payload:")
        st.code(encoded)
    else:
        st.warning("Please enter a payload")
