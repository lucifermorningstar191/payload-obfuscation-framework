def is_detected(payload):
    signatures = ["malware", "attack", "exploit"]

    for sig in signatures:
        if sig in payload.lower():
            return True


    return False

