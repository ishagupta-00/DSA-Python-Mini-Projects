# -------------------- LOGIN SYSTEM --------------------

def create_user():
    print("\n========== CREATE ACCOUNT ==========")

    username = input("Create username: ").strip()

    while username == "":
        print("Username cannot be empty.")
        username = input("Create username: ").strip()

    while True:
        password = input("Create password: ")

        if len(password) < 4:
            print("Password must contain at least 4 characters.")
        else:
            break

    print("\nAccount created successfully!")
    return {
        "username": username,
        "password": password
    }


def login(user):
    print("\n========== LOGIN ==========")

    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == user["username"] and password == user["password"]:
            print("\nLogin successful!")
            print("Welcome,", user["username"])
            return True

        attempts -= 1

        if attempts > 0:
            print("\nInvalid username or password.")
            print("Attempts remaining:", attempts)

    print("\nToo many failed attempts.")
    print("Login access blocked for this session.")

    return False


def main():
    user = create_user()

    print("\nYour account is ready. Please login.")

    if login(user):
        print("\nYou are now logged into the system.")
    else:
        print("\nPlease try again later.")


main()