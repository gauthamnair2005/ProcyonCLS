import kernel
import sys
import ekernel

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "1.0.0":
            ekernel.splashScreen("ProcyonCLS HTML Viewer", "Version 1.0.0")
            ekernel.printHeader("HTML Viewer")
            url = input("Enter URL : ").strip()
            ekernel.textBrowser(url)
        else:
            kernel.printError("This version of HTML Viewer is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()