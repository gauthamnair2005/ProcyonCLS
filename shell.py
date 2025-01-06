import kernel
import sys
import os
import time
import datetime
import getpass
import ekernel
import sqlite3
import updater
import requests
import blessed
from blessed import Terminal

term = Terminal()

logo = """
                                                    
                                    *+++******             
                               *++*******#######**         
                             ++****************####**      
                            +***++*******####******###     
                          *+**++++*****###%###******###    
                         ****+++*****###%%%%%###*****#%#   
                         ****+****##%%##%%%%%%%##****##%#  
                         #******##%%%%%%##########*####%%  
                         ##*****###%%%%%%##%%%%%#####%#%%  
                         %%###########%%%#####%%%%%%%##%#  
                          %%%%%%################%%%%##%%   
                           %%%%%%%%%%%%%%%%%%%%%%%%##%%    
                            %%%%%%%%%%%%%%%%%%%%%%#%%%     
                              #%%%%%%%%%%%%%%%%%%%%%       
                                ###%%%%%%%%%%%%%%%         
                                     #######%                                  
                                        
            """

def boot():
    kernel.clrscr()
    lines = logo.split('\n')
    max_line_length = max(len(line) for line in lines)
    terminal_width = term.width
    padding = (terminal_width - max_line_length) // 2
    centered_logo = '\n'.join(' ' * padding + line for line in lines)
    kernel.println(term.magenta(centered_logo))
    kernel.println((f"{kernel.getReleaseName()}"))
    kernel.println((f"Copyright © {datetime.datetime.now().year}, Procyonis Computing"))
    print()
    
    # Progress bar positioning and animation
    progress_y = term.height - 5
    bar_width = min(50, term.width - 20)
    padding = (term.width - bar_width) // 2
    
    # Move cursor and show progress
    print(term.move_y(progress_y))
    kernel.println(("Starting..."))
    
    for i in range(bar_width + 1):
        bar = '═' * i + '─' * (bar_width - i)
        print(term.move_x(padding) + f"{bar}", end='\r', flush=True)
        
        if i < bar_width * 0.3:
            time.sleep(0.1)
        elif i < bar_width * 0.7:
            time.sleep(0.05)
        else:
            time.sleep(0.08)
    
    print()
    time.sleep(1)
    kernel.clrscr()

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

def displayLogo():
    term = blessed.Terminal()
    
    logo_text = """
                    
     *****####*     
   **++***##***##   
  **+**##%%%##**##% 
 #***#%%%%##%####%% 
  %%%#########%%%%  
   %%%%%%%%%%%%%%   
      ##%%%%%%      
                    
"""
    lines = logo_text.split('\n')
    max_line_length = max(len(line) for line in lines)
    terminal_width = term.width
    padding = (terminal_width - max_line_length) // 2
    centered_logo = '\n'.join(' ' * padding + line for line in lines)
    kernel.println(term.magenta(centered_logo))

def updateCheckOnStart():
    newtag = updater.get_latest_release()
    currenttag = updater.read_current_tag()
    if newtag[0] > currenttag:
        kernel.printWarning(f"Version {newtag[0]} is available!")
        kernel.printInfo("Run 'clsupdate' to see what's new and update")
        time.sleep(2)
    return None

