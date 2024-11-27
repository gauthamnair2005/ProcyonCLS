import kernel
import sys
import os
import pyfiglet
import time
import getpass
import ekernel
import sqlite3
import updater

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
    if newtag != currenttag:
        kernel.printWarning(f"ProcyonCLS Munnar {newtag} is available!")
        kernel.printInfo("Run 'clsupdate' to update")
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
    ekernel.prettyPrint("Welcome to ProcyonCLS")
    time.sleep(2)
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    kernel.println("Get ready to experience the ProcyonCLS Munnar")
    time.sleep(2)
    kernel.printError("..........")
    time.sleep(1)
    kernel.printWarning(".........")
    time.sleep(1)
    kernel.printSuccess(".......")
    time.sleep(1)
    kernel.printInfo("......")
    time.sleep(2)
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    time.sleep(2)
    kernel.printInfo("ProcyonCLS now is even better with new features and improvements")
    time.sleep(2)
    kernel.println("* ProcyonCLS now boots faster than ever, and is loaded with new features.")
    time.sleep(0.9)
    kernel.println("* ProcyonCLS now has a new security application, to keep your system secure.")
    time.sleep(0.9)
    kernel.println("* ProcyonCLS now has a new notes application, to keep your notes safe.")
    time.sleep(0.9)
    kernel.println("* ProcyonCLS now has a new database application, to store your data.")
    time.sleep(0.9)
    kernel.println("* ProcyonCLS now has a new evaluator application, to perform calculations.")
    time.sleep(0.9)
    kernel.println("* ProcyonCLS now has an updater, which helps you get up to date.")
    time.sleep(10)
    input("Press Enter to continue...")
    kernel.clrscr()


def create_user_applet():
    ekernel.printHeader("User Creation")
    username = input("Enter Username: ").strip()
    password = getpass.getpass("Enter Password: ").strip()
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    age = input("Enter Age: ").strip()
    age = int(age) if age.isdigit() else None
    other_details = input("Enter Other Details: ").strip()
    add_user(username, password, first_name, last_name, age, other_details)
    kernel.printSuccess("User Created Successfully!")
    kernel.printWarning("Please wait..")
    time.sleep(5)
    prompt(first_name, username)

