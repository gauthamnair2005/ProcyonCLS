import kernel
import sys
import ekernel
import os

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9L":
            ekernel.splashScreen("ProcyonCLS App Market", "Version 0.9L")
            ekernel.printHeader("App Market")
            if not os.path.exists("apps"):
                os.mkdir("apps")
            kernel.println("Submit your apps to ProcyonCLS App Market to see them here soon..!")
        else:
            kernel.printError("This version of market is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()