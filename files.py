import kernel
import ekernel
import os
import sys
import time

def print_directory_contents(path="."):
    contents = os.listdir(path)
    max_width = 4
    col_width = max(len(name) for name in contents) + 2

    for i, name in enumerate(contents):
        if os.path.isdir(os.path.join(path, name)):
            kernel.println(f"\033[38;2;255;165;0m{name:<{col_width - 2}}\033[0m", end='')
        else:
            kernel.println(f"{name:<{col_width}}", end='')
        if (i + 1) % max_width == 0:
            print()
    if len(contents) % max_width != 0:
        print()

def view_file_properties(path, filename):
    file_path = os.path.join(path, filename)
    if os.path.exists(file_path):
        kernel.printInfo(f"Properties of {filename}:")
        kernel.printInfo(f"Size: {os.path.getsize(file_path)} bytes")
        kernel.printInfo(f"Created: {time.ctime(os.path.getctime(file_path))}")
        kernel.printInfo(f"Modified: {time.ctime(os.path.getmtime(file_path))}")
        kernel.printInfo(f"Accessed: {time.ctime(os.path.getatime(file_path))}")
    else:
        kernel.printError(f"File {filename} does not exist.")

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "1.9.1":
            ekernel.splashScreen("ProcyonCLS File Explorer", "Version 1.9.1")
            ekernel.printHeader("File Explorer")
            current_path = os.getcwd()
            while True:
                kernel.printInfo(f"\nCurrent Directory: {current_path}")
                print_directory_contents(current_path)
                kernel.println("\nOptions:")
                kernel.println("1. Change Directory (cd)")
                kernel.println("2. View File Properties")
                kernel.println("3. Exit")
                choice = input("Enter choice: ")

                if choice == "1":
                    new_dir = input("Enter directory to change to: ")
                    new_path = os.path.join(current_path, new_dir)
                    if os.path.isdir(new_path):
                        current_path = new_path
                    else:
                        kernel.printError(f"Directory {new_dir} does not exist.")
                elif choice == "2":
                    filename = input("Enter filename to view properties: ")
                    view_file_properties(current_path, filename)
                elif choice == "3":
                    kernel.printInfo("Exiting File Explorer.")
                    break
                else:
                    kernel.printError("Invalid choice. Please enter a number between 1 and 3.")
        else:
            kernel.printError("This version of File Explorer is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()