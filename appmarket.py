import kernel
import sys
import ekernel
import os
import requests
from blessed import Terminal

term = Terminal()

GITHUB_REPO = "https://api.github.com/repos/gauthamnair2005/ProcyonCLS-AppMarket/contents/apps"
GITHUB_APP_UPDATE_TAG_REPO = "https://api.github.com/repos/gauthamnair2005/ProcyonCLS-App-Updater/contents/"

if not os.path.exists("apps"):
    os.makedirs("apps")

def fetch_apps():
    try:
        response = requests.get(GITHUB_REPO)
        response.raise_for_status()
        apps = response.json()
        return [app['name'] for app in apps if app['type'] == 'file' and app['name'].endswith('.py')]
    except requests.RequestException as e:
        kernel.printError(f"Error fetching apps: {e}!")
        return []

def fetch_app_version(app_name):
    try:
        appTag = app_name.split(".")[0] + ".txt"
        appTagUrl = f"{GITHUB_APP_UPDATE_TAG_REPO}/{appTag}"
        response = requests.get(appTagUrl)
        response.raise_for_status()
        appTagContent = response.json()
        return requests.get(appTagContent['download_url']).text.strip()
    except requests.RequestException as e:
        kernel.printError(f"Error fetching app version: {e}!")
        return None

def get_local_app_version(app_path):
    try:
        with open(app_path, 'r') as f:
            for line in f:
                if line.startswith("__version__"):
                    return line.split("=")[1].strip().strip('"').strip("'")
        return None
    except OSError as e:
        kernel.printError(f"Error reading local app version: {e}")
        return None

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.0.3":
            # Initialize with splash screen
            ekernel.splashScreen("ProcyonCLS AppMarket", "Version 2.0.3")
            
            while True:
                # Display menu
                kernel.clrscr()
                ekernel.printHeader("AppMarket")
                kernel.printInfo(term.center("Welcome to ProcyonCLS AppMarket"))
                print()
                menu_items = [
                    "1. Browse Apps",
                    "2. Update Apps", 
                    "3. Uninstall Apps",
                    "4. Exit"
                ]
                for item in menu_items:
                    print(term.center(item))
                print()

                try:
                    kernel.println(term.center("Enter choice:"))
                    choice = int(kernel.centered_input(term))

                    if choice == 1:
                        kernel.clrscr()
                        ekernel.printHeader("Browse Apps")
                        apps = fetch_apps()
                        if not apps:
                            kernel.printError(term.center("Internet connection not available"))
                        else:
                            kernel.println(term.center("Available Apps:"))
                            print()
                            for i, app in enumerate(apps):
                                appNoExtension = app.split(".")[0]
                                print(term.center(f"{i + 1}. {appNoExtension}"))
                            
                            try:
                                print()
                                kernel.println(term.center("Enter app number to install:"))
                                app_num = int(kernel.centered_input(term))
                                if 1 <= app_num <= len(apps):
                                    app_name = apps[app_num - 1]
                                    app_url = f"{GITHUB_REPO}/{app_name}"
                                    response = requests.get(app_url)
                                    response.raise_for_status()
                                    app_content = response.json()
                                    appInstallLoc = os.path.join("apps", app_name)
                                    
                                    # Show progress
                                    kernel.printInfo(term.center("Downloading..."))
                                    with open(appInstallLoc, 'w') as f:
                                        f.write(requests.get(app_content['download_url']).text)
                                    kernel.printSuccess(term.center(f"App {app_name} installed successfully"))
                                else:
                                    kernel.printError(term.center("Invalid selection"))
                            except ValueError:
                                kernel.printError(term.center("Invalid input. Please enter a number."))

                    elif choice == 2:
                        kernel.clrscr()
                        ekernel.printHeader("Update Apps")
                        appInstalledList = [app for app in os.listdir("apps") if app.endswith('.py')]
                        
                        if not appInstalledList:
                            kernel.printError(term.center("No apps installed"))
                        else:
                            for i, app in enumerate(appInstalledList):
                                print(term.center(f"{i + 1}. {app}"))
                                appWithLoc = os.path.join("apps", app)
                                local_version = get_local_app_version(appWithLoc)
                                server_version = fetch_app_version(app)
                                
                                if local_version and server_version:
                                    if local_version == server_version:
                                        kernel.printSuccess(term.center(f"App {app} is up to date"))
                                    else:
                                        kernel.printWarning(term.center(f"Update available for {app}"))
                                        kernel.println(term.center("Do you want to update? (y/n)"))
                                        if kernel.centered_input(term).lower() == 'y':
                                            app_url = f"{GITHUB_REPO}/{app}"
                                            response = requests.get(app_url)
                                            response.raise_for_status()
                                            app_content = response.json()
                                            with open(appWithLoc, 'w') as f:
                                                f.write(requests.get(app_content['download_url']).text)
                                            kernel.printSuccess(term.center(f"App {app} updated successfully"))
                                else:
                                    kernel.printError(term.center(f"Could not determine version for {app}"))

                    elif choice == 3:
                        kernel.clrscr()
                        ekernel.printHeader("Uninstall Apps")
                        appInstalledList = [app for app in os.listdir("apps") if app.endswith('.py')]
                        
                        if not appInstalledList:
                            kernel.printError(term.center("No apps installed"))
                        else:
                            kernel.println(term.center("Installed Apps:"))
                            print()
                            for i, app in enumerate(appInstalledList):
                                print(term.center(f"{i + 1}. {app}"))
                            
                            try:
                                print()
                                kernel.println(term.center("Enter app number to uninstall:"))
                                app_num = int(kernel.centered_input(term))
                                if 1 <= app_num <= len(appInstalledList):
                                    app_name = appInstalledList[app_num - 1]
                                    os.remove(os.path.join("apps", app_name))
                                    kernel.printSuccess(term.center(f"App {app_name} uninstalled successfully"))
                                else:
                                    kernel.printError(term.center("Invalid selection"))
                            except ValueError:
                                kernel.printError(term.center("Invalid input. Please enter a number."))

                    elif choice == 4:
                        kernel.printInfo(term.center("Exiting AppMarket"))
                        break

                    else:
                        kernel.printError(term.center("Invalid choice"))
                    kernel.println(term.center("\nPress Enter to continue..."))
                    kernel.centered_input(term)

                except ValueError:
                    kernel.printError(term.center("Invalid input"))
                    kernel.println(term.center("\nPress Enter to continue..."))
                    kernel.centered_input(term)

        else:
            kernel.printError("This version of market is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()