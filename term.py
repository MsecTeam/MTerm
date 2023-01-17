import sys
import os
import time
import socket
os.system("clear")
print("\033[1;33m")
print(" /$$      /$$                                     /$$$$$$$$                  /$$           ")
print(" | $$$    /$$$                                    |__  $$__/                 | $$          ")
print(" | $$$$  /$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$")
print(" | $$ $$/$$ $$ /$$_____/ /$$__  $$ /$$_____/         | $$ /$$__  $$ /$$__  $$| $$ /$$_____/")
print(" | $$  $$$| $$|  $$$$$$ | $$$$$$$$| $$               | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$ ")
print(" | $$\  $ | $$ \____  $$| $$_____/| $$               | $$| $$  | $$| $$  | $$| $$ \____  $$")
print(" | $$ \/  | $$ /$$$$$$$/|  $$$$$$$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/")
print(" |__/     |__/|_______/  \_______/ \_______/         |__/ \______/  \______/ |__/|_______/ ")
print("Create By  RedSec")
print("Msec Tools")
print("")
while True:
    # Dapatkan pilihan dari pengguna
    pilihan = input("Msec@root~# ")

    # Eksekusi perintah sesuai dengan pilihan
    if pilihan == "help":
        print("===========")
        print("Menu:")
        print("===========")
        print("clear : Clear Program")
        print("install : Install Package")
        print("cd : Enter Repository")
        print("ls : Show Repository")
        print("python3 : Run Python3")
        print("git : Cloning Repository")
        print("rm : Remove Repository")
        print("exit : Exit The Program")
        print("chmod : Give Repository Permissions")
    elif pilihan == "chmod":
        chmod = input("Enter Repository Name => ")
        os.system(f"chmod +x {chmod}")
    elif pilihan == "rm":
        rm = input("Enter the name of the repository that you want to delete => ")
        os.system(f"rm -R {rm}")
    elif pilihan == "install":
        install = input ("Package name that you want to install => ")
        os.system(f"sudo apt install {install}")
    elif pilihan == "cd":
        cd = input ("Enter Repository Name => ")
        os.system(f"cd {cd}")
    elif pilihan == "ls":
        os.system("ls")
    elif pilihan == "python3":
        python3 = input("Enter Repository Name => ")
        os.system(f"python3 {python3}")
    elif pilihan == "git":
        git = input ("Enter the name of the repository that you want to clone => ")
        os.system(f"git clone {git}")
    elif pilihan == "clear":
        print("\033[1;33m")
        os.system("clear")
        print(" /$$      /$$                                     /$$$$$$$$                  /$$           ")
        print(" | $$$    /$$$                                    |__  $$__/                 | $$          ")
        print(" | $$$$  /$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$")
        print(" | $$ $$/$$ $$ /$$_____/ /$$__  $$ /$$_____/         | $$ /$$__  $$ /$$__  $$| $$ /$$_____/")
        print(" | $$  $$$| $$|  $$$$$$ | $$$$$$$$| $$               | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$ ")
        print(" | $$\  $ | $$ \____  $$| $$_____/| $$               | $$| $$  | $$| $$  | $$| $$ \____  $$")
        print(" | $$ \/  | $$ /$$$$$$$/|  $$$$$$$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/")
        print(" |__/     |__/|_______/  \_______/ \_______/         |__/ \______/  \______/ |__/|_______/ ")
        print("Create By  RedSec")
        print("Msec Tools")
        print("")
    elif pilihan == "exit":
        break
    else:
        print("Menu tidak valid.")
