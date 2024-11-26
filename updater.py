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

def getLatestReleaseTag():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        response = requests.get(url)
        response.raise_for_status()
        release_info = response.json()
        latest_tag = release_info["tag_name"], release_info["zipball_url"]
        return latest_tag
    except:
        kernel.printError("Server unreachable..!")
        exit(1)

def readCurrentTag():
    if os.path.exists(current_tag_file):
        with open(current_tag_file, "r") as f:
            return f.read().strip()
    return None

def writeCurrentTag(tag):
    with open(current_tag_file, "w") as f:
        f.write(tag)

def downloadAndExtractRepo(url, extractTo):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        zip_filename = "update.zip"
        with open(zip_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.wrtie(chunk)
        with zipfile.ZipFile(zip_filename, "r") as zip_ref:
            zip_ref.extractall(extractTo)
        os.remove(zip_filename)
    except:
        kernel.printError("Error downloading update..!")
        exit(1)

def replaceLocalFiles(src_dir, dest_dir):
    for item in os.listdir(dest_dir):
        item_path = os.path.join(dest_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        shutil.move(item_path, dest_dir)

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "KRNL_0.5C3":
            ekernel.splashScreen("ProcyonCLS Updater", "Version 0.5C3 Munnar")
            ekernel.printHeader("ProcyonCLS Updater")
            latest_tag, zip_url = getLatestReleaseTag()
            current_tag = readCurrentTag()
            if latest_tag != current_tag:
                kernel.printWarning(f"Update available : {current_tag} -> {latest_tag}")
                temp_dir = os.path.join(current_directory, "temp")
                downloadAndExtractRepo(zip_url, temp_dir)
                extracted_folder = os.path.join(temp_dir, os.listdir(temp_dir)[0])
                replaceLocalFiles(extracted_folder, current_directory)
                writeCurrentTag(latest_tag)
                shutil.rmtree(temp_dir)
                kernel.printSuccess("Update successful, please reboot ProcyonCLS")
            else:
                kernel.printSuccess("You're up to date.!")
        else:
            kernel.printError("This version of updater is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()