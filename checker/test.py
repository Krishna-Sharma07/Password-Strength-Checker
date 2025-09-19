from checker import check_password_strength, generate_password

def test_strength_checker():
    passwords = [
        "abc",
        "abcdefghi",
        "Password",
        "Password123",
        "Password123!",
        "Very$trongPass123!"
    ]

    for pw in passwords:
        result = check_password_strength(pw)
        print(f"\nPassword: {pw}")
        print("Strength:", result["strength"], f"(Level {result['level']})")
        print("Rules:")
        for rule, passed in result["rules"].items():
            print(f"  {rule}: {'✅' if passed else '❌'}")


def test_password_generator():
    for length in [8, 12, 16]:
        pw = generate_password(length)
        result = check_password_strength(pw)
        print(f"\nGenerated ({length} chars): {pw}")
        print("Strength:", result["strength"], f"(Level {result['level']})")


if __name__ == "__main__":
    test_strength_checker()
    test_password_generator()
