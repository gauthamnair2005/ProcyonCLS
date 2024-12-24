import kernel
import sys
import ekernel
import operator
from blessed import Terminal
from simpleeval import SimpleEval

term = Terminal()

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.1.0":
            # Initialize with splash screen
            ekernel.splashScreen("ProcyonCLS Evaluator", "Version 2.1.0")
            
            while True:
                # Display interface
                kernel.clrscr()
                ekernel.printHeader("Evaluator")
                print()
                
                # Show help text
                kernel.printInfo(("Type 'exit' to quit"))
                print()
                
                try:
                    # Get expression
                    expression = kernel.centered_input(term, "Expression ↓ ").strip()
                    
                    if expression.lower() == 'exit':
                        kernel.printInfo(("Exiting Evaluator"))
                        break
                    
                    if not expression:
                        kernel.printWarning(("Please enter an expression"))
                        continue
                    
                    # Additional input validation
                    kernel.printSuccess((f"Result: {eval(expression)}"))
                    
                except ValueError as e:
                    kernel.printError((str(e)))
                except Exception as e:
                    kernel.printError((f"Error: {str(e)}"))
                
                print()
                kernel.centered_input(term, "Press Enter to continue...")
                
        else:
            kernel.printError(("This version of evaluator is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError(("OS Scope Error"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.printWarning(("\nOperation cancelled by user"))
    except Exception as e:
        kernel.printError((f"An error occurred: {str(e)}"))