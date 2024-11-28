import kernel
import sys
import ekernel

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9FC2":
            ekernel.splashScreen("ProcyonCLS Text Browser", "Version 0.9FC2")
            ekernel.printHeader("Text Browser")
            url = input("Enter URL : ").strip()
            ekernel.textBrowser(url)
        else:
            kernel.printError("This version of browser is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()