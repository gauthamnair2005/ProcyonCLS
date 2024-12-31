import kernel
import sys
import ekernel
import os
import updater
from blessed import Terminal

term = Terminal()

count = 0

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.3.0":
            # Initialize with splash screen
            ekernel.splashScreen("ProcyonCLS Security", "Version 2.3.0")
            
            while True:
                # Display menu
                kernel.clrscr()
                ekernel.printHeader("Security")
                print()
                kernel.printBold(("Security Update : UB-20250000"))
                print()
                kernel.printInfo(("Menu"))
                kernel.printInfo(("-" * 30))
                print()
                menu_items = [
                    "1. Scan for vulnerabilities",
                    "2. Update ProcyonCLS",
                    "3. Exit"
                ]
                for item in menu_items:
                    kernel.println((item))
                print()

                try:
                    choice = int(kernel.centered_input(term, "Enter choice: "))

                    if choice == 1:
                        kernel.println(("Performing Cloud Scan..."))
                        
                        def fetchFilefromGitHubRepo(filename):
                            import requests
                            url = f"https://raw.githubusercontent.com/gauthamnair2005/ProcyonCLS/refs/heads/main/{filename}"
                            response = requests.get(url)
                            return response.text if response.status_code == 200 else None

                        def compareFile(filename):
                            with open(filename, "r", encoding="utf-8") as file:
                                localFile = file.read().strip().replace('\r\n', '\n')
                            gitHubFile = fetchFilefromGitHubRepo(filename)
                            if gitHubFile is not None:
                                gitHubFile = gitHubFile.strip().replace('\r\n', '\n')
                                return localFile == gitHubFile
                            return None

                        def checkVulnerability(filename):
                            global count
                            if compareFile(filename):
                                filename = filename.replace(".py", "").replace("_", " ")
                                filename = filename[0].upper() + filename[1:]
                                kernel.printSuccess((f"No vulnerabilities found in {filename}"))
                            else:
                                filename = filename.replace(".py", "").replace("_", " ")
                                filename = filename[0].upper() + filename[1:]
                                kernel.printError((f"Vulnerability found in {filename}"))
                                count += 1

                        for file in os.listdir():
                            if file.endswith(".py"):
                                try:
                                    checkVulnerability(file)
                                except:
                                    kernel.printError(("Network error"))
                                    kernel.printWarning(("Please check your internet connection, performing less effective offline scan.."))
                                    
                                    with open(file, "r", encoding="utf-8") as openfile:
                                        if file != "security.py":
                                            content = openfile.read()
                                            vulnerable_paths = ["/bin", "/boot", "/dev", "/etc", "/home", "/lib", "/lib64", 
                                                             "/media", "/mnt", "/opt", "/proc", "/root", "/run", "/sbin", 
                                                             "/srv", "/sys", "/tmp", "/usr", "/var", "Windows", "System32", "SysWoW64"]
                                            if any(path in content for path in vulnerable_paths):
                                                kernel.printError((f"Vulnerability found in {file}"))
                                            else:
                                                kernel.printSuccess((f"No vulnerabilities found in {file}"))

                        if count >= 1:
                            kernel.printError((f"{count} vulnerabilities found!"))
                            kernel.printWarning(("Reason (Either of them):\n● ProcyonCLS is outdated\n● File has been modified"))
                            kernel.printInfo(("Detecting which reason is true.."))
                            
                            updTag = updater.get_latest_release()
                            curTag = updater.readCurrentTag()
                            
                            if curTag != updTag[0]:
                                kernel.printError(("Reason: ProcyonCLS is outdated"))
                                kernel.printWarning(("Please update ProcyonCLS to the latest version"))
                                confirm = kernel.centered_input(term, "Do you want to update ProcyonCLS (y/n): ").strip()
                                if confirm.lower() == "y":
                                    os.execv(sys.executable, ['python3', 'updater.py', '2.3.0'])
                                    exit(0)
                                else:
                                    kernel.printWarning(("Not updated ProcyonCLS, please update soon!"))
                            else:
                                kernel.printError(("Reason: File has been modified"))
                                kernel.printWarning(("Performing System Recovery!"))
                                kernel.printInfo(("Recovering files.."))
                                
                                for file in os.listdir():
                                    if file.endswith(".py"):
                                        if not compareFile(file):
                                            with open(file, "w", encoding="utf-8") as openfile:
                                                openfile.write(fetchFilefromGitHubRepo(file).replace('\r\n', '\n'))
                                                filename = file.replace(".py", "").replace("_", " ")
                                                filename = filename[0].upper() + filename[1:]
                                            kernel.printSuccess((f"Recovered {file}"))
                                kernel.printSuccess(("Recovered all files!"))
                        else:
                            kernel.printSuccess(("No vulnerabilities found!"))

                    elif choice == 2:
                        kernel.callApplication("updChk", isAdmin=True)

                    elif choice == 3:
                        kernel.println(("Exiting.."))
                        sys.exit(0)

                    else:
                        kernel.printWarning(("Invalid choice."))

                    kernel.println(("\nPress Enter to continue..."))
                    kernel.centered_input(term)

                except ValueError:
                    kernel.printError(("Invalid input. Please enter a number."))
                    kernel.println(("\nPress Enter to continue..."))
                    kernel.centered_input(term)

        else:
            kernel.printError(("This version of security is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError(("OS scope error"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.printWarning(("\nOperation cancelled by user"))
        sys.exit(1)