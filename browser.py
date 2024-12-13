import kernel
import sys
import ekernel
from blessed import Terminal

term = Terminal()

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.0.4":
            ekernel.splashScreen("ProcyonCLS HTML Viewer", "Version 2.0.4")
            ekernel.printHeader("HTML Viewer")
            url = kernel.centered_input(term, "Enter URL : ").strip()
            kernel.println((ekernel.textBrowser(url)))
        else:
            kernel.printError(("This version of HTML Viewer is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()