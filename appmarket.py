import kernel
import sys
import ekernel
import time

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9B":
            ekernel.splashScreen("ProcyonCLS App Market", "Version 0.9B Munnar")
            ekernel.printHeader("App Market")
            kernel.println("Coming Soon..!")
        else:
            kernel.printError("This version of market is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()