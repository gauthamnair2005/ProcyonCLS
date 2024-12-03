import kernel
import sys
import ekernel
import os
import requests

GITHUB_REPO = "https://api.github.com/repos/gauthamnair2005/ProcyonCLS-AppMarket/contents/apps"

def fetch_apps():
    try:
        response = requests.get(GITHUB_REPO)
        response.raise_for_status()
        apps = response.json()
        return [app['name'] for app in apps if app['type'] == 'file' and app['name'].endswith('.py')]
    except requests.RequestException as e:
        kernel.printError(f"Error fetching apps: {e}")
        return []

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9M":
            ekernel.splashScreen("ProcyonCLS AppMarket", "Version 0.9M")
            ekernel.printHeader("AppMarket")
            if not os.path.exists("apps"):
                os.mkdir("apps")
            kernel.println("Fetching available apps from server...")
            apps = fetch_apps()
            if apps:
                kernel.println("Available Apps:")
                for app in apps:
                    kernel.println(f"● {app.replace('.py', '')}")
            else:
                kernel.printError("No apps available or failed to fetch apps.")
        else:
            kernel.printError("This version of market is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()