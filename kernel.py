# Kernel for Procyon Command Line System

import sys
import os
import time
try:
    from blessed import Terminal
except:
    if sys.platform == "win32":
        os.system("pip install blessed")
    else:
        os.system("pip3 install blessed")

term = Terminal()

def clrscr():
    print(term.clear)

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] >= "2.3.0":
            clrscr()
            print(term.bold("Procyon Neo Kernel 2.3.0"))
            print("..............")
            print("Loading Kernel modules...")
            time.sleep(0.1)
            print("FDD", end=" ", flush=True)
            print(term.green("[Done]"))
            print("FND", end=" ", flush=True)
            time.sleep(0.2)
            print(term.green("[Done]"))
            print("FODBCD", end=" ", flush=True)
            time.sleep(0.2)
            print(term.green("[Done]"))
            print("Extended Kernel", end=" ", flush=True)
            if os.path.exists("ekernel.py"):
                time.sleep(0.2)
                print(term.green("[Done]"))
            else:
                print(term.red("[Failed]"))
                sys.exit(1)
            print("APIs", end=" ", flush=True)
            time.sleep(0.2)
            print(term.green("[Done]"))
            print("Kernel Loaded Successfully!")
            print("Booting ProcyonCLS...")
            time.sleep(0.2)
            if os.path.exists("shell.py"):
                os.system("python3 shell.py 2.3.0")
            else:
                clrscr()
                print(term.bold_red("Kernel Panic : OS error"))
                print("Technical Details : ")
                print(term.red(" Error Code : 0x0003"))
                print(term.red(" Error Description : OS not linked to Kernel"))
                sys.exit(1)
        else:
            clrscr()
            print(term.bold_red("Kernel Panic : Bootloader error"))
            print("Technical Details : ")
            print(term.red(" Error Code : 0x0001"))
            print(term.red(" Error Description : Incompatible version reported by Bootloader"))
            print(term.red(f" Reported {sys.argv[1]} as opposed to 2.3.0"))
            sys.exit(1)
    else:
        clrscr()
        print(term.bold_red("Kernel Panic : Bootloader error"))
        print("Technical Details : ")
        print(term.red(" Error Code : 0x0002"))
        print(term.red(" Error Description : Kernel invoked without Bootloader"))
        sys.exit(1)

if __name__ == "__main__":
    main()

# Kernel APIs

def shutDown():
    print("Shutting down...")
    return sys.exit(0)

def reboot():
    print("Rebooting...")
    os.execv(sys.executable, ['python3', 'start.py'])

def getVersion():
    return "2.3.0"

def getBuild():
    return "2024.12.27.1924"

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
    return "Release Preview"

def printError(param, end="\n"):
    print(term.center(term.red(param)), end=end)

def printWarning(param, end="\n"):
    print(term.center(term.yellow(param)), end=end)

def printSuccess(param, end="\n"):
    print(term.center(term.green(param)), end=end)

def printInfo(param, end="\n"):
    print(term.center(term.blue(param)), end=end)

def println(param="", end="\n", flush=False):
    print(term.center(param), end=end, flush=flush)

def centered_input(term, prompt=""):
    width = term.width
    if prompt:
        println((prompt))
    input_width = 30
    center_pos = (width - input_width) // 2
    print('\r' + ' ' * center_pos, end='', flush=True)
    return input()

def bsod(error, msg):
    clrscr()
    print(term.bold_red("Kernel Panic : Bootloader error"))
    print("Technical Details : ")
    print(term.red(f" Error Code : {error}"))
    print(term.red(f" Error Description : {msg}"))
    time.sleep(5)
    sys.exit(1)

def printYellow(param):
    print(term.center(term.yellow(param)))

def printGreen(param):
    print(term.center(term.green(param)))

def printBlue(param):
    print(term.center(term.blue(param)))

def printCyan(param):
    print(term.center(term.cyan(param)))

def printMagenta(param):
    print(term.center(term.magenta(param)))

def printRed(param):
    print(term.center(term.red(param)))

def printWhite(param):
    print(term.center(term.white(param)))

def printBlack(param):
    print(term.center(term.black(param)))

def printBold(param):
    print(term.center(term.bold(param)))

def printUnderline(param):
    print(term.center(term.underline(param)))

def printInverted(param):
    print(term.center(term.reverse(param)))

def printStrikethrough(param):
    print(term.center(term.strikethrough(param)))

def printReset(param):
    print(term.center(term.normal(param)))

def printItalic(param):
    print(term.center(term.italic(param)))

def printOverline(param):
    print(term.center(term.overline(param)))

def printBlink(param):
    print(term.center(term.blink(param)))

def printDoubleUnderline(param):
    print(term.center(term.double_underline(param)))

def printDoubleStrikethrough(param):
    print(term.center(term.double_strikethrough(param)))

def printDoubleOverline(param):
    print(term.center(term.double_overline(param)))

def printDoubleBlink(param):
    print(term.center(term.double_blink(param)))

def printFramed(param):
    print(term.center(term.framed(param)))

def printEncircled(param):
    print(term.center(term.encircled(param)))

def printRainbow(param):
    print(term.center(term.color_rgb(255, 0, 0)(param)))

def callApplication(app, isAdmin=False):
    appResolved = f"python3 {app}.py 2.3.0 {isAdmin}"
    os.system(appResolved)

def callApplication3P(app, isAdmin=False):
    appResolved = f"python3 apps/{app}.py 2.3.0 {isAdmin}"
    os.system(appResolved)