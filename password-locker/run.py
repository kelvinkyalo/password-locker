#!/usr/bin/env python3.6
from user import User
from accounts import Account


def create_new_account(account_name, account_password):
    '''
    Function to create a new account
    '''
    new_account = Account(account_name, account_password)
    return new_account


def save_new_account(accounts):
    '''
    Function to save account
    '''
    accounts.save_accounts()


def delete_account(accounts):
    '''
    Function to delete accounts
    '''
    return Account.delete_accounts(accounts)


def find_account(account_name):
    '''
    Function that finds a accounts by name and returns the account
    '''
    return Account.find_by_name(account_name)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()


def main():

    print('\n')

    while True:
        print("Hello welcome to password-locker")
        print('\n')
        print('''use these short codes to navigate; \n 'nu'- add new user \n 'lg'- login to your account''')
        short_code = input().lower()
        print('\n')

        if short_code == 'cc':
            print("create username...")
            created_user_name = input()

            print("create password ....")
            created_user_password = input()

            print("confirm password ...")
            confirm_password = input()
            print('\n')

            while confirm_password != created_user_password:
                print("invalid Password ....")
                print('Enter user name ...')
                created_user_password = input()
                print('confirn password ....')
                confirm_password = input()
                print('\n')
            else:
                print(
                    f"Hello{created_user_name} You have successfully created your account.")
                print('\n')
                print('you can now login ..')
                print('\n')
                print('Username...')
                entered_username = input()
                print("Your password....")
                entered_password = input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print('\n')
                print("Invalid username or password")
                print("Username....")
                entered_username = input()
                print("Your password....")
                entered_password = input()
                print('\n')

            else:
                print('\n')
                print(
                    f" Welcome {entered_username} to your account...")
                print('\n')

                print("Select an option to continue: \n Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1:view your saved accounts")
                print("2:Add new accounts")
                print("3:Remove account")
                print("4:search new account")
                print("5:log out")
                option = input()

                if option == '2':
                    while True:
                        print(" Do you wish to continue? Y/N...")

                        choice = input().lower()
                        if choice == 'y':
                            print("Enter account name....")
                            account_name = input()
                            print('\n')
                            print(
                                "I can create a password for if you type in - 'rp' \n** Or create your own password with - 'cp'")
                            keyword = input().lower()

                            # Generates the random digit number
                            if keyword == 'rp':
                                account_password = random.randint(11111, 111111)
                                print('\n')
                                print('Automatically generated this for you')
                                print(f"  Account: {account_name}....")
                                print(f" Password: {account_password}...")
                                print('\n')

                            elif keyword == 'cp':
                                print("Create your own password password")
                                account_password = input()
                                print(f" Account: {account_name}....")
                                print(f" Password: {account_password}....")
                                print('\n')

                            else:
                                print(" Enter a valid code....")

                            # elif save_new_credential(create_new_credential(
                            #     account_name, account_password))

                        elif choice == 'cp':
                            break
                        else:
                            print("use 'y' for yes and 'n' for no")

                elif option == '1':
                    while True:
                        print("This is a list of your accounts....")

                        if display_accounts():

                            for account in display_accounts():
                                print(
                                    f"Account Name:{account.account_name} ")
                                print(
                                    f"Password:{account.account_password} ")

                        else:

                            print('\n')
                            print("No  account credentials available....")
                            print('\n')

                        print("Back to menu? y/n")

                        back = input().lower()

                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("invalid option...")
                            continue

                elif option == '5':
                    print(
                        "WARNING all your details will be lost. \n Proceed? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print(" You have logged out successfully ")
                        print('\n')
                        break
                    elif logout == 'n':
                        continue

                elif option == '3':
                    while True:
                        print("search for accounts to delete")

                        search_name = input()

                        # if check_existing_credentials(search_name):
                        search_account = find_account(search_name)
                        print(
                            f"Account Name: {search_account.account_name}\n Password: {search_account.account_password}")
                        print("Delete? y/n")

                        confirm = input().lower()
                        if confirm == 'y':
                            delete_account(search_account)
                            print("Account successfully removed ")
                            break
                        elif confirm == 'n':
                            continue

                    else:
                        print("Account does not exist ")
                        break

                elif option == '4':
                    while True:
                        print("continue? y/n")
                        choice = input().lower()
                        if choice == 'y':
                            print("Enter account name to find accounts...")

                            search_name = input()

                            # if check_existing_accounts(search_name):
                            search_account = find_account(search_name)
                            print(
                                f"Account Name: {search_account.account_name}\n Password: {search_account.account_password}")
                            # else:
                            print("Sorry this account does not exist....")

                        elif choice == 'n':
                            break
                        else:
                            print("Invalid code....")

                    print(" Invalid code....")
                    continue

                elif short_code == 'ex':
                    break
            else:
                print("Enter valid code to continue")

        elif short_code == 'lg':
            print("welcome ")
            print(" Enter user name....")
            created_user_name = input()

            print("Enter user name ....")
            created_user_name = input()
            print('\n')


if __name__ == '__main__':
    main()
