import kernel
import sys
import ekernel

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9C":
            ekernel.splashScreen("Linea Programming Language", "0.5 'Bettafish'")
            ekernel.printHeader("Linea")
            kernel.println("Coming Soon..!")
        else:
            kernel.printError("This version of Linea is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()