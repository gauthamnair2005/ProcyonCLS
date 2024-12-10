# Kernel for Procyon Command Line System

import sys
import os
import time
from datetime import datetime

try:
    def main():
        if len(sys.argv) == 2:
            if sys.argv[1] >= "1.9.0":
                os.system("cls" if sys.platform == "win32" else "clear")
                print("Procyon Neo Kernel 1.9.0")
                print("..............")
                print("Loading Kernel modules...")
                time.sleep(0.1)
                print("FDD", end=" ", flush=True)
                time.sleep(0.2)
                print("\033[92m[Done]\033[0m")
                print("FND", end=" ", flush=True)
                time.sleep(0.2)
                print("\033[92m[Done]\033[0m")
                print("FODBCD", end=" ", flush=True)
                time.sleep(0.2)
                print("\033[92m[Done]\033[0m")
                print("Extended Kernel", end=" ", flush=True)
                if os.path.exists("ekernel.py"):
                    time.sleep(0.2)
                    print("\033[92m[Done]\033[0m")
                else:
                    print("\033[91m[Failed]\033[0m")
                    sys.exit(1)
                print("APIs", end=" ", flush=True)
                time.sleep(0.2)
                print("\033[92m[Done]\033[0m")
                print("Kernel Loaded Successfully!")
                print("Booting ProcyonCLS...")
                time.sleep(0.2)
                if os.path.exists("shell.py"):
                    os.system("python3 shell.py 1.9.0")
                else:
                    os.system("cls" if sys.platform == "win32" else "clear")
                    print("Kernel Panic : OS error")
                    print("Technical Details : ")
                    print(" Error Code : 0x0003")
                    print(" Error Description : OS not linked to Kernel")
                    sys.exit(1)
            else:
                os.system("cls" if sys.platform == "win32" else "clear")
                print("Kernel Panic : Bootloader error")
                print("Technical Details : ")
                print(" Error Code : 0x0001")
                print(" Error Description : Incompatible version reported by Bootloader")
                print(f" Reported {sys.argv[1]} as opposed to 1.9.0")
                sys.exit(1)
        else:
            os.system("cls" if sys.platform == "win32" else "clear")
            print("Kernel Panic : Bootloader error")
            print("Technical Details : ")
            print(" Error Code : 0x0002")
            print(" Error Description : Kernel invoked without Bootloader")
            sys.exit(1)

    if __name__ == "__main__":
        main()

except:
    sys.exit(1)


# Kernel APIs

def shutDown():
    println("Shutting down...")
    return sys.exit(0)

def reboot():
    println("Rebooting...")
    os.execv(sys.executable, ['python3', 'start.py'])

def getVersion():
    return "1.9.0"

def getBuild():
    return "2024.12.10.1713"

def getAuthor():
    return "Gautham Nair"

def getCompany():
    return "Procyonis Computing"

def getLicense():
    return "GNU GPL v3.0"

def getKernelName():
    return "Procyon Neo"

def getCodeName():
    return "Munnar"

def getReleaseName():
    return "ProcyonCLS 2025"

def getRelease():
    return "Developer Preview 10"

def printError(param, end = "\n"):
    print(f"\033[91m{param}\033[0m", end = end)

def printWarning(param, end = "\n"):
    print(f"\033[93m{param}\033[0m", end = end)

def printSuccess(param, end = "\n"):
    print(f"\033[92m{param}\033[0m", end = end)

def printInfo(param, end = "\n"):
    print(f"\033[94m{param}\033[0m", end = end)

def println(param, end = "\n"):
    print(param, end = end)

def clrscr():
    os.system("cls" if sys.platform == "win32" else "clear")

def bsod(error, msg):
    os.system("cls" if sys.platform == "win32" else "clear")
    print("\033[44m\033[97m")
    print(""*1000000000)
    os.system("cls" if sys.platform == "win32" else "clear")        
    print("Kernel Panic : System Failure")
    print("Technical Details : ")
    print(f" Error Code : {error}")
    print(f" Error Description : {msg}")
    print("\033[0m")
    time.sleep(5)
    sys.exit(1)

def printYellow(param):
    print(f"\033[93m{param}\033[0m")

def printGreen(param):
    print(f"\033[92m{param}\033[0m")

def printBlue(param):
    print(f"\033[94m{param}\033[0m")

def printCyan(param):
    print(f"\033[96m{param}\033[0m")

def printMagenta(param):
    print(f"\033[95m{param}\033[0m")

def printRed(param):
    print(f"\033[91m{param}\033[0m")

def printWhite(param):
    print(f"\033[97m{param}\033[0m")

def printBlack(param):
    print(f"\033[30m{param}\033[0m")

def printBold(param):
    print(f"\033[1m{param}\033[0m")

def printUnderline(param):
    print(f"\033[4m{param}\033[0m")

def printInverted(param):
    print(f"\033[7m{param}\033[0m")

def printStrikethrough(param):
    print(f"\033[9m{param}\033[0m")

def printReset(param):
    print(f"\033[0m{param}\033[0m")

def printYellow(param):
    print(f"\033[93m{param}\033[0m")

def printItalic(param):
    print(f"\033[3m{param}\033[0m")

def printOverline(param):
    print(f"\033[53m{param}\033[0m")

def printBlink(param):
    print(f"\033[5m{param}\033[0m")

def printDoubleUnderline(param):
    print(f"\033[21m{param}\033[0m")

def printDoubleStrikethrough(param):
    print(f"\033[29m{param}\033[0m")

def printDoubleOverline(param):
    print(f"\033[55m{param}\033[0m")

def printDoubleBlink(param):
    print(f"\033[6m{param}\033[0m")

def printFramed(param):
    print(f"\033[51m{param}\033[0m")

def printEncircled(param):
    print(f"\033[52m{param}\033[0m")

def printRainbow(param):
    print(f"\033[38;2;255;0;0m{param}\033[0m")

def callApplication(app, isAdmin = False):
    appResolved = "python3 " + app + ".py 1.9.0 " + str(isAdmin)
    os.system(appResolved)

def callApplication3P(app, isAdmin = False):
    appResolved = "python3 apps/" + app + ".py 1.9.0 " + str(isAdmin)
    os.system(appResolved)