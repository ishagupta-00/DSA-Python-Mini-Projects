import json
import os
from datetime import datetime

DATA_FILE = "atm_data.json"


# -------------------- FILE HANDLING --------------------

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    return {
        "account_holder": "",
        "account_number": "",
        "pin": "",
        "balance": 0,
        "transactions": []
    }


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# -------------------- ACCOUNT SETUP --------------------

def create_account(data):
    print("\n========== ATM ACCOUNT SETUP ==========")

    name = input("Enter account holder name: ").strip()

    while True:
        pin = input("Create a 4-digit PIN: ")

        if pin.isdigit() and len(pin) == 4:
            confirm_pin = input("Confirm your PIN: ")

            if pin == confirm_pin:
                break
            else:
                print("PINs do not match. Try again.")
        else:
            print("PIN must contain exactly 4 digits.")

    while True:
        initial_deposit = input("Enter initial deposit amount: ")

        try:
            initial_deposit = float(initial_deposit)

            if initial_deposit >= 0:
                break
            else:
                print("Amount cannot be negative.")

        except ValueError:
            print("Please enter a valid amount.")

    account_number = "ATM" + str(datetime.now().timestamp()).replace(".", "")[-8:]

    data["account_holder"] = name
    data["account_number"] = account_number
    data["pin"] = pin
    data["balance"] = initial_deposit

    if initial_deposit > 0:
        data["transactions"].append({
            "type": "Initial Deposit",
            "amount": initial_deposit,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

    save_data(data)

    print("\nAccount created successfully!")
    print("Account Number:", account_number)


# -------------------- LOGIN --------------------

def login(data):
    print("\n========== ATM LOGIN ==========")

    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")

        if entered_pin == data["pin"]:
            print("\nLogin successful!")
            print("Welcome,", data["account_holder"])
            return True

        attempts -= 1

        if attempts > 0:
            print("Incorrect PIN.")
            print("Attempts remaining:", attempts)

    print("\nToo many incorrect attempts.")
    print("ATM access has been blocked for this session.")

    return False


# -------------------- CHECK BALANCE --------------------

def check_balance(data):
    print("\n========== BALANCE ==========")
    print("Available Balance: Rs.", format(data["balance"], ".2f"))


# -------------------- DEPOSIT --------------------

def deposit_money(data):
    print("\n========== DEPOSIT ==========")

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount.")
            return

        data["balance"] += amount

        data["transactions"].append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        save_data(data)

        print("Amount deposited successfully.")
        print("Updated Balance: Rs.", format(data["balance"], ".2f"))

    except ValueError:
        print("Please enter a valid amount.")


# -------------------- WITHDRAW --------------------

def withdraw_money(data):
    print("\n========== WITHDRAW ==========")

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount.")

        elif amount > data["balance"]:
            print("Insufficient balance.")

        else:
            data["balance"] -= amount

            data["transactions"].append({
                "type": "Withdrawal",
                "amount": amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            })

            save_data(data)

            print("Please collect your cash.")
            print("Remaining Balance: Rs.",
                  format(data["balance"], ".2f"))

    except ValueError:
        print("Please enter a valid amount.")


# -------------------- MINI STATEMENT --------------------

def mini_statement(data):
    print("\n========== MINI STATEMENT ==========")

    if len(data["transactions"]) == 0:
        print("No transactions available.")
        return

    for transaction in data["transactions"][-5:]:
        print(
            transaction["date"],
            "|",
            transaction["type"],
            "| Rs.",
            format(transaction["amount"], ".2f")
        )

    print("------------------------------------")
    print("Current Balance: Rs.",
          format(data["balance"], ".2f"))


# -------------------- LAST TRANSACTION --------------------

def last_transaction(data):
    print("\n========== LAST TRANSACTION ==========")

    if len(data["transactions"]) == 0:
        print("No transactions found.")
        return

    transaction = data["transactions"][-1]

    print("Type:", transaction["type"])
    print("Amount: Rs.", format(transaction["amount"], ".2f"))
    print("Date:", transaction["date"])


# -------------------- CHANGE PIN --------------------

def change_pin(data):
    print("\n========== CHANGE PIN ==========")

    current_pin = input("Enter current PIN: ")

    if current_pin != data["pin"]:
        print("Incorrect current PIN.")
        return

    while True:
        new_pin = input("Enter new 4-digit PIN: ")

        if not new_pin.isdigit() or len(new_pin) != 4:
            print("PIN must contain exactly 4 digits.")
            continue

        confirm_pin = input("Confirm new PIN: ")

        if new_pin != confirm_pin:
            print("PINs do not match.")
            continue

        data["pin"] = new_pin
        save_data(data)

        print("PIN changed successfully.")
        break


# -------------------- ACCOUNT DETAILS --------------------

def account_details(data):
    print("\n========== ACCOUNT DETAILS ==========")

    print("Account Holder:", data["account_holder"])
    print("Account Number:", data["account_number"])
    print("Balance: Rs.", format(data["balance"], ".2f"))


# -------------------- ATM MENU --------------------

def atm_menu(data):

    while True:

        print("\n================================")
        print("          ATM MAIN MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Last Transaction")
        print("6. Change PIN")
        print("7. Account Details")
        print("8. Logout")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(data)

        elif choice == "2":
            deposit_money(data)

        elif choice == "3":
            withdraw_money(data)

        elif choice == "4":
            mini_statement(data)

        elif choice == "5":
            last_transaction(data)

        elif choice == "6":
            change_pin(data)

        elif choice == "7":
            account_details(data)

        elif choice == "8":
            print("\nYou have been logged out.")
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")


# -------------------- MAIN PROGRAM --------------------

def main():

    data = load_data()

    if data["pin"] == "":
        create_account(data)

    if login(data):
        atm_menu(data)


main()