def fetchMOTD():
    try:
        url = "https://raw.githubusercontent.com/gauthamnair2005/ProcyonCLS-MOTD/main/motd.txt"
        response = requests.get(url)
        response.raise_for_status()
        text = response.text
        text = str(text)
        kernel.printBold((text))
    except:
        kernel.printError(("Could not fetch MOTD.!"))

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
    term = blessed.Terminal()
    
    # Welcome screen
    kernel.clrscr()
    ekernel.prettyPrint(term.center(f"Welcome to {kernel.getReleaseName()}"))
    time.sleep(2)
    
    sections = [
        {
            "title": "ProcyonCLS got better",
            "content": "With ProcyonCLS 2025, you get a rich and secure experience along with the new AppMarket, ChatCLS, NetGet and more!"
        },
        {
            "title": "Security at its peak",
            "content": "ProcyonCLS 2025 comes with enhanced security features to protect your data and privacy. Like updates, password reset, secure account verification and system repair!"
        },
        {
            "title": "AppMarket",
            "content": "ProcyonCLS 2025 comes with AppMarket, a place to download and install applications.",
            "note": "To publish your application, pull request on GitHub."
        },
        {
            "title": "ChatCLS",
            "content": "ProcyonCLS 2025 comes with ChatCLS, an AI powered chat application.",
            "note": "ChatCLS is still in beta, and requires OpenAI API key."
        },
        {
            "title": "NetGet",
            "content": "ProcyonCLS 2025 comes with NetGet, a network download tool.",
            "note": "NetGet is still in beta, and requires internet connection."
        },
        {
            "title": "Files",
            "content": "ProcyonCLS 2025 comes with Files, a file manager application."
        }
    ]
    for section in sections:
        kernel.clrscr()
        ekernel.printHeader("Out of Box Experience")
        print()
        kernel.printInfo((f"ProcyonCLS 2025 : {section['title']}"))
        kernel.printInfo(("-" * (len(section['title']) + 20)))
        time.sleep(1)
        content_lines = section['content'].split('\n')
        for line in content_lines:
            print(term.center(line))
            
        if 'note' in section:
            kernel.printWarning((f"Note: {section['note']}"))
            
        print()
        kernel.centered_input(term, "Press any key to continue...")
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    print()
    kernel.printInfo(("Checking for updates..."))
    time.sleep(1)
    
    if updater.get_latest_release()[0] > updater.read_current_tag():
        kernel.printWarning(("[Outdated]"))
        if kernel.centered_input(term, "Update available, do you want to update? (y/n): ").strip().lower() == "y":
            os.execv(sys.executable, ['python3', 'updater.py', '2.3.5'])
        else:
            kernel.printWarning(("Not Updating"))
    else:
        kernel.printSuccess(("[Up to date]"))
    
    time.sleep(2)
    kernel.clrscr()
    ekernel.printHeader("Out of Box Experience")
    ekernel.prettyPrint(term.center("Let's Get Started"))
    time.sleep(2)
    kernel.clrscr()

def create_user_applet():
    ekernel.printHeader(f"{kernel.getReleaseName()}")
    kernel.printInfo(("Create a new user"))
    kernel.printInfo(("-" * (len("Create a new user") + 20)))
    username = kernel.centered_input(term, "Enter a nice Username: ").strip()
    while True:
        if get_user(username):
            kernel.printWarning(("Username already exists!"))
            username = kernel.centered_input(term, "Enter a unique and nice Username: ").strip()
        else:
            break
    while True:
        password = getpass.getpass(term.center("Enter a good Password: ")).strip()
        while True:
            if len(password) < 8:
                kernel.printWarning(("Password must be at least 8 characters long!"))
                password = getpass.getpass(term.center("Enter a bigger Password: ")).strip()
            else:
                break
        confirm = getpass.getpass(term.center("Confirm Password: ")).strip()
        if password == confirm:
            break
        else:
            kernel.printError(("Passwords do not match!"))
    first_name = kernel.centered_input(term, "Enter your First Name: ").strip()
    last_name = kernel.centered_input(term, "Enter your Last Name: ").strip()
    age = kernel.centered_input(term, "Enter your Age: ").strip()
    age = int(age) if age.isdigit() else None
    other_details = kernel.centered_input(term, "Enter your Other Details: ").strip()
    add_user(username, password, first_name, last_name, age, other_details)
    kernel.printSuccess(("User Created Successfully!"))
    kernel.printWarning(("Hang on.."))
    time.sleep(2)
    prompt(first_name, username)

