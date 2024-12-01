import kernel
import sys
import ekernel

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9J":
            ekernel.splashScreen("ProcyonCLS Evaluator", "Version 0.9J")
            ekernel.printHeader("Evaluator")
            kernel.println("Type expression or 'exit' to quit")
            while True:
                try:
                    expression = input("Evaluator>  ")
                    if expression == "exit":
                        break
                    else:
                        kernel.println(eval(expression))
                except:
                    kernel.printError("Invalid expression")
        else:
            kernel.printError("This version of evaluator is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()