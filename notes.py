import kernel
import sys
import ekernel
import os
from blessed import Terminal

term = Terminal()

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.0.2":
            ekernel.splashScreen("ProcyonCLS Notes", "Version 2.0.2")
            ekernel.printHeader("Notes")
            if not os.path.exists("notes"):
                os.mkdir("notes")
            notes = os.listdir("notes")
            kernel.printInfo(term.center("Information"))
            kernel.printInfo(term.center("-" * ((len("Information") + 20))))
            kernel.printInfo(term.center("● R - Read"))
            kernel.printInfo(term.center("● W - Write"))
            kernel.printInfo(term.center("● A - Append"))
            kernel.printInfo(term.center("● R+ - Read and Write"))
            print()
            kernel.printInfo(term.center("Created Notes"))
            kernel.printInfo(term.center("-" * ((len("Created Notes") + 20))))
            if not notes:
                kernel.printWarning(term.center("No notes created yet. Created notes will be seen here"))
            else:
                for note in notes:
                    kernel.println(term.center(note))
            print()
            while True:
                filename = kernel.centered_input(term, "Enter filename : ").strip()
                if filename == "exit":
                    break
                elif filename in os.listdir():
                    kernel.printError(term.center("Cannot access system files"))
                else:
                    filename = "notes/" + filename
                    accessMode = kernel.centered_input(term, "Enter access mode (r/w/a/r+) : ").strip()
                    try:
                        if accessMode == "r":
                            with open(filename, "r") as file:
                                kernel.println(term.center(file.read()))
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
                            kernel.printError(term.center("Invalid access mode"))
                    except:
                        kernel.printError(term.center("Error accessing file"))
        else:
            kernel.printError(term.center("This version of notes is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError(term.center("OS Scope Error"))

if __name__ == "__main__":
    main()