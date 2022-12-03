import getpass
import users
import sys
import encryption
import googleDriveAPI

u= users
e= encryption
g= googleDriveAPI

def privilegeMenu():
    try:
        while True:
            
            user_In = input("|U - Upload file | D - Download file | S - User settings | L - Log out | E - Exit|\n").lower()
            if(user_In == "s"):
                while True:
                    
                    user_In = input("|A - Add User | D - Delete User | N - Generate New Key | E - Exit to menu|\n").lower()
                    if (user_In == "a"):
                        createLogin = input("Create login name: ")
                        createPassword = getpass.getpass("Create password: ")
                        u.newUser(createLogin,createPassword)
                        
                    elif(user_In == "d"):
                        userName = input("\nEnter username you wish to delete: ")
                        u.deleteUser(userName)
                        
                    elif(user_In == "N"):
                        e.keyGen()
                        break
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")

            elif(user_In == "u"):
                while True:
                   
                    print("\nEnsure that files you wish to upload are in the 'Files' folder.\nEnter m to return to main menu.\n")
                    user_In = input("Enter file name: ")
                    if(user_In == "m"):
                        break
                    else:
                       e.encrypt(user_In, e.keyRead())
                       g.uploadFile(user_In)

            elif(user_In == "e"):
                print("Exiting.")
                sys.exit()

            elif(user_In == "l"):
                
                u.privilege = False
                print("Logging out.")
                break

            elif(user_In == "d"):
               
                while True:
                    user_In = input("\n|S - Search for file | D - Download File | E - Exit to menu|\n").lower()
                    if(user_In == "s"):
                      
                        user_In = input("Enter file name: ")
                        g.searchFile(user_In)
                    elif(user_In == "d"):
                       
                        user_In = input("Enter file name: ")
                        fileID= g.fileID(user_In)
                        g.downloadFile(fileID, user_In)
                        e.decrypt(user_In, e.keyRead())
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")
            else:
                 print("Wrong input try again\n")
               
               

    except Exception:
        pass


def standardMenu():
    try:
        while True:
            
            user_In = input("|U - Upload file | D - Download file | L - Log Out | E - Exit|\n").lower()
            if(user_In == "u"):
                while True:
                    print("\nEnsure that files you wish to upload are in the 'Files' folder.\nEnter m to return to main menu.\n")
                    user_In = input("Enter file name: ")
                    if(user_In == "m"):
                        break
                    else:
                       e.encrypt(user_In, e.keyRead())
                       g.uploadFile(user_In)

            elif(user_In == "e"):
                print("Exiting.")
                sys.exit()

            elif(user_In == "l"):
                print("Logging out.")
                break

            elif(user_In == "d"):
                while True:
                    user_In = input("\n|S - Search for file | D - Download File | E - Exit to menu|\n").lower()
                    if(user_In == "s"):
                        user_In = input("Enter file name: ")
                        g.searchFile(user_In)
                    elif(user_In == "d"):
                        user_In = input("Enter file name: ")
                        fileID= g.fileID(user_In)
                        g.downloadFile(fileID, user_In)
                        e.decrypt(user_In, e.keyRead())
                    elif(user_In == "e"):
                        break
                    else:
                        print("Wrong input try again\n")
            else:
                 print("Wrong input try again\n")
               
               

    except Exception:
        pass