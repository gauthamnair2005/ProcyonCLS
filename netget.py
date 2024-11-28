import kernel
import sys
import ekernel

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9E":
            ekernel.splashScreen("ProcyonCLS NetGet", "Version 0.9E")
            ekernel.printHeader("NetGet Downloader")
            url = input("Enter URL : ").strip()
            destAndFileExtension = input("Enter destination and filename to save with extension : ").strip()
            ekernel.urlDownloader(url, destAndFileExtension)
        else:
            kernel.printError("This version of NetGet is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()