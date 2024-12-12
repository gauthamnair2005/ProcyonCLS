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
        if sys.argv[1] >= "2.0.3":
            clrscr()
            print(term.bold("Procyon Neo Kernel 2.0.3"))
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
                os.system("python3 shell.py 2.0.3")
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
            print(term.red(f" Reported {sys.argv[1]} as opposed to 2.0.3"))
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
    return "2.0.3"

def getBuild():
    return "2024.12.12.1944"

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
    return "Developer Preview 12"

def printError(param, end="\n"):
    print(term.red(param), end=end)

def printWarning(param, end="\n"):
    print(term.yellow(param), end=end)

def printSuccess(param, end="\n"):
    print(term.green(param), end=end)

def printInfo(param, end="\n"):
    print(term.blue(param), end=end)

def println(param="", end="\n", flush=False):
    print(param, end=end, flush=flush)

def centered_input(term, prompt=""):
    width = term.width
    if prompt:
        println(term.center(prompt))
    input_width = 30
    center_pos = (width - input_width) // 2
    print('\r' + ' ' * center_pos, end='', flush=True)
    return input()

def bsod(error, msg):
    clrscr()
    print(term.on_blue(term.white(" " * 1000000000)))
    clrscr()
    print(term.on_blue(term.white("Kernel Panic : System Failure")))
    print(term.on_blue(term.white("Technical Details : ")))
    print(term.on_blue(term.white(f" Error Code : {error}")))
    print(term.on_blue(term.white(f" Error Description : {msg}")))
    print(term.normal)
    time.sleep(5)
    sys.exit(1)

def printYellow(param):
    print(term.yellow(param))

def printGreen(param):
    print(term.green(param))

def printBlue(param):
    print(term.blue(param))

def printCyan(param):
    print(term.cyan(param))

def printMagenta(param):
    print(term.magenta(param))

def printRed(param):
    print(term.red(param))

def printWhite(param):
    print(term.white(param))

def printBlack(param):
    print(term.black(param))

def printBold(param):
    print(term.bold(param))

def printUnderline(param):
    print(term.underline(param))

def printInverted(param):
    print(term.reverse(param))

def printStrikethrough(param):
    print(term.strikethrough(param))

def printReset(param):
    print(term.normal(param))

def printItalic(param):
    print(term.italic(param))

def printOverline(param):
    print(term.overline(param))

def printBlink(param):
    print(term.blink(param))

def printDoubleUnderline(param):
    print(term.double_underline(param))

def printDoubleStrikethrough(param):
    print(term.double_strikethrough(param))

def printDoubleOverline(param):
    print(term.double_overline(param))

def printDoubleBlink(param):
    print(term.double_blink(param))

def printFramed(param):
    print(term.framed(param))

def printEncircled(param):
    print(term.encircled(param))

def printRainbow(param):
    print(term.color_rgb(255, 0, 0)(param))

def callApplication(app, isAdmin=False):
    appResolved = f"python3 {app}.py 2.0.3 {isAdmin}"
    os.system(appResolved)

def callApplication3P(app, isAdmin=False):
    appResolved = f"python3 apps/{app}.py 2.0.3 {isAdmin}"
    os.system(appResolved)