def prompt(user, username):
    updateCheckOnStart()
    kernel.clrscr()
    ekernel.prettyPrint(f"Welcome, {user}")
    time.sleep(3)
    kernel.clrscr()
    ekernel.printHeader("ProcyonCLS Desktop")
    kernel.printWarning("This is a Pre-Release version of ProcyonCLS!")
    kernel.printInfo("Check for updates regularly to get latest bugfixes and features.")
    kernel.println(time.strftime("%d/%m/%Y %H:%M:%S"))
    while True:
        prmpt = input(f"\033[92m{username}\033[0m@\033[96mProcyonCLS\033[0m:~\033[93m$\033[0m ").strip()
        if prmpt == "exit" or prmpt == "shutdown":
            kernel.shutDown()
        elif prmpt == "reboot":
            kernel.reboot()
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
        elif prmpt == "database":
            kernel.callApplication("database", isAdmin=False)
        elif prmpt == "linea":
            kernel.callApplication("linearun", isAdmin=False)
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
            if ekernel.admin(username):
                os.execv(sys.executable, ['python3', 'updater.py', 'KRNL_0.5'])
            else:
                kernel.printError("Admin access denied, updater needs admin access to run!")
        elif prmpt == "security":
            if ekernel.admin(username):
                kernel.callApplication("security", isAdmin=True)
            else:
                kernel.printError("Admin access denied, security needs admin access to run!")
        elif prmpt in ["dir", "ls"]:
            kernel.println(os.listdir())
        elif prmpt == "ver":
            ekernel.printHeader("Version Information")
            kernel.printInfo("ProcyonCLS Pre-Release Build")
            kernel.println(f"Version : {kernel.getVersion()}")
            kernel.println(f"Code Name : {kernel.getCodeName()}")
            kernel.println(f"Release : {kernel.getRelease()}")
        elif prmpt == "info":
            ekernel.printHeader("Software Information")
            kernel.printInfo("ProcyonCLS Pre-Release Build")
            kernel.println(f"Version : {kernel.getVersion()}")
            kernel.println(f"Build : {kernel.getBuild()}")
            kernel.println(f"Author : {kernel.getAuthor()}")
            kernel.println(f"Company : {kernel.getCompany()}")
            kernel.println(f"License : {kernel.getLicense()}")
            kernel.println(f"Kernel Name : {kernel.getKernelName()}")
            kernel.println(f"Code Name : {kernel.getCodeName()}")
            kernel.println(f"Release : {kernel.getRelease()}")
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
                else:
                    kernel.printError("Invalid field")
            else:
                kernel.printError("Usage: update <field> <value>")
        elif prmpt == "create user":
            create_user_applet()
        elif prmpt == "help":
            ekernel.printHeader("Help")
            kernel.printInfo("Available commands :")
            kernel.println("help - Display this help message")
            kernel.println("exit - Exit the shell")
            kernel.println("bsod - Invoke a Blue Screen of Death")
            kernel.println("run <application> - Run a 3rd party application")
            kernel.println("admin <application> - Run a 3rd party application with admin privileges")
            kernel.println("clrscr - Clear the screen")
            kernel.println("eval - Open the evaluator")
            kernel.println("date - Display the current date")
            kernel.println("time - Display the current time")
            kernel.println("datetime - Display the current date and time")
            kernel.println("reset password - Reset the user password")
            kernel.println("update <field> <value> - Update user details")
            kernel.println("create user - Create a new user")
            kernel.println("ver - Display OS version information")
            kernel.println("info - Display OS information")
            kernel.println("notes - Open the notes application")
            kernel.println("dir/ls - List files and folders in the current directory")
            kernel.println("mkdir - Create a new folder")
            kernel.println("security - Open the security application")
            kernel.println("delete - Delete a file")
            kernel.println("reboot - Reboot the system")
            kernel.println("shutdown - Shutdown the system")
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
            try:
                kernel.callApplication(prmpt[4:], isAdmin=False)
            except Exception as e:
                kernel.printError(f"Error running 3rd party application: {e}")
        elif prmpt.startswith("admin "):
            if ekernel.admin(username):
                if prmpt[6:] in ["bootload", "kernel", "shell", "ekernel"]:
                    kernel.printError("Cannot run system files")
                else:
                    try:
                        kernel.callApplication(prmpt[6:], isAdmin=True)
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
        if sys.argv[1] == "0.9B":
            os.system("cls" if sys.platform == "win32" else "clear")
            print(pyfiglet.figlet_format("ProcyonCLS", font="slant", justify="center"))
            print("0.9B Munnar")
            print("\n\n\nCopyright © 2024, Procyonis Computing\n\n\nStarting...")
            for _ in range(5):
                print("═", end="", flush=True)
                time.sleep(0.5)
            for _ in range(50):
                print("═", end="", flush=True)
                time.sleep(0.1)
            for _ in range(3):
                print("═", end="", flush=True)
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
                while True:
                    ekernel.printHeader("Login")
                    username = input("Enter Username: ").strip()
                    password = getpass.getpass("Enter Password: ").strip()
                    user_data = get_user(username)
                    if user_data and user_data[1] == password:
                        kernel.printSuccess("Login Successful!")
                        kernel.printWarning("Please wait..")
                        time.sleep(2)
                        prompt(get_name(username), username)
                        break
                    else:
                        kernel.printError("Login Failed!")
                        time.sleep(2)
                        kernel.clrscr()
        else:
            print("OS Error : Kernel version mismatch")
            print(f"Expected 0.9B, got {sys.argv[1]}")
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