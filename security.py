import kernel
import sys
import ekernel
import os
import time

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9FC2":
            ekernel.splashScreen("ProcyonCLS Security", "Version 0.9FC2")
            ekernel.printHeader("Security")
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
                kernel.println("Scanning for vulnerabilities..")
                for i in os.listdir():
                    if i.endswith(".py"):
                        with open(i, "r", encoding = "utf-8") as file:
                            if "security.py" not in i:
                                if "System32" in file.read() or "WINDOWS" in file.read() or "/bin" in file.read():
                                    kernel.printWarning(f"Potential vulnerability found in {i}")
                                else:
                                    time.sleep(2)
                                    kernel.printSuccess(f"No vulnerabilities found in {i}")
                            else:
                                pass
            elif choice == 2:
                confirm = input("Running updater will terminate current session. Do you want to continue (y/n) : ").strip()
                if confirm.lower() == "y":
                    os.execv(sys.executable, ['python3', 'updater.py', '0.9FC2'])
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