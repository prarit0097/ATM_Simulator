# main.py
from atm import ATM
import os


def display_main_menu():
    print("\n🏧 Python ATM Simulator")
    print("1. Login")
    print("2. Exit")
    return input("Enter choice: ")


def display_account_menu(atm):
    print(f"\nWelcome, {atm.current_account.name}!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini Statement")
    print("5. Change PIN")
    print("6. Logout")
    return input("Choose operation: ")


def initialize_sample_account():
    if not os.path.exists("accounts.json"):
        from account import Account
        sample_acc = Account("123456", "Raj Sharma", "1234", 10000)
        return {"123456": sample_acc}
    return {}


def main():
    atm = ATM()

    # Create sample account if needed
    if not atm.accounts:
        atm.accounts = initialize_sample_account()
        atm.save_data()

    while True:
        choice = display_main_menu()

        if choice == "1":
            acc_no = input("Account Number: ")
            pin = input("PIN: ")

            if atm.login(acc_no, pin):
                while True:
                    option = display_account_menu(atm)

                    if option == "1":
                        print(f"\n💰 Balance: ₹{atm.current_account.balance}")
                    elif option == "2":
                        handle_deposit(atm)
                    elif option == "3":
                        handle_withdraw(atm)
                    elif option == "4":
                        print(atm.mini_statement())
                    elif option == "5":
                        new_pin = input("New PIN: ")
                        print(atm.current_account.update_pin(new_pin))
                    elif option == "6":
                        atm.save_data()
                        print("Logged out!")
                        break
                    else:
                        print("Invalid option!")
            else:
                print("❌ Invalid credentials")

        elif choice == "2":
            atm.save_data()
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


def handle_deposit(atm):
    try:
        amount = float(input("Deposit amount: ₹"))
        print(atm.deposit(amount))
    except ValueError:
        print("❌ Invalid amount!")


def handle_withdraw(atm):
    try:
        amount = float(input("Withdrawal amount: ₹"))
        print(atm.withdraw(amount))
    except ValueError as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()