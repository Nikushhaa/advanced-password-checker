import string
import random

def check_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 25
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Digit
    if any(char.isdigit() for char in password):
        score += 25
    else:
        feedback.append("Add at least one number.")

    # Uppercase
    if any(char.isupper() for char in password):
        score += 25
    else:
        feedback.append("Add at least one uppercase letter.")

    # Special character
    if any(char in string.punctuation for char in password):
        score += 25
    else:
        feedback.append("Add at least one special character (!@#$...).")

    return score, feedback


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


print("=== Advanced Password Tool ===")

while True:
    print("\n1 - Check Password")
    print("2 - Generate Strong Password")
    print("3 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        password = input("Enter your password: ")
        score, feedback = check_password(password)

        print(f"\nStrength Score: {score}/100")

        if score == 100:
            print("Strong Password 💪")
        elif score >= 75:
            print("Good Password 👍")
        elif score >= 50:
            print("Medium Password ⚠️")
        else:
            print("Weak Password ❌")

        if feedback:
            print("\nSuggestions:")
            for tip in feedback:
                print("-", tip)

    elif choice == "2":
        strong_pass = generate_password()
        print("\nGenerated Password:", strong_pass)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option.")
