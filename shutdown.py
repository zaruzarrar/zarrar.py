import os

confirm = input("Do you really want to shut down the system? (yes/no): ")

if confirm.lower() == "yes":

 os.system("shutdown /s /t 0")
else:

 print("Shutdown cancelled.")