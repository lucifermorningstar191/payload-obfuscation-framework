import random
import string


def random_insert_obfuscation(payload: str) -> str:
    """
    Inserts random characters between payload characters.
    This simulates basic obfuscation used to break signatures.
    """
    obfuscated = ""

    for char in payload:
        obfuscated += char
        obfuscated += random.choice(string.ascii_letters)

    return obfuscated


def split_and_join_obfuscation(payload: str) -> str:
    """
    Splits string and joins using a separator.
    """
    return "_".join(payload)
