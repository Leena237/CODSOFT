import random
import string

def creating_password(leng):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(leng))
    return password

def main():
    try:
        leng = int(input("Enter the length of the password: "))
        if leng <= 0:
            print("Please enter a valid positive length.")
            return

        password = creating_password(leng)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid Input!! Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
