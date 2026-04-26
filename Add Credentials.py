import pickle
import colorama
from colorama import Fore
from colorama import Style
from colorama import Back
colorama.init()

print("Would you like to create the account for the Cashier or the Adminstrator?")
print(Fore.CYAN + "1. Cashier" + Style.RESET_ALL)
print(Fore.RED + "2. Administrator" + Style.RESET_ALL)
c=int(input("Enter your choice "))

if c==1:
    def save_usercredentials(usercredentialsfile):
        print("Welcome to the Credentials Writer!")
        # Initialize an empty dictionary
        ucredentials = {}

        while True:
            # Get username and password
            username = input("Enter a username: ")
            password = input("Enter a password: ")

            # Add username and password to the dictionary
            ucredentials[username] = password
            print(f"Added {username} to the credentials list!")

            # Ask user if they want to add more credentials
            choice = input("Do you want to add another credential for a cashier? (yes/no): ").strip().lower()
            if choice != "yes":
                break

        # Save the credentials to the binary file
        try:
            with open(usercredentialsfile, "wb") as f:
                pickle.dump(ucredentials, f)
            print(f"Credentials saved to {usercredentialsfile} successfully!")
        except Exception as e:
            print(f"An error occurred while saving the file: {e.__class__.__name__}: {e}")

    # Call the function with a valid file name
    save_usercredentials("usercredentials.dat")

elif c==2:
    def save_admincredentials(admincredentialsfile):
        print("Welcome to the Credentials Writer!")
        # Initialize an empty dictionary
        acredentials = {}

        while True:
            # Get username and password
            username = input("Enter a username: ")
            password = input("Enter a password: ")

            # Add username and password to the dictionary
            acredentials[username] = password
            print(f"Added {username} to the credentials list!")

            # Ask user if they want to add more credentials
            choice = input("Do you want to add another credential for an administrator? (yes/no): ").strip().lower()
            if choice != "yes":
                break

        # Save the credentials to the binary file
        try:
            with open(admincredentialsfile, "wb") as f:
                pickle.dump(acredentials, f)
            print(f"Credentials saved to {admincredentialsfile} successfully!")
        except Exception as e:
            print(f"An error occurred while saving the file: {e.__class__.__name__}: {e}")

    # Call the function with a valid file name
    save_admincredentials("admincredentials.dat")

