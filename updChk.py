import kernel
import sys
import ekernel
import time
import requests
import zipfile
import shutil
import os
from blessed import Terminal
import updater

term = Terminal()

# Constants
OWNER = "gauthamnair2005"
REPO = "ProcyonCLS"
CURRENT_TAG_FILE = "tag.txt"

def check_for_updates():
    curTag = updater.read_current_tag()
    latestTag, url, description  = updater.get_latest_release()
    if curTag is None or latestTag is None:
        kernel.println(("Error fetching release information!"))
        return
    elif curTag < latestTag:
        kernel.println(term.green(f"New update available! Current version: {curTag}, Latest version: {latestTag}"))
        for line in description.split('\n'):
                kernel.println((line))
        print()
        confirm = kernel.centered_input(term, "Do you want to update now? (y/n) : ")
        if confirm == "y":
            os.execv(sys.executable, ['python3', 'updater.py', '2.2.0'])
        else:
            kernel.printError(("Update cancelled!"))
    elif curTag > latestTag:
        kernel.printWarning(("Current version is greater than latest version!"))
    else:
        kernel.printSuccess(("ProcyonCLS is up to date!"))

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.2.0":
            ekernel.splashScreen("ProcyonCLS Update Checker", "Version 2.2.0")
            ekernel.printHeader("Update Checker")
            check_for_updates()
        else:
            kernel.printError(("This version of Update Checker is incompatible with current version of ProcyonCLS"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.bsod("0x0005", "User interrupted execution")
    except Exception as e:
        kernel.bsod("0x0006", f"Error: {e}")