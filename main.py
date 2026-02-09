from evasion.signature_checker import is_detected
from evasion.encoder import encode_payload
from evasion.obfuscator import random_insert_obfuscation

with open("payloads/original_payload.txt") as f:
    payload = f.read().strip()

encoded_payload = encode_payload(payload)

print("Original Payload:", payload)
print("Detected:", is_detected(payload))


print("\nEncoded Payload:", encoded_payload)
print("Detected:", is_detected(encoded_payload))

obfuscated_payload = random_insert_obfuscation(encoded_payload)

print("\nObfuscated Payload:", obfuscated_payload)
print("Detected after obfuscation:", is_detected(obfuscated_payload))
