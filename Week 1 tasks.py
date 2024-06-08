import argparse
import secrets
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument(
        "-l", "--length", type=int, default=12,
        help="Length of the password (default: 12)"
    )
    parser.add_argument(
        "-u", "--uppercase", action="store_true",
        help="Include uppercase letters"
    )
    parser.add_argument(
        "-d", "--digits", action="store_true",
        help="Include digits"
    )
    parser.add_argument(
        "-s", "--special", action="store_true",
        help="Include special characters"
    )

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_uppercase=args.uppercase,
        use_digits=args.digits,
        use_special=args.special
    )

    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
