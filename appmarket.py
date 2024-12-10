import kernel
import sys
import ekernel
import os
import requests

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
        if sys.argv[1] >= "1.9.0":
            ekernel.splashScreen("ProcyonCLS AppMarket", "Version 1.9.0")
            ekernel.printHeader("AppMarket")
            kernel.printInfo("Welcome to ProcyonCLS AppMarket")
            kernel.println("1. Browse Apps")
            kernel.println("2. Update Apps")
            kernel.println("3. Uninstall Apps")
            kernel.println("4. Exit")
            while True:
                try:
                    choice = int(input("Enter choice : "))
                    if choice == 1:
                        apps = fetch_apps()
                        if not apps:
                            kernel.printError("Internet connection not available")
                        else:
                            kernel.println("Available Apps:")
                            for i, app in enumerate(apps):
                                appNoExtension = app.split(".")[0]
                                kernel.println(f" {i + 1}. {appNoExtension}")
                            try:
                                app_num = int(input("Enter the app number to install : "))
                                if app_num < 1 or app_num > len(apps):
                                    kernel.printError("Invalid input")
                                else:
                                    app_name = apps[app_num - 1]
                                    app_url = f"{GITHUB_REPO}/{app_name}"
                                    response = requests.get(app_url)
                                    response.raise_for_status()
                                    app_content = response.json()
                                    appInstallLoc = os.path.join("apps", app_name)
                                    with open(appInstallLoc, 'w') as f:
                                        f.write(requests.get(app_content['download_url']).text)
                                    kernel.printSuccess(f"App {app_name} installed successfully")
                            except ValueError:
                                kernel.printError("Invalid input. Please enter a number.")
                    elif choice == 2:
                        appInstalledList = os.listdir("apps")
                        appInstalledList = [app for app in appInstalledList if app.endswith('.py')]
                        if not appInstalledList:
                            kernel.printError("No apps installed")
                        else:
                            kernel.println("Installed Apps:")
                            for i, app in enumerate(appInstalledList):
                                kernel.println(f" {i + 1}. {app}")
                                appWithLoc = os.path.join("apps", app)
                                local_version = get_local_app_version(appWithLoc)
                                server_version = fetch_app_version(app)
                                if local_version and server_version:
                                    if local_version == server_version:
                                        kernel.printSuccess(f"App {app} is up to date")
                                    else:
                                        kernel.printError(f"App {app} update available")
                                        update = input("Do you want to update the app? (y/n) : ").lower()
                                        if update == "y":
                                            app_url = f"{GITHUB_REPO}/{app}"
                                            response = requests.get(app_url)
                                            response.raise_for_status()
                                            app_content = response.json()
                                            with open(appWithLoc, 'w') as f:
                                                f.write(requests.get(app_content['download_url']).text)
                                            kernel.printSuccess(f"App {app} updated successfully")
                                        elif update == "n":
                                            kernel.printError("App not updated")
                                        else:
                                            kernel.printError("Invalid input")
                                else:
                                    kernel.printError(f"Could not determine version for app {app}")
                    elif choice == 3:
                        appInstalledList = os.listdir("apps")
                        appInstalledList = [app for app in appInstalledList if app.endswith('.py')]
                        if not appInstalledList:
                            kernel.printError("No apps installed")
                        else:
                            kernel.println("Installed Apps:")
                            for i, app in enumerate(appInstalledList):
                                kernel.println(f" {i + 1}. {app}")
                            try:
                                app_num = int(input("Enter the app number to uninstall : "))
                                if app_num < 1 or app_num > len(appInstalledList):
                                    kernel.printError("Invalid input")
                                else:
                                    app_name = appInstalledList[app_num - 1]
                                    os.remove(os.path.join("apps", app_name))
                                    kernel.printSuccess(f"App {app_name} uninstalled successfully")
                            except ValueError:
                                kernel.printError("Invalid input. Please enter a number.")
                            except OSError as e:
                                kernel.printError(f"Error uninstalling app: {e}")
                    elif choice == 4:
                        kernel.printInfo("Exiting AppMarket")
                        break
                    else:
                        kernel.printError("Invalid choice. Please enter a number between 1 and 4.")
                except ValueError:
                    kernel.printError("Invalid input. Please enter a number.")
        else:
            kernel.printError("This version of market is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()