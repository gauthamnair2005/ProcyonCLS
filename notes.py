import kernel
import sys
import ekernel
import os

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "1.6.1":
            ekernel.splashScreen("ProcyonCLS Notes", "Version 1.6.1")
            ekernel.printHeader("Notes")
            kernel.printInfo("● R - Read")
            kernel.printInfo("● W - Write")
            kernel.printInfo("● A - Append")
            kernel.printInfo("● R+ - Read and Write")
            if not os.path.exists("notes"):
                os.mkdir("notes")
            while True:
                filename = input("Enter filename : ").strip()
                if filename == "exit":
                    break
                elif filename in os.listdir():
                    kernel.printError("Cannot access system files")
                else:
                    filename = "notes/" + filename
                    accessMode = input("Enter access mode (r/w/a/r+) : ").strip()
                    try:
                        if accessMode == "r":
                            with open(filename, "r") as file:
                                kernel.println(file.read())
                        elif accessMode == "w":
                            with open(filename, "w") as file:
                                file.write(input("Enter text : "))
                        elif accessMode == "a":
                            with open(filename, "a") as file:
                                file.write(input("Enter text : "))
                        elif accessMode in ["rw", "ra"]:
                            with open(filename, "r+") as file:
                                kernel.println(file.read())
                                file.write(input("Enter text : "))
                        else:
                            kernel.printError("Invalid access mode")
                    except:
                        kernel.printError("Error accessing file")
        else:
            kernel.printError("This version of notes is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()