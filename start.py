# Bootloader for Procyon Command Line System

import sys
import os
import time

try:
    os.system("cls" if sys.platform == "win32" else "clear")
    print("Procyon Bootloader vv1.3.0")
    print("..............")
    print("Detecting ProcyonCLS Kernel...")
    if os.path.exists("kernel.py"):
        print("Kernel found!")
        print("Booting kernel...")
        time.sleep(0.5)
        os.system("python3 kernel.py v1.3.0")
    else:
        print("Kernel not found!")
        print("Exiting...")
        time.sleep(2)
        sys.exit(1)

except:
    sys.exit(1)