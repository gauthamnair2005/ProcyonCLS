import kernel
import sys
import ekernel
import time
import requests
import zipfile
import shutil
import os

owner = "gauthamnair2005"
repo = "ProcyonCLS"
current_tag_file = "tag.txt"
current_directory = os.getcwd()
db_file = "configuration.db"
protected_dirs = ["notes", "apps", "downloads"]

def getLatestReleaseTagOnly():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        response = requests.get(url)
        response.raise_for_status()
        release_info = response.json()
        latest_tag = release_info["tag_name"]
        return latest_tag
    except requests.RequestException as e:
        kernel.printError(f"Error fetching latest release: {e}")
        sys.exit(1)

def getLatestReleaseTag():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        response = requests.get(url)
        response.raise_for_status()
        release_info = response.json()
        latest_tag = release_info["tag_name"], release_info["zipball_url"]
        return latest_tag
    except requests.RequestException as e:
        kernel.printError(f"Error fetching latest release: {e}")
        sys.exit(1)

def readCurrentTag():
    if os.path.exists(current_tag_file):
        with open(current_tag_file, "r") as f:
            return f.read().strip()
    return None

def writeCurrentTag(tag):
    with open(current_tag_file, "w") as f:
        f.write(tag)

def fetchWhatsNew():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        response = requests.get(url)
        response.raise_for_status()
        release_info = response.json()
        return release_info["body"]
    except requests.RequestException as e:
        kernel.printError(f"Error fetching latest release: {e}")
        sys.exit(1)

def downloadRelease(url, dest):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except requests.RequestException as e:
        kernel.printError(f"Error downloading release: {e}")
        sys.exit(1)

def extractRelease(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    except zipfile.BadZipFile as e:
        kernel.printError(f"Error extracting release: {e}")
        sys.exit(1)

def replaceLocalFiles(extracted_path, target_path):
    if not os.path.exists(extracted_path):
        kernel.printError(f"Extracted path does not exist: {extracted_path}")
        sys.exit(1)

    # Collect all Python files in the extracted update directory
    extracted_files = set()
    for root, _, files in os.walk(extracted_path):
        for file in files:
            if file.endswith(".py"):
                extracted_files.add(os.path.relpath(os.path.join(root, file), extracted_path))

    # Collect all Python files in the current directory
    current_files = set()
    for root, _, files in os.walk(target_path):
        for file in files:
            if file.endswith(".py"):
                current_files.add(os.path.relpath(os.path.join(root, file), target_path))

    # Remove deprecated Python files
    deprecated_files = current_files - extracted_files
    for file in deprecated_files:
        file_path = os.path.join(target_path, file)
        if os.path.exists(file_path):
            os.remove(file_path)
            kernel.printInfo(f" ● Removed deprecated file: {file_path}")

    # Replace or add new files from the extracted update directory
    for root, dirs, files in os.walk(extracted_path):
        relative_path = os.path.relpath(root, extracted_path)
        target_dir = os.path.join(target_path, relative_path)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_dir, file)

            if os.path.basename(target_file) == db_file:
                continue

            shutil.copy2(source_file, target_file)

        for dir in dirs:
            source_dir = os.path.join(root, dir)
            target_dir = os.path.join(target_path, relative_path, dir)

            if os.path.basename(target_dir) in protected_dirs:
                continue

            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)

            shutil.copytree(source_dir, target_dir)


def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] != None:
            ekernel.splashScreen("ProcyonCLS Updater", "Version 1.2.0")
            ekernel.printHeader("ProcyonCLS Updater")
            current_tag = readCurrentTag()
            kernel.printInfo(f"Current version: {current_tag}")
            kernel.println("Checking for updates...")
            time.sleep(2)
            latest_tag, zip_url = getLatestReleaseTag()
            if latest_tag > current_tag:
                kernel.printInfo(f"Update available: {current_tag} -> {latest_tag}")
                kernel.println(fetchWhatsNew())
                confirm = input("Do you want to update? (y/n) : ").strip()
                if confirm.lower() != "y":
                    kernel.printWarning("Update cancelled by user")
                elif confirm.lower() == "y":
                    kernel.printInfo("Updating ProcyonCLS...")
                    zip_path = os.path.join(current_directory, "latest_release.zip")
                    temp_extract_path = os.path.join(current_directory, "temp")
                    kernel.println("● Downloading update..")
                    downloadRelease(zip_url, zip_path)
                    kernel.println("● Extracting update..")
                    extractRelease(zip_path, temp_extract_path)

                    extracted_folder_name = None
                    for item in os.listdir(temp_extract_path):
                        if os.path.isdir(os.path.join(temp_extract_path, item)):
                            extracted_folder_name = item
                            break

                    if extracted_folder_name:
                        extracted_path = os.path.join(temp_extract_path, extracted_folder_name)
                        kernel.println("● Updating files...")
                        replaceLocalFiles(extracted_path, current_directory)
                        kernel.println("● Writing new tag..")
                        writeCurrentTag(latest_tag)
                        kernel.println("● Cleaning up..")
                        shutil.rmtree("temp")
                        os.remove("latest_release.zip")
                        kernel.printSuccess("Update completed successfully!")
                        time.sleep(1)
                        kernel.reboot()
                else:
                    kernel.printError("No extracted folder found.")
                shutil.rmtree(temp_extract_path)
                os.remove(zip_path)
            elif latest_tag < current_tag:
                kernel.printWarning("You're using version newer than version published, make sure you obtained current version from trusted sources")
            else:
                kernel.printSuccess("You're up to date!")
                os.execv(sys.executable, ['python3', 'shell.py', '1.2.0'])
        else:
            kernel.printError("This version of updater is incompatible with the current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.bsod("0x0005", "User interrupted execution")
    except Exception as e:
        kernel.bsod("0x0006", f"Error : {e}")