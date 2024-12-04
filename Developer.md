# ProcyonCLS - Command Line System

## Developing Applications for ProcyonCLS

### Introduction

Developing applications for ProcyonCLS is a simple process. ProcyonCLS is a command line system that is designed to be easy to use and easy to develop for. This document will guide you through the process of developing applications for ProcyonCLS.

### Getting Started

To get started developing applications for ProcyonCLS, you will need to have a basic understanding of the command line and how to use it. You will also need to have a basic understanding of the ProcyonCLS command line system.

### Creating a New Application

Applications for ProcyonCLS are written in Python. To create a new application, create a new Python file with a `.py` extension. This file will contain the code for your application.

#### Writing Code

ProcyonCLS provides a Kernel API and an Extended Kernel API, which you can use to interact with the command line system. You can import these APIs into your application using the following code:

```python
import sys

folder1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder1_path)

import kernel
import ekernel

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "v1.4.0":
            ekernel.splashScreen("App", "Version (String)")
            ekernel.printHeader("App")
            kernel.println("Hello, World!")
            ekernel.prettyPrint("Hello, World!")
        else:
            kernel.printError("This version of app is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()
```

The above code is a simple example of a ProcyonCLS application. It imports the Kernel API and the Extended Kernel API, and prints "Hello, World!" to the command line, both in plain text and in a pretty format.

#### Understanding the Code

* `import kernel` - This is the main kernel as well as base API provider for ProcyonCLS and extended kernel. In this code, the `println()` and `printError()` are provided by the kernel API.

* `import ekernel` - This is the extended kernel API provider for ProcyonCLS. In this code, the `prettyPrint()` is provided by the extended kernel API.

* `import sys` - This is the system module for Python. It provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

* `def main():` - This is the main function of the application. It checks the command line arguments and prints "Hello, World!" to the command line.

* `if len(sys.argv) == 2:` - This checks if there are two command line arguments.

* `if sys.argv[1] == "v1.4.0":` - This checks if the second command line argument is `v1.4.0`.

* `ekernel.splashScreen("App", "Version (String)")` - This prints the splash screen with the application name and version.

* `ekernel.printHeader("App")` - This prints the header for the application.

* `kernel.println("Hello, World!")` - This prints "Hello, World!" to the command line.

* `ekernel.prettyPrint("Hello, World!")` - This prints "Hello, World!" to the command line in a pretty format.

* `else:` - This is the else statement for the `if sys.argv[1] == "v1.4.0":` statement.

* `kernel.printError("This version of app is incompatible with current version of ProcyonCLS")` - This prints an error message to the command line.

* `else:` - This is the else statement for the `if len(sys.argv) == 2:` statement.

* `kernel.printError("OS Scope Error")` - This prints an error message to the command line.

* `if __name__ == "__main__":` - This checks if the script is being run as the main program.

* `main()` - This calls the main function.

### Running the Application

To run this application, you need to first place the application in the `apps` directory in ProcyonCLS, then type `run <yourapplication>` in ProcyonCLS prompt. For example, if your application is named `hello.py`, you would type `run hello` in the command line.

# ProcyonCLS App Market

## Uploading Your Application

To upload your application to the ProcyonCLS App Market, follow these steps:

/!\ **Note**: Before uploading your application, make sure that it is working correctly and that it follows the guidelines provided in the ProcyonCLS documentation. Also it's first come first serve in terms of naming, so make sure your application name is unique.

1. **Fork the Repository**: Fork the `ProcyonCLS-AppMarket` repository to your GitHub account.
2. **Clone the Repository**: Clone the forked repository to your local machine.
   ```sh
   git clone https://github.com/yourusername/ProcyonCLS-AppMarket.git
   cd ProcyonCLS-AppMarket
   ```
3. **Add your Application**: Add your application to the `apps` directory.
    ```sh
    cp /path/to/your/app.py apps/
    ```
4. **Commit and Push**: Commit your changes and push them to your forked repository.
    ```sh
    git add apps/app.py
    git commit -m "Add MyApp - DeveloperName - Version - Description"
    git push origin main
    ```
5. **Create a Pull Request**: Create a pull request from your forked repository to the main repository.

Once your pull request is approved, your application will be added to the ProcyonCLS App Market.

### Conclusion

This document has provided an overview of how to develop applications for ProcyonCLS. For more information on developing applications for ProcyonCLS, refer to the sample.py file in the ProcyonCLS repository.
