import kernel
import sys
import ekernel
import time
import requests
import zipfile
import shutil
import os
from blessed import Terminal

term = Terminal()

# Constants
OWNER = "gauthamnair2005"
REPO = "ProcyonCLS"
CURRENT_TAG_FILE = "tag.txt"
CURRENT_DIRECTORY = os.getcwd()
DB_FILE = "configuration.db"
PROTECTED_DIRS_FILE = "protected_dirs.txt"

def read_protected_dirs(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def get_latest_release():
    try:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
        response = requests.get(url)
        response.raise_for_status()
        release_info = response.json()
        return release_info["tag_name"], release_info["zipball_url"], release_info["body"]
    except requests.RequestException as e:
        kernel.printError(term.center(f"Error fetching latest release: {e}"))
        return None, None, None

def read_current_tag():
    if os.path.exists(CURRENT_TAG_FILE):
        with open(CURRENT_TAG_FILE, "r") as f:
            return f.read().strip()
    return None

def write_current_tag(tag):
    with open(CURRENT_TAG_FILE, "w") as f:
        f.write(tag)

def download_release(url, dest):
    try:
        kernel.println(term.center(" ● Downloading update..."))
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except requests.RequestException as e:
        kernel.printError(term.center(f"Error downloading release: {e}"))
        return False

def extract_release(zip_path, extract_to):
    try:
        kernel.println(term.center(" ● Extracting update..."))
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return True
    except zipfile.BadZipFile as e:
        kernel.printError(term.center(f"Error extracting release: {e}"))
        return False

def replace_local_files(extracted_path, target_path):
    if not os.path.exists(extracted_path):
        kernel.printError(term.center(f"Extracted path does not exist: {extracted_path}"))
        return False
    
    try:
        kernel.println(term.center(" ● Updating files..."))
        protected_dirs = read_protected_dirs(PROTECTED_DIRS_FILE)
        
        # Remove old Python files
        for item in os.listdir():
            if item.endswith(".py") and item not in protected_dirs:
                os.remove(item)
        
        # Copy new files
        for item in os.listdir(extracted_path):
            if item == "protected_dirs.txt" or item in protected_dirs:
                continue
            source = os.path.join(extracted_path, item)
            destination = os.path.join(target_path, item)
            
            if os.path.isdir(source):
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(source, destination)
        return True
    except Exception as e:
        kernel.printError(term.center(f"Error replacing files: {e}"))
        return False

def main():
    if len(sys.argv) >= 2 and sys.argv[1] >= "2.0.1":
        # Initialize with splash screen
        ekernel.splashScreen("ProcyonCLS Updater", "Version 2.0.1")
        
        # Display header
        kernel.clrscr()
        ekernel.printHeader("System Updater")
        
        # Display current version
        current_tag = read_current_tag()
        kernel.printInfo(term.center(f"Current version: {current_tag}"))
        print()
        
        # Check for updates
        kernel.println(term.center("Checking for updates..."))
        print()
        time.sleep(1)
        
        latest_tag, zip_url, whats_new = get_latest_release()
        if not latest_tag:
            return
            
        if latest_tag > current_tag:
            kernel.printInfo(term.center(f"Update available: {latest_tag}"))
            print()
            kernel.println(term.center("What's New:"))
            for line in whats_new.split('\n'):
                kernel.println(term.center(line))
            print()
            
            confirm = kernel.centered_input(term, f"Do you want to update? {current_tag} -> {latest_tag} (y/n): ")
            if confirm.lower() != "y":
                kernel.printWarning(term.center("Update cancelled"))
                return
                
            # Perform update
            zip_path = os.path.join(CURRENT_DIRECTORY, "latest_release.zip")
            temp_extract_path = os.path.join(CURRENT_DIRECTORY, "temp")
            
            try:
                # Download and extract
                if not download_release(zip_url, zip_path):
                    return
                if not extract_release(zip_path, temp_extract_path):
                    return
                
                # Find extracted folder
                extracted_folder = next((item for item in os.listdir(temp_extract_path) 
                                      if os.path.isdir(os.path.join(temp_extract_path, item))), None)
                if not extracted_folder:
                    kernel.printError(term.center("No extracted folder found"))
                    return
                
                extracted_path = os.path.join(temp_extract_path, extracted_folder)
                
                # Replace files and cleanup
                if not replace_local_files(extracted_path, CURRENT_DIRECTORY):
                    return
                    
                kernel.println(term.center(" ● Writing new tag..."))
                write_current_tag(latest_tag)
                
                kernel.println(term.center(" ● Cleaning up..."))
                shutil.rmtree(temp_extract_path)
                os.remove(zip_path)
                
                kernel.printSuccess(term.center("Update completed successfully!"))
                time.sleep(1)
                kernel.reboot()
                
            except Exception as e:
                kernel.printError(term.center(f"Update failed: {e}"))
                if os.path.exists(temp_extract_path):
                    shutil.rmtree(temp_extract_path)
                if os.path.exists(zip_path):
                    os.remove(zip_path)
                    
        elif latest_tag < current_tag:
            kernel.printWarning(term.center("You're using a newer version than published"))
            kernel.printWarning(term.center("Make sure you obtained current version from trusted sources"))
        else:
            kernel.printSuccess(term.center("You're up to date!"))
            os.execv(sys.executable, ['python3', 'shell.py', '2.0.1'])
    else:
        kernel.printError(term.center("This version of updater is incompatible with ProcyonCLS"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.bsod("0x0005", "User interrupted execution")
    except Exception as e:
        kernel.bsod("0x0006", f"Error: {e}")