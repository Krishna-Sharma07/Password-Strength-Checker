import re
import random
import string

def check_password_strength(password: str) -> dict:

    rules = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "symbol": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }

    score = sum(rules.values())

    if len(password) < 8 or score <= 2:
        strength = "Weak"
        level = 1
    elif score == 3:
        strength = "Medium"
        level = 2
    elif score == 4 and len(password) >= 10:
        strength = "Strong"
        level = 3
    elif score == 5 and len(password) >= 12:
        strength = "Very Strong"
        level = 4
    else:
        strength = "Medium"
        level = 2

    return {
        "rules": rules,
        "strength": strength,
        "level": level
    }

def generate_password(length: int = 12) -> str:

    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += [random.choice(characters) for _ in range(length - 4)]

    random.shuffle(password)

    return "".join(password)