# ProcyonCLS Extended Kernel

import time
import kernel
import getpass
import hashlib
import pyfiglet
import sqlite3
import requests
from bs4 import BeautifulSoup
from blessed import Terminal

term = Terminal()

def urlDownloader(url, destAndExtensionOfFile):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(destAndExtensionOfFile, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except:
        return f"Error downloading file from {url}, please check the URL or your internet and try again!"

def splashScreen(name, ver):
    kernel.clrscr()
    kernel.println(term.magenta(term.center(term.bold(pyfiglet.figlet_format(name)))))
    kernel.println((ver))
    time.sleep(3)
    kernel.clrscr()

def prettyPrint(param):
    kernel.println(pyfiglet.figlet_format(param))

def printHeader(header):
    kernel.println((term.magenta(f"▓▒ {header} ▒░")))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def securePass(display):
    return hash_password(getpass.getpass(display))

def admin(username, display="Enter Password : "):
    password = getpass.getpass(term.center(display))
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT password FROM users WHERE username = "{username}"')
    if cursor.fetchone()[0] == password:
        return True
    else:
        return False

def textBrowser(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        response = requests.get(url, verify=True)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text
    except:
        return f"Error fetching the site from {url}. Please check the URL and your internet connection."