# ProcyonCLS Extended Kernel

import time
import kernel
import getpass
import hashlib
import pyfiglet
import sqlite3
import requests
import requests
from bs4 import BeautifulSoup


def urlDownloader(url, destAndExtensionOfFile):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(destAndExtensionOfFile, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except:
        kernel.printError(f"Error downloading file from {url}, please check the URL or your internet and try again!")

def splashScreen(name, ver):
    kernel.clrscr()
    prettyPrint(name)
    kernel.println(ver)
    time.sleep(3)
    kernel.clrscr()

def prettyPrint(param):
    print("\033[0;35m" + pyfiglet.figlet_format(param) + "\033[0m")

def printHeader(header):
    color = "\033[0;35m"
    reset = "\033[0m"
    kernel.printBold(f"{color}▓▒ {header} ▒░{reset}")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def securePass(display):
    return hash_password(getpass.getpass(display))

def admin(username, display = "Enter Password : "):
    password = getpass.getpass(display)
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT password FROM users WHERE username = "{username}"')
    if cursor.fetchone()[0] == password:
        return True
    else:
        return False
        
def textBrowser(url):
    try:
        if url.startswith("http://") or url.startswith("https://"):
            pass
        else:
            url = "https://" + url
        response = requests.get(url, verify=True)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        kernel.println(text)
    except:
        kernel.printError(f"Error fetching page from {url}!")