def prompt(user, username):
    term = blessed.Terminal()
    kernel.clrscr()
    with term.location(0, term.height // 2):
        ekernel.prettyPrint(term.center(f"Welcome {user}!"))
    time.sleep(2)
    kernel.clrscr()
    ekernel.printHeader("ProcyonCLS")
    updateCheckOnStart()
    kernel.printInfo("Message Of The Day")
    kernel.printInfo("-" * (len("Message Of The Day") + 20))
    fetchMOTD()
    kernel.printInfo("Workspace")
    kernel.printInfo("-" * (len("Workspace") + 20))
    kernel.printInfo(time.strftime("Date : %d/%m/%Y"))
    kernel.printInfo(time.strftime("Time : %H:%M:%S"))
    if sys.platform == "win32":
        print()
    else:
        kernel.printWarning("Note : You are running ProcyonCLS on a Unix/Linux system, so make sure you type the apps to run in correct case as mentioned in AppMarket or the file directory listing.")
    while True:
        prompt_text = (f"{term.bright_green(username)}"
                      f"{term.normal}@"
                      f"{term.bright_cyan('ProcyonCLS')}"
                      f"{term.normal}:~"
                      f"{term.yellow('$')} ")
        prmpt = input(prompt_text).strip()
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
            fileFolder = kernel.centered_input(term, "Enter file name to delete : ").strip()
            if os.path.exists(fileFolder):
                try:
                    os.remove(fileFolder)
                    kernel.printSuccess((f"{fileFolder} deleted successfully!"))
                except Exception as e:
                    kernel.printError((f"Error deleting file: {e}"))
            else:
                kernel.printError((f"{fileFolder} not found"))
        elif prmpt.startswith("mkdir "):
            folder = prmpt[6:]
            if sys.platform == "win32" and folder.lower() in ["con", "prn", "aux", "nul"] + [f"com{i}" for i in range(1, 10)] + [f"lpt{i}" for i in range(1, 10)]:
                kernel.bsod("0x0007", "Attempted to create system file")
            else:
                try:
                    with open("protected_dirs.txt", "a") as f:
                        f.write(folder + "\n")
                        f.close()
                    os.mkdir(folder)
                    kernel.printSuccess((f"{folder} created successfully!"))
                except Exception as e:
                    kernel.printError((f"Error creating folder: {e}"))
        elif prmpt == "mkdir":
            folder = kernel.centered_input(term, "Enter folder name : ").strip()
            if sys.platform == "win32" and folder.lower() in ["con", "prn", "aux", "nul"] + [f"com{i}" for i in range(1, 10)] + [f"lpt{i}" for i in range(1, 10)]:
                kernel.bsod("0x0007", "Attempted to create system file")
            else:
                try:
                    os.mkdir(folder)
                    kernel.printSuccess((f"{folder} created successfully!"))
                except Exception as e:
                    kernel.printError((f"Error creating folder: {e}"))
        elif prmpt == "notes":
            kernel.callApplication("notes", isAdmin=False)
        elif prmpt == "market" or prmpt == "appmarket" or prmpt == "appstore" or prmpt == "store":
            if ekernel.admin(username):
                kernel.printSuccess(("Admin access granted"))
                kernel.callApplication("appmarket", isAdmin=True)
            else:
                kernel.printError(("Admin access denied, market needs admin access to run!"))
        elif prmpt == "python":
            os.system("python3")
        elif prmpt.startswith("for "):
            parts = prmpt[4:].split()
            if len(parts) == 4:
                if parts[1] == "till":
                    if parts[2].isdigit():
                        if parts[0] == parts[4]:
                            if parts[3] == "echo":
                                for i in range(0, int(parts[2].split(":")[0])):
                                    print(i)
                            else:
                                kernel.printError(("Invalid command for for loop"))
                        else:
                            kernel.printError(("Invalid iterator or invalid call of iterator"))
                    else:
                        kernel.printError(("Invalid range"))
                else:
                    kernel.printError(("Invalid for loop action"))
            else:
                kernel.printError(("Invalid for loop syntax"))
        elif prmpt == "browser":
            kernel.callApplication("browser", isAdmin=False)
        elif prmpt == "clsupdate":
            if ekernel.admin(username):
                kernel.printSuccess(("Admin access granted"))
                kernel.callApplication("updChk", isAdmin=True)
            else:
                kernel.printError(("Admin access denied, updater needs admin access to run!"))
        elif prmpt == "security":
            if ekernel.admin(username):
                kernel.printSuccess(("Admin access granted"))
                kernel.callApplication("security", isAdmin=True)
            else:
                kernel.printError(("Admin access denied, security needs admin access to run!"))
        elif prmpt in ["dir", "ls"]:
            kernel.printInfo((f"{os.getcwd()}"))
            for i in os.listdir():
                kernel.println((i))
        elif prmpt == "info" or prmpt == "ver":
            kernel.printInfo(("Software Information"))
            kernel.printInfo(("-------------------------"))
            displayLogo()
            kernel.printInfo(("Information"))
            kernel.println((f"{kernel.getReleaseName()}"))
            kernel.println((f"{kernel.getVersion()}"))
            kernel.println((f"{kernel.getCodeName()}"))
            kernel.println((f"{kernel.getBuild()}"))
            kernel.println((f"{kernel.getAuthor()}"))
            kernel.println((f"{kernel.getCompany()}"))
            kernel.println((f"{kernel.getLicense()}"))
            kernel.println((f"{kernel.getKernelName()} {kernel.getVersion()}"))
            kernel.println((f"{kernel.getRelease()}"))
        elif prmpt in ["calc", "calculator", "eval", "evaluator"]:
            try:
                kernel.callApplication("evaluator", isAdmin=False)
            except:
                kernel.printError((f"Error running evaluator"))
        elif prmpt == "date":
            kernel.println((time.strftime("%d/%m/%Y")))
        elif prmpt == "time":
            kernel.println((time.strftime("%H:%M:%S")))
        elif prmpt == "datetime":
            kernel.println((time.strftime("%d/%m/%Y %H:%M:%S")))
        elif prmpt in ["reset password", "reset-password"]:
            ekernel.printHeader("Reset Password")
            if ekernel.admin(user, "Enter old password : "):
                kernel.printSuccess(("Admin access granted"))
                password = getpass.getpass(term.center("Enter new password : ")).strip()
                update_user(user, 'password', password)
                kernel.printSuccess(("Password reset successfully!"))
            else:
                kernel.printError(("Admin access denied"))
        elif prmpt == "update":
            kernel.printError(("Usage: update <field> <value>"))
        elif prmpt.startswith("update "):
            parts = prmpt.split()
            if len(parts) == 3:
                field, value = parts[1], parts[2]
                if field in ['username', 'first_name', 'last_name', 'age', 'other_details']:
                    update_user(user, field, value)
                    kernel.printSuccess((f"{field} updated successfully!"))
                elif field == "password":
                    kernel.printError(("Cannot update password here"))
                    kernel.printWarning(("Use 'reset password' to reset password"))
                else:
                    kernel.printError(("Invalid field"))
            else:
                kernel.printError(("Usage: update <field> <value>"))
        elif prmpt == "create user":
            create_user_applet()
        elif prmpt == "file" or prmpt == "files":
            kernel.callApplication("files", isAdmin=False)
        elif prmpt == "help":
            ekernel.printHeader("Help")
            kernel.printInfo(("Available Commands"))
            kernel.println(("help - Display this help message"))
            kernel.println(("run <application> - Run a 3rd party application"))
            kernel.println(("admin <application> - Run a 3rd party application with admin prVileges"))
            kernel.println(("clrscr - Clear the screen"))
            kernel.println(("eval - Open the evaluator"))
            kernel.println(("date - Display the current date"))
            kernel.println(("time - Display the current time"))
            kernel.println(("datetime - Display the current date and time"))
            kernel.println(("reset password - Reset the user password"))
            kernel.println(("update <field> <value> - Update user details"))
            kernel.println(("create user - Create a new user"))
            kernel.println(("ver - Display OS version information"))
            kernel.println(("info - Display OS information"))
            kernel.println(("notes - Open the notes application"))
            kernel.println(("dir - List files and folders in the current directory"))
            kernel.println(("mkdir - Create a new folder"))
            kernel.println(("security - Open the security application"))
            kernel.println(("delete - Delete a file"))
            kernel.println(("chatcls - Open the ChatCLS application"))
            kernel.println(("market - Open the AppMarket application"))
            kernel.println(("clsupdate - Update the OS"))
            kernel.println(("file - Open the Files application"))
            kernel.println(("browser - Open the browser application"))
            kernel.println(("netget - Open the NetGet application"))
            kernel.println(("delete user - Delete the current user"))
            kernel.println(("reboot - Reboot the system"))
            kernel.println(("shutdown - Shutdown the system"))
        elif prmpt.startswith("prettyprint "):
            ekernel.prettyPrint(prmpt[12:])
        elif prmpt.startswith("echo "):
            kernel.println(prmpt[5:])
        elif prmpt == "logout":
            break
        elif prmpt == "delete user":
            if ekernel.admin(username):
                kernel.printSuccess(("Admin access granted"))
                delete_user(username)
                kernel.printSuccess(("User deleted successfully!"))
                break
            else:
                kernel.printError(("Admin access denied"))
        elif prmpt == "bsod":
            kernel.bsod("0x0004", "User invoked BSOD")
        elif prmpt.startswith("run "):
            if prmpt[4:] in ["bootload", "kernel", "shell", "ekernel"]:
                kernel.printError(("Cannot run system files"))
            else:
                try:
                    kernel.callApplication3P(prmpt[4:], isAdmin=False)
                except Exception as e:
                    kernel.printError((f"Error running 3rd party application: {e}"))
        elif prmpt.startswith("admin "):
            if ekernel.admin(username):
                if prmpt[6:] in ["bootload", "kernel", "shell", "ekernel"]:
                    kernel.printError(("Cannot run system files"))
                else:
                    try:
                        kernel.printSuccess(("Admin access granted"))
                        kernel.callApplication3P(prmpt[6:], isAdmin=True)
                    except Exception as e:
                        kernel.printError((f"Error running 3rd party application: {e}"))
            else:
                kernel.printError(("Admin access denied"))
        elif prmpt == "clrscr":
            kernel.clrscr()
        elif prmpt == "" or prmpt.isspace():
            continue
        else:
            kernel.printError((f"Command '{prmpt}' not found"))

def main():
    initialize_db()
    if len(sys.argv) == 2:
        if sys.argv[1] >= "2.3.5":
            kernel.clrscr()
            boot()
            time.sleep(2)
            kernel.clrscr()
            kernel.println(("Welcome"))
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
                    ekernel.printHeader(f"{kernel.getReleaseName()}")
                    kernel.printInfo(("Login"))
                    kernel.printInfo(("-" * ((len("Login") + 20))))
                    username = kernel.centered_input(term, "Enter Username: ").strip()
                    password = getpass.getpass(term.center("Enter Password: ")).strip()
                    user_data = get_user(username)
                    if user_data and user_data[1] == password:
                        kernel.printSuccess(("Login Successful!"))
                        kernel.printWarning(("Hang on.."))
                        time.sleep(2)
                        prompt(get_name(username), username)
                        break
                    else:
                        kernel.printError(("Login Failed!"))
                        tries += 1
                        time.sleep(2)
                        kernel.clrscr()
                else:
                    kernel.printError(("Maximum login attempts reached"))
                    confirm = kernel.centered_input(term, "Do you want to reset the password (y/n) : ").strip()
                    if confirm.lower() == "y":
                        reset = kernel.centered_input(term, "Enter username to reset password : ").strip()
                        if get_user(reset):
                            confirmN = kernel.centered_input(term, "Enter your last name to confirm identity : ").strip()
                            if confirmN == get_user(reset)[3]:
                                new_password = getpass.getpass(term.center("Enter new password : ")).strip()
                                update_user(reset, 'password', new_password)
                                kernel.printSuccess(("Password reset successfully!"))
                            else:
                                kernel.printError(("Identity not confirmed"))
                        else:
                            kernel.printError(("User not found"))
                    else:
                        kernel.printError(("Exiting..."))
        else:
            print("OS Error : Kernel version mismatch")
            print(f"Expected 2.3.5, got {sys.argv[1]}")
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