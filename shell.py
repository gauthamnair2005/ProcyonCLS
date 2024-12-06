import kernel
import sys
import os
import pyfiglet
import time
import getpass
import ekernel
import sqlite3
import updater
import requests

def initialize_db():
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL,
                        first_name TEXT,
                        last_name TEXT,
                        age INTEGER,
                        other_details TEXT)''')
    conn.commit()
    conn.close()

def updateCheckOnStart():
    newtag = updater.getLatestReleaseTag()
    currenttag = updater.readCurrentTag()
    if newtag[0] > currenttag:
        kernel.printWarning(f"Update to version {newtag[0]} is available!")
        kernel.printInfo("Run 'clsupdate' to see what's new and update")
        time.sleep(2)
    return None

def fetchMOTD():
    try:
        url = "https://raw.githubusercontent.com/gauthamnair2005/ProcyonCLS-MOTD/main/motd.txt"
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except:
        return None

def add_user(username, password, first_name, last_name, age, other_details):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, first_name, last_name, age, other_details) VALUES (?, ?, ?, ?, ?, ?)', 
                   (username, password, first_name, last_name, age, other_details))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_name(username):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute('SELECT first_name FROM users WHERE username = ?', (username,))
    name = cursor.fetchone()[0]
    conn.close()
    return name

def update_user(username, field, value):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET {field} = ? WHERE username = ?', (value, username))
    conn.commit()
    conn.close()

def delete_user(username):
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

def oobe():
    print("\033[0;35m" + pyfiglet.figlet_format("Welcome to ProcyonCLS 2025") + "\033[0m")
    time.sleep(2)
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    time.sleep(1)
    print()
    kernel.printInfo("ProcyonCLS got better")
    kernel.printInfo("-------------------------")
    time.sleep(1)
    kernel.println("  With ProcyonCLS 2025, you get a rich and secure experience")
    kernel.println("along with the new AppMarket, ChatCLS, NetGet and more!")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()    
    kernel.printInfo("ProcyonCLS 2025 : Security at it's peak")
    kernel.printInfo("--------------------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with enhanced security features")
    kernel.println("to protect your data and privacy. Like updates, ")
    kernel.println("password reset, secure account verification and" )
    kernel.println("system repair.!")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : AppMarket")
    kernel.printInfo("----------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with AppMarket, a place to")
    kernel.println("download and install applications. You can also")
    kernel.println("create your own applications and share them with")
    kernel.println("the community.")
    kernel.printWarning("Note : AppMarket is under development and not functional")
    kernel.printWarning("in this build. To publish your application, pull")
    kernel.printWarning("request on GitHub.")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : ChatCLS")
    kernel.printInfo("----------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with ChatCLS, an AI powered")
    kernel.println("chat application. ChatCLS can help you with your")
    kernel.println("queries, provide information and much more.")
    kernel.printWarning("Note: ChatCLS is still in beta, and requires")
    kernel.printWarning("OpenAI API key.")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : NetGet")
    kernel.printInfo("----------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with NetGet, a download")
    kernel.println("manager to download files from the internet.")
    kernel.printWarning("Note: NetGet is still in beta,")
    kernel.printWarning("and may not work properly.")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : Evaluator")
    kernel.printInfo("----------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with Evaluator, a calculator")
    kernel.println("application to perform mathematical operations.")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : HTML Viewer")
    kernel.printInfo("----------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with HTML Viewer, a browser")
    kernel.println("application to view HTML files.")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : Notes")
    kernel.printInfo("----------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with Notes, a note taking")
    kernel.println("application to write and save notes.")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : Security")
    kernel.printInfo("----------------------------------")
    time.sleep(1)
    kernel.println("  ProcyonCLS 2025 comes with enhanced security features")
    kernel.println("to protect your data and privacy. Like updates, ")
    kernel.println("password reset, secure account verification and" )
    kernel.println("system repair.!")
    time.sleep(2)
    print()
    input("Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo("ProcyonCLS 2025 : Let's Get Started")
    kernel.printInfo("--------------------------------------------")
    time.sleep(1)
    print("Checking for updates...", end = " ", flush = True)
    time.sleep(1)
    if updater.getLatestReleaseTagOnly() > updater.readCurrentTag():
        kernel.printWarning("[Outdated]")
        print("Update available, do you want to update? (y/n) : ", end = "", flush = True)
        confirm = input().strip()
        if confirm.lower() == "y":
            os.execv(sys.executable, ['python3', 'updater.py', '1.5.0'])
        else:
            kernel.printWarning("Not Updating")
    else:
        kernel.printSuccess("[Up to date]")
    time.sleep(2)
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print("\033[0;35m" + pyfiglet.figlet_format("Let's Get Started") + "\033[0m")
    time.sleep(2)
    kernel.clrscr()

def create_user_applet():
    ekernel.printHeader("ProcyonCLS 2025")
    kernel.printInfo("Create a new user")
    kernel.printInfo("-------------------------")
    username = input("Enter Username: ").strip()
    while True:
        if get_user(username):
            kernel.printWarning("Username already exists!")
            username = input("Enter Username: ").strip()
        else:
            break
    while True:
        password = getpass.getpass("Enter Password: ").strip()
        while True:
            if len(password) < 8:
                kernel.printWarning("Password must be at least 8 characters long!")
                password = getpass.getpass("Enter Password: ").strip()
            else:
                break
        confirm = getpass.getpass("Confirm Password: ").strip()
        if password == confirm:
            break
        else:
            kernel.printError("Passwords do not match!")
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    age = input("Enter Age: ").strip()
    age = int(age) if age.isdigit() else None
    other_details = input("Enter Other Details: ").strip()
    add_user(username, password, first_name, last_name, age, other_details)
    kernel.printSuccess("User Created Successfully!")
    kernel.printWarning("Hang tight..")
    time.sleep(2)
    prompt(first_name, username)

def prompt(user, username):
    kernel.clrscr()
    ekernel.prettyPrint(f"Welcome, {user}")
    time.sleep(2)
    kernel.clrscr()
    ekernel.printHeader("ProcyonCLS 2025")
    kernel.printInfo("Workspace")
    kernel.printInfo("-------------------------")
    updateCheckOnStart()
    print(fetchMOTD())
    kernel.printWarning("This is Developer Preview 8 build of ProcyonCLS 2025!")
    kernel.printInfo("● " + time.strftime("Date : %d/%m/%Y"))
    kernel.printInfo("● " + time.strftime("Time : %H:%M:%S"))
    while True:
        prmpt = input(f"\033[92m{username}\033[0m@\033[96mProcyonCLS\033[0m:~\033[93m$\033[0m ").strip()
        if prmpt == "exit" or prmpt == "shutdown":
            kernel.shutDown()
        elif prmpt == "reboot":
            kernel.reboot()
        elif prmpt == "oobe":
            oobe()
        elif prmpt == "netget":
            kernel.callApplication("netget", isAdmin=False)
        elif prmpt == "chatcls":
            kernel.callApplication("chatcls", isAdmin=False)
        elif prmpt.startswith("system "):
            os.system(prmpt[7:])
        elif prmpt == "delete":
            fileFolder = input("Enter file name to delete : ").strip()
            if os.path.exists(fileFolder):
                try:
                    os.remove(fileFolder)
                    kernel.printSuccess(f"{fileFolder} deleted successfully!")
                except Exception as e:
                    kernel.printError(f"Error deleting file: {e}")
            else:
                kernel.printError(f"{fileFolder} not found")
        elif prmpt.startswith("mkdir "):
            folder = prmpt[6:]
            if sys.platform == "win32" and folder.lower() in ["con", "prn", "aux", "nul"] + [f"com{i}" for i in range(1, 10)] + [f"lpt{i}" for i in range(1, 10)]:
                kernel.bsod("0x0007", "Attempted to create system file")
            else:
                try:
                    os.mkdir(folder)
                    kernel.printSuccess(f"{folder} created successfully!")
                except Exception as e:
                    kernel.printError(f"Error creating folder: {e}")
        elif prmpt == "mkdir":
            folder = input("Enter folder name : ").strip()
            if sys.platform == "win32" and folder.lower() in ["con", "prn", "aux", "nul"] + [f"com{i}" for i in range(1, 10)] + [f"lpt{i}" for i in range(1, 10)]:
                kernel.bsod("0x0007", "Attempted to create system file")
            else:
                try:
                    os.mkdir(folder)
                    kernel.printSuccess(f"{folder} created successfully!")
                except Exception as e:
                    kernel.printError(f"Error creating folder: {e}")
        elif prmpt == "notes":
            kernel.callApplication("notes", isAdmin=False)
        elif prmpt == "market" or prmpt == "appmarket" or prmpt == "appstore" or prmpt == "store":
            if ekernel.admin(username):
                kernel.callApplication("appmarket", isAdmin=True)
            else:
                kernel.printError("Admin access denied, market needs admin access to run!")
        elif prmpt == "python":
            os.system("python3")
        elif prmpt == "browser":
            kernel.callApplication("browser", isAdmin=False)
        elif prmpt == "clsupdate":
            confirm = input("Running updater will terminate current session. Do you want to continue (y/n) : ").strip()
            if confirm.lower() == "y":
                if ekernel.admin(username):
                    os.execv(sys.executable, ['python3', 'updater.py', '1.5.0'])
                else:
                    kernel.printError("Admin access denied, updater needs admin access to run!")
        elif prmpt == "security":
            if ekernel.admin(username):
                kernel.callApplication("security", isAdmin=True)
            else:
                kernel.printError("Admin access denied, security needs admin access to run!")
        elif prmpt in ["dir", "ls"]:
            kernel.printInfo(f"| {os.getcwd()}")
            for i in os.listdir():
                kernel.println("|--" + i)
        elif prmpt == "ver":
            ekernel.printHeader("Version Information")
            kernel.printInfo(f"| {kernel.getReleaseName()} {kernel.getRelease()}")
            kernel.println(f"|--OS Name : {kernel.getReleaseName()}")
            kernel.println(f"|--Version : {kernel.getVersion()}")
            kernel.println(f"|--Release : {kernel.getRelease()}")
        elif prmpt == "info":
            ekernel.printHeader("Software Information")
            kernel.printInfo(f"| {kernel.getReleaseName()} {kernel.getRelease()}")
            kernel.println(f"|--OS Name : {kernel.getReleaseName()}")
            kernel.println(f"|--Version : {kernel.getVersion()}")
            kernel.println(f"|--Codename : {kernel.getCodeName()}")
            kernel.println(f"|--Build : {kernel.getBuild()}")
            kernel.println(f"|--Author : {kernel.getAuthor()}")
            kernel.println(f"|--Company : {kernel.getCompany()}")
            kernel.println(f"|--License : {kernel.getLicense()}")
            kernel.println(f"|--Kernel : {kernel.getKernelName()} {kernel.getVersion()}")
            kernel.println(f"|--Release : {kernel.getRelease()}")
        elif prmpt in ["calc", "calculator", "eval", "evaluator"]:
            try:
                kernel.callApplication("evaluator", isAdmin=False)
            except:
                kernel.printError(f"Error running evaluator")
        elif prmpt == "date":
            kernel.println(time.strftime("%d/%m/%Y"))
        elif prmpt == "time":
            kernel.println(time.strftime("%H:%M:%S"))
        elif prmpt == "datetime":
            kernel.println(time.strftime("%d/%m/%Y %H:%M:%S"))
        elif prmpt in ["reset password", "reset-password"]:
            ekernel.printHeader("Reset Password")
            if ekernel.admin("Enter old password : "):
                password = getpass.getpass("Enter new password : ").strip()
                update_user(user, 'password', password)
                kernel.printSuccess("Password reset successfully!")
            else:
                kernel.printError("Admin access denied")
        elif prmpt == "update":
            kernel.printError("Usage: update <field> <value>")
        elif prmpt.startswith("update "):
            parts = prmpt.split()
            if len(parts) == 3:
                field, value = parts[1], parts[2]
                if field in ['username', 'first_name', 'last_name', 'age', 'other_details']:
                    update_user(user, field, value)
                    kernel.printSuccess(f"{field} updated successfully!")
                elif field == "password":
                    kernel.printError("Cannot update password here")
                    kernel.printWarning("Use 'reset password' to reset password")
                else:
                    kernel.printError("Invalid field")
            else:
                kernel.printError("Usage: update <field> <value>")
        elif prmpt == "create user":
            create_user_applet()
        elif prmpt == "help":
            ekernel.printHeader("Help")
            kernel.printInfo("| Available commands :")
            kernel.println("|--help - Display this help message")
            kernel.println("|--exit - Exit the shell")
            kernel.println("|--run <application> - Run a 3rd party application")
            kernel.println("|--admin <application> - Run a 3rd party application with admin prVileges")
            kernel.println("|--clrscr - Clear the screen")
            kernel.println("|--eval - Open the evaluator")
            kernel.println("|--date - Display the current date")
            kernel.println("|--time - Display the current time")
            kernel.println("|--datetime - Display the current date and time")
            kernel.println("|--reset password - Reset the user password")
            kernel.println("|--update <field> <value> - Update user details")
            kernel.println("|--create user - Create a new user")
            kernel.println("|--ver - Display OS version information")
            kernel.println("|--info - Display OS information")
            kernel.println("|--notes - Open the notes application")
            kernel.println("|--dir/ls - List files and folders in the current directory")
            kernel.println("|--mkdir - Create a new folder")
            kernel.println("|--security - Open the security application")
            kernel.println("|--delete - Delete a file")
            kernel.println("|--chatcls - Open the ChatCLS application")
            kernel.println("|--market - Open the AppMarket application")
            kernel.println("|--clsupdate - Update the OS")
            kernel.println("|--browser - Open the browser application")
            kernel.println("|--netget - Open the NetGet application")
            kernel.println("|--delete user - Delete the current user")
            kernel.println("|--reboot - Reboot the system")
            kernel.println("|--shutdown - Shutdown the system")
        elif prmpt.startswith("prettyprint "):
            ekernel.prettyPrint(prmpt[12:])
        elif prmpt.startswith("echo "):
            kernel.println(prmpt[5:])
        elif prmpt == "logout":
            break
        elif prmpt == "delete user":
            if ekernel.admin(username):
                delete_user(username)
                kernel.printSuccess("User deleted successfully!")
                break
            else:
                kernel.printError("Admin access denied")
        elif prmpt == "bsod":
            kernel.bsod("0x0004", "User invoked BSOD")
        elif prmpt.startswith("run "):
            if prmpt[4:] in ["bootload", "kernel", "shell", "ekernel"]:
                kernel.printError("Cannot run system files")
            else:
                try:
                    kernel.callApplication3P(prmpt[4:], isAdmin=False)
                except Exception as e:
                    kernel.printError(f"Error running 3rd party application: {e}")
        elif prmpt.startswith("admin "):
            if ekernel.admin(username):
                if prmpt[6:] in ["bootload", "kernel", "shell", "ekernel"]:
                    kernel.printError("Cannot run system files")
                else:
                    try:
                        kernel.callApplication3P(prmpt[6:], isAdmin=True)
                    except Exception as e:
                        kernel.printError(f"Error running 3rd party application: {e}")
            else:
                kernel.printError("Admin access denied")
        elif prmpt == "clrscr":
            kernel.clrscr()
        elif prmpt == "" or prmpt.isspace():
            continue
        else:
            kernel.printError("Command not found")

def main():
    initialize_db()
    if len(sys.argv) == 2:
        if sys.argv[1] == "1.5.0":
            os.system("cls" if sys.platform == "win32" else "clear")
            print(pyfiglet.figlet_format("ProcyonCLS", font="slant", justify="center"))
            print("\033[0;35m" + pyfiglet.figlet_format("2025", font="slant", justify="center") + "\033[0m")
            print("                         1.5.0 | Developer Preview 8")
            print("\n\n\n                    Copyright © 2024, Procyonis Computing\n\n\n                                 Starting...")
            print("                         ", end="", flush=True)
            for _ in range(5):
                print("\033[0;35m═\033[0m", end="", flush=True)
                time.sleep(0.5)
            for _ in range(8):
                print("\033[0;35m═\033[0m", end="", flush=True)
                time.sleep(0.1)
            for _ in range(3):
                print("\033[0;35m═\033[0m", end="", flush=True)
                time.sleep(0.2)
            for _ in range(5):
                print("\033[0;35m═\033[0m", end="", flush=True)
                time.sleep(0.5)
            for _ in range(3):
                print("\033[0;35m═\033[0m", end="", flush=True)
                time.sleep(0.2)
            time.sleep(2)
            kernel.clrscr()
            kernel.println("Welcome")
            time.sleep(1.5)
            kernel.clrscr()
            conn = sqlite3.connect('configuration.db')
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM users')
            user_count = cursor.fetchone()[0]
            conn.close()
            if user_count == 0:
                oobe()
                create_user_applet()
            else:
                tries = 0
                while tries <= 5:
                    ekernel.printHeader("ProcyonCLS 2025")
                    kernel.printInfo("Login")
                    kernel.printInfo("-------------------------")
                    username = input("Enter Username: ").strip()
                    password = getpass.getpass("Enter Password: ").strip()
                    user_data = get_user(username)
                    if user_data and user_data[1] == password:
                        kernel.printSuccess("Login Successful!")
                        kernel.printWarning("Hang tight..")
                        time.sleep(2)
                        prompt(get_name(username), username)
                        break
                    else:
                        kernel.printError("Login Failed!")
                        tries += 1
                        time.sleep(2)
                        kernel.clrscr()
                else:
                    kernel.printError("Maximum login attempts reached")
                    confirm = input("Do you want to reset the password (y/n) : ").strip()
                    if confirm.lower() == "y":
                        reset = input("Enter username to reset password : ").strip()
                        if get_user(reset):
                            confirmN = input("Enter your last name to confirm identity : ").strip()
                            if confirmN == get_user(reset)[3]:
                                new_password = getpass.getpass("Enter new password : ").strip()
                                update_user(reset, 'password', new_password)
                                kernel.printSuccess("Password reset successfully!")
                            else:
                                kernel.printError("Identity not confirmed")
                        else:
                            kernel.printError("User not found")
                    else:
                        kernel.printError("Exiting...")
        else:
            print("OS Error : Kernel version mismatch")
            print(f"Expected 1.5.0, got {sys.argv[1]}")
            sys.exit(1)
    else:
        print("OS Error : Shell needs kernel to run")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.bsod("0x0005", "User interrupted execution")
    except Exception as e:
        kernel.bsod("0x0006", f"Error : {e}")