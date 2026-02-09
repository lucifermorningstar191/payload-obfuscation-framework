from evasion.signature_checker import is_detected
from evasion.encoder import encode_payload

with open("payloads/original_payload.txt") as f:
    payload = f.read().strip()

encoded_payload = encode_payload(payload)

print("Original Payload:", payload)
print("Detected:", is_detected(payload))

print("\nEncoded Payload:", encoded_payload)
print("Detected:", is_detected(encoded_payload))
