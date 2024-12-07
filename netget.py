import kernel
import sys
import ekernel
import os

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "1.6.1":
            ekernel.splashScreen("ProcyonCLS NetGet", "Version 1.6.1")
            ekernel.printHeader("NetGet Downloader")
            if not os.path.exists("downloads"):
                os.mkdir("downloads")
            url = input("Enter URL : ").strip()
            destAndFileExtension = input("Enter destination and filename to save with extension : ").strip()
            ekernel.urlDownloader(url, destAndFileExtension)
        else:
            kernel.printError("This version of NetGet is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()