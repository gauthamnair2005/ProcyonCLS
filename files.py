import kernel
import ekernel
import os
import sys
import time
from blessed import Terminal

term = Terminal()

def print_directory_contents(path="."):
    try:
        contents = sorted(os.listdir(path))
        if not contents:
            kernel.printWarning(term.center("Empty directory"))
            return

        # Print header
        kernel.printInfo(term.center("Directory Contents"))
        kernel.printInfo(term.center("-" * 30))
        print()

        # Calculate column width and number of items per row
        max_width = 4  # Number of items per row
        col_width = max(len(name) for name in contents) + 2

        # Print contents with proper formatting
        for i, name in enumerate(contents):
            is_dir = os.path.isdir(os.path.join(path, name))
            formatted_name = term.orange(f"{name}/") if is_dir else f"{name}"
            
            # Center the row of items
            if i % max_width == 0:
                padding = (term.width - (col_width * max_width)) // 2
                print(" " * padding, end='')
            
            kernel.println(f"{formatted_name:<{col_width}}", end='')
            
            if (i + 1) % max_width == 0:
                print()
                
        if len(contents) % max_width != 0:
            print()
            
    except Exception as e:
        kernel.printError(term.center(f"Error listing directory: {str(e)}"))

def view_file_properties(path, filename):
    try:
        file_path = os.path.join(path, filename)
        if os.path.exists(file_path):
            kernel.printInfo(term.center(f"Properties of {filename}"))
            kernel.printInfo(term.center("-" * 30))
            kernel.printInfo(term.center(f"Size: {os.path.getsize(file_path)} bytes"))
            kernel.printInfo(term.center(f"Created: {time.ctime(os.path.getctime(file_path))}"))
            kernel.printInfo(term.center(f"Modified: {time.ctime(os.path.getmtime(file_path))}"))
            kernel.printInfo(term.center(f"Accessed: {time.ctime(os.path.getatime(file_path))}"))
        else:
            kernel.printError(term.center(f"File {filename} does not exist"))
    except Exception as e:
        kernel.printError(term.center(f"Error getting file properties: {str(e)}"))

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.0.2":
            # Initialize with splash screen
            ekernel.splashScreen("ProcyonCLS File Explorer", "Version 2.0.2")
            
            current_path = os.getcwd()
            
            while True:
                # Display interface
                kernel.clrscr()
                ekernel.printHeader("File Explorer")
                print()
                
                # Show current path
                kernel.printInfo(term.center(f"Current Directory: {current_path}"))
                print()
                
                # Show directory contents
                print_directory_contents(current_path)
                print()
                
                # Display menu
                menu_items = [
                    "1. Change Directory (cd)",
                    "2. View File Properties",
                    "3. Exit"
                ]
                
                for item in menu_items:
                    kernel.println(term.center(item))
                print()

                try:
                    choice = kernel.centered_input(term, "Enter choice: ").strip()

                    if choice == "1":
                        new_dir = kernel.centered_input(term, "Enter directory name: ").strip()
                        if new_dir == "..":
                            current_path = os.path.dirname(current_path)
                        else:
                            new_path = os.path.join(current_path, new_dir)
                            if os.path.isdir(new_path):
                                current_path = os.path.abspath(new_path)
                            else:
                                kernel.printError(term.center(f"Directory '{new_dir}' does not exist"))
                                kernel.centered_input(term, "Press Enter to continue...")
                    
                    elif choice == "2":
                        filename = kernel.centered_input(term, "Enter filename: ").strip()
                        view_file_properties(current_path, filename)
                        kernel.centered_input(term, "Press Enter to continue...")
                    
                    elif choice == "3":
                        kernel.printInfo(term.center("Exiting File Explorer"))
                        break
                    
                    else:
                        kernel.printError(term.center("Invalid choice"))
                        kernel.centered_input(term, "Press Enter to continue...")

                except Exception as e:
                    kernel.printError(term.center(f"An error occurred: {str(e)}"))
                    kernel.centered_input(term, "Press Enter to continue...")

        else:
            kernel.printError(term.center("This version of File Explorer is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError(term.center("OS Scope Error"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.printWarning(term.center("\nOperation cancelled by user"))
    except Exception as e:
        kernel.printError(term.center(f"An error occurred: {str(e)}"))