import random
import string

def generate_password(length):
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits 
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)
length = int(input("Enter password length (minimum 8): "))
while True:
    try:
        if length < 8:
            print("Password should be at least 8 characters long.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (y/n): ").lower()

        if again != "y":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.") 