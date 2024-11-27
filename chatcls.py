import kernel
import sys
import ekernel
import time

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9B":
            ekernel.splashScreen("ProcyonCLS Chat", "Version 0.9B Munnar")
            ekernel.printHeader("ChatCLS")
            kernel.println("Coming Soon..!")
            kernel.printWarning("You'll need OpenAI API key to use this feature, after it releases")
        else:
            kernel.printError("This version of evaluator is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()