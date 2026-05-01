from login_logic import check_login
from get_account import get_account_number_by_name
from register_user import register_user
from banking import customer

while True:

    print("\n=== BANK SYSTEM ===")

    print("L - Login")
    print("R - Register")
    print("E - Exit")

    main_choice = input("Enter choice: ").strip().upper()


    if main_choice == "L":

        print("\n=== BANK LOGIN ===")

        username = input("Enter username: ").strip()

        user_record = check_login(username)

        # USER NOT FOUND
        if user_record is None:

            print("\n=== USER NOT FOUND ===")
            print("User not found.")
            print("Please register first.")

            continue

        # PASSWORD SECTION
        print("\n=== PASSWORD VERIFICATION ===")

        password = input("Enter password: ").strip()

        stored_password = user_record[0]

        if password == stored_password:

            print("\n=== LOGIN SUCCESSFUL ===")

            try:

                print("\n=== ACCOUNT ACCESS ===")

                acc_no = get_account_number_by_name(username)

                if acc_no is None:

                   print("\n=== ACCOUNT NOT FOUND ===")

                   continue

                print("Account Number:", acc_no)

                C1 = customer(acc_no)

            except ValueError:

                print("\n=== INVALID INPUT ===")
                print("Invalid account number")

                continue

            C1 = customer(acc_no)

           
            while True:

                print("\n=== BANK MENU ===")

                print("D - Deposit")
                print("W - Withdraw")
                print("S - Show Account Info")
                print("E - Exit")

                menu_choice = input(
                    "Enter choice: "
                ).strip().upper()

                if menu_choice == "D":

                    print("\n=== DEPOSIT OPERATION ===")

                    try:

                        amount = float(
                            input(
                                "Enter amount to deposit: "
                            )
                        )

                        C1.deposit(amount)

                    except ValueError:

                        print("\n=== INVALID INPUT ===")
                        print("Invalid amount")

                elif menu_choice == "W":

                    print("\n=== WITHDRAW OPERATION ===")

                    try:

                        amount = float(
                            input(
                                "Enter amount to withdraw: "
                            )
                        )

                        C1.withdraw(amount)

                    except ValueError:

                        print("\n=== INVALID INPUT ===")
                        print("Invalid amount")

                elif menu_choice == "S":

                    print("\n=== ACCOUNT INFORMATION ===")

                    C1.display()

                elif menu_choice == "E":

                    print("\n=== EXITING ACCOUNT ===")

                    C1.close_connection()

                    print("Thank you for banking with us!")

                    break

                else:

                    print("\n=== INVALID CHOICE ===")

        else:

            print("\n=== LOGIN FAILED ===")
            print("Incorrect password")

    
    elif main_choice == "R":

        register_user()

    
    elif main_choice == "E":

        print("\n=== EXIT ===")

        print("Goodbye")

        break

    else:

        print("\n=== INVALID CHOICE ===")

# 863898