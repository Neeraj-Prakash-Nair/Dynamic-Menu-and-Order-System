from Adminfunction import  Administrator
from Cashierfunction import NomNomNation
import pickle
import colorama
from colorama import Fore
from colorama import Style
from colorama import Back
colorama.init()

def login():
    print("Select Role:")
    print(Fore.CYAN + "1. Cashier " + Style.RESET_ALL)
    print(Fore.RED + "2. Admin " + Style.RESET_ALL)
    
    role_choice = input("Enter your choice (1 or 2): ")
    
    
    if role_choice == "1":
        f1=open("usercredentials.dat","rb")
        
        while True:

            u_username = input(Fore.GREEN + "Username " + Style.RESET_ALL)
            u_password = input(Fore.MAGENTA + "Password " + Style.RESET_ALL)
            d=pickle.load(f1)
            
            for i in d:
                
                if u_username in d and d[u_username] == u_password:
                    print(Fore.GREEN + "You've logged in successfully!" + Style.RESET_ALL)
                    NomNomNation()
                    return
                else:
                    print(Fore.RED + "Please check the credentials entered" + Style.RESET_ALL)
        f1.close()
        return
        
    elif role_choice == "2":
        
        f2=open("admincredentials.dat","rb")
        
        while True:

            a_username = input(Fore.GREEN + "Username " + Style.RESET_ALL)
            a_password = input(Fore.MAGENTA + "Password " + Style.RESET_ALL)
            k=pickle.load(f2)
            for i in k:
                
                if a_username in k and k[a_username] == a_password:
                    print(Fore.GREEN + "You've logged in successfully!" + Style.RESET_ALL)
                    Administrator()
                    return
                else:
                    print(Fore.RED + "Please check the credentials entered" + Style.RESET_ALL)
        f2.close()
        return
        
    else:
        print(Fore.RED + "Invalid Choice" + Style.RESET_ALL)
        

login()
