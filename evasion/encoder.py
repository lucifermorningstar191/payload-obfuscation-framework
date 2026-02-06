from evasion.encoder import encode_payload

from evasion.signature_checker import is_detected
from evasion.encoder import encode_payload

with open("payloads/original_payload.txt", "r") as f:
    payload = f.read()

print("Original Payload:", payload)
print("Detected:", is_detected(payload))

encoded_payload = encode_payload(payload)

print("\nEncoded Payload:", encoded_payload)
print("Detected after encoding:", is_detected(encoded_payload))
