import kernel
import sys
import ekernel
import os
import updater

count = 0

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9JC2":
            ekernel.splashScreen("ProcyonCLS Security", "Version 0.9JC2")
            ekernel.printHeader("Security")
            kernel.printInfo("Security Update : UB-20241201-3")
            kernel.println("1. Scan for vulnerabilities")
            kernel.println("2. Update ProcyonCLS")
            kernel.println("3. Exit")
            while True:
                try:
                    choice = int(input("Enter choice : "))
                    break
                except ValueError:
                    kernel.printWarning("Invalid input. Please enter a number.")
            if choice == 1:
                kernel.println("Performing Cloud Scan...")
                def fetchFilefromGitHubRepo(filename):
                    import requests
                    url = "https://raw.githubusercontent.com/gauthamnair2005/ProcyonCLS/refs/heads/main/" + filename
                    response = requests.get(url)
                    if response.status_code == 200:
                        return response.text
                    else:
                        return None
                def compareFile(filename):
                    with open(filename, "r", encoding="utf-8") as file:
                        localFile = file.read().strip().replace('\r\n', '\n')
                    gitHubFile = fetchFilefromGitHubRepo(filename)
                    if gitHubFile is not None:
                        gitHubFile = gitHubFile.strip().replace('\r\n', '\n')
                        if localFile == gitHubFile:
                            return True
                        else:
                            return False
                    else:
                        return None
                def checkVulnerability(filename):
                    global count
                    if compareFile(filename):
                        kernel.printSuccess("No vulnerabilities found in " + filename)
                    else:
                        kernel.printError("Vulnerability found in " + filename)
                        count += 1
                for file in os.listdir():
                    if file.endswith(".py"):
                        try:
                            checkVulnerability(file)
                        except:
                            kernel.printError("Network error")
                            kernel.printWarning("Please check your internet connection, performing less effectVe offline scan..")
                            with open(file, "r", encoding="utf-8") as openfile:
                                if file != "security.py":
                                    content = openfile.read()
                                    vulnerable_paths = ["/bin", "/boot", "/dev", "/etc", "/home", "/lib", "/lib64", "/media", "/mnt", "/opt", "/proc", "/root", "/run", "/sbin", "/srv", "/sys", "/tmp", "/usr", "/var", "Windows", "System32", "SysWoW64"]
                                    if any(path in content for path in vulnerable_paths):
                                        kernel.printError("Vulnerability found in " + file)
                                    else:
                                        kernel.printSuccess("No vulnerabilities found in " + file)
                if count >= 1:
                    kernel.printError(f"{count} vulnerabilities found.!") 
                    kernel.printWarning("Reason (Either of them):\n● ProcyonCLS is outdated\n● File has been modified")
                    kernel.printInfo("Detecting which reason is true..")
                    updTag = updater.getLatestReleaseTagOnly()
                    curTag = updater.readCurrentTag()
                    if curTag != updTag:
                        kernel.printError("Reason : ProcyonCLS is outdated")
                        kernel.printWarning("Please update ProcyonCLS to the latest version")
                        confirm = input("Do you want to update ProcyonCLS (y/n) : ").strip()
                        if confirm.lower() == "y":
                            os.execv(sys.executable, ['python3', 'updater.py', '0.9JC2'])
                            exit(0)
                        else:
                            kernel.printWarning("Not updated ProcyonCLS, please update soon..!")
                    else:
                        kernel.printError("Reason : File has been modified")
                        kernel.printWarning("Performing System Recovery..!")
                        kernel.printInfo("Recovering files..")
                        for file in os.listdir():
                            if file.endswith(".py"):
                                if not compareFile(file):
                                    with open(file, "w", encoding="utf-8") as openfile:
                                        openfile.write(fetchFilefromGitHubRepo(file).replace('\r\n', '\n'))
                                    kernel.printSuccess("Recovered " + file)
                        kernel.printSuccess("Recovered all files..!")
                else:
                    kernel.printSuccess("No vulnerabilities found.!")
            elif choice == 2:
                confirm = input("Running updater will terminate current session. Do you want to continue (y/n) : ").strip()
                if confirm.lower() == "y":
                    os.execv(sys.executable, ['python3', 'updater.py', '0.9JC2'])
                    exit(0)
            elif choice == 3:
                kernel.println("Exiting..")
                sys.exit(0)
            else:
                kernel.printWarning("Invalid choice.")
        else:
            kernel.printError("This version of security is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS scope error")

if __name__ == "__main__":
    main()