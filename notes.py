import kernel
import sys
import ekernel
import os
from blessed import Terminal

term = Terminal()

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.0.5":
            ekernel.splashScreen("ProcyonCLS Notes", "Version 2.0.5")
            ekernel.printHeader("Notes")
            if not os.path.exists("notes"):
                os.mkdir("notes")
            notes = os.listdir("notes")
            kernel.printInfo(("Information"))
            kernel.printInfo(("-" * ((len("Information") + 20))))
            kernel.printInfo(("● R - Read"))
            kernel.printInfo(("● W - Write"))
            kernel.printInfo(("● A - Append"))
            kernel.printInfo(("● R+ - Read and Write"))
            print()
            kernel.printInfo(("Created Notes"))
            kernel.printInfo(("-" * ((len("Created Notes") + 20))))
            if not notes:
                kernel.printWarning(("No notes created yet. Created notes will be seen here"))
            else:
                for note in notes:
                    kernel.println((note))
            print()
            while True:
                filename = kernel.centered_input(term, "Enter filename : ").strip()
                if filename == "exit":
                    break
                elif filename in os.listdir():
                    kernel.printError(("Cannot access system files"))
                else:
                    filename = "notes/" + filename
                    accessMode = kernel.centered_input(term, "Enter access mode (r/w/a/r+) : ").strip()
                    try:
                        if accessMode == "r":
                            with open(filename, "r") as file:
                                kernel.println((file.read()))
                        elif accessMode == "w":
                            with open(filename, "w") as file:
                                file.write(kernel.centered_input(term, "Enter text : "))
                        elif accessMode == "a":
                            with open(filename, "a") as file:
                                file.write(kernel.centered_input(term, "Enter text : "))
                        elif accessMode in ["rw", "ra"]:
                            with open(filename, "r+") as file:
                                kernel.println(file.read())
                                file.write(kernel.centered_input(term, "Enter text : "))
                        else:
                            kernel.printError(("Invalid access mode"))
                    except:
                        kernel.printError(("Error accessing file"))
        else:
            kernel.printError(("This version of notes is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError(("OS Scope Error"))

if __name__ == "__main__":
    main()