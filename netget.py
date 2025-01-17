import kernel
import sys
import ekernel
import os
import requests
from blessed import Terminal

term = Terminal()

def download_file(url, destination):
    try:
        kernel.println(("Starting download..."))
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        downloaded = 0
        
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(block_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size:
                        progress = (downloaded / total_size) * 100
                        kernel.println((f"Download progress: {progress:.1f}%"), end='\r')
        
        kernel.printSuccess(("\nDownload completed successfully!"))
        return True
    except requests.RequestException as e:
        kernel.printError((f"Download failed: {str(e)}"))
        return False
    except Exception as e:
        kernel.printError((f"Error: {str(e)}"))
        return False

def validate_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except:
        return False

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.3.5":
            # Initialize with splash screen
            ekernel.splashScreen("ProcyonCLS NetGet", "Version 2.3.5")
            
            # Create downloads directory if not exists
            if not os.path.exists("downloads"):
                os.makedirs("downloads")
            
            while True:
                # Display menu
                kernel.clrscr()
                ekernel.printHeader("NetGet Downloader")
                print()
                
                menu_items = [
                    "1. Download File",
                    "2. View Download History",
                    "3. Exit"
                ]
                
                for item in menu_items:
                    kernel.println((item))
                print()

                try:
                    choice = int(kernel.centered_input(term, "Enter choice: "))

                    if choice == 1:
                        kernel.clrscr()
                        ekernel.printHeader("Download File")
                        print()
                        
                        url = kernel.centered_input(term, "Enter URL: ").strip()
                        if not url:
                            kernel.printError(("URL cannot be empty"))
                            continue
                            
                        if not validate_url(url):
                            kernel.printError(("Invalid or unreachable URL"))
                            continue
                        
                        filename = kernel.centered_input(term, "Enter filename with extension: ").strip()
                        if not filename:
                            kernel.printError(("Filename cannot be empty"))
                            continue
                        
                        destination = os.path.join("downloads", filename)
                        
                        if os.path.exists(destination):
                            overwrite = kernel.centered_input(term, "File exists. Overwrite? (y/n): ").lower()
                            if overwrite != 'y':
                                kernel.printWarning(("Download cancelled"))
                                continue
                        
                        if download_file(url, destination):
                            # Save to history
                            with open(os.path.join("downloads", ".history"), "a") as f:
                                f.write(f"{url} -> {filename}\n")
                    
                    elif choice == 2:
                        kernel.clrscr()
                        ekernel.printHeader("Download History")
                        print()
                        
                        history_file = os.path.join("downloads", ".history")
                        if os.path.exists(history_file):
                            with open(history_file, "r") as f:
                                history = f.readlines()
                                if history:
                                    for entry in history:
                                        kernel.println((entry.strip()))
                                else:
                                    kernel.printWarning(("No download history"))
                        else:
                            kernel.printWarning(("No download history"))
                    
                    elif choice == 3:
                        kernel.printInfo(("Exiting NetGet"))
                        break
                    
                    else:
                        kernel.printError(("Invalid choice"))
                    
                    print()
                    kernel.centered_input(term, "Press Enter to continue...")
                
                except ValueError:
                    kernel.printError(("Invalid input"))
                    print()
                    kernel.centered_input(term, "Press Enter to continue...")
                
                except KeyboardInterrupt:
                    kernel.printWarning(("\nOperation cancelled"))
                    continue
        
        else:
            kernel.printError(("This version of NetGet is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError(("OS Scope Error"))

if __name__ == "__main__":
    main()