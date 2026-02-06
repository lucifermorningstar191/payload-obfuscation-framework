from evasion.signature_checker import is_detected

with open("payloads/original_payload.txt") as f:
    payload = f.read().strip()

print("Payload:", payload)
print("Detected:", is_detected(payload))

