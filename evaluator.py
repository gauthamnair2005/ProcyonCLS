import kernel
import sys
import ekernel
import operator
from blessed import Terminal
from simpleeval import SimpleEval

term = Terminal()

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.0.1":
            # Initialize with splash screen
            ekernel.splashScreen("ProcyonCLS Evaluator", "Version 2.0.1")
            
            while True:
                # Display interface
                kernel.clrscr()
                ekernel.printHeader("Evaluator")
                print()
                
                # Show help text
                kernel.printInfo(term.center("Type 'exit' to quit"))
                print()
                
                try:
                    # Get expression
                    expression = kernel.centered_input(term, "Expression : ").strip()
                    
                    if expression.lower() == 'exit':
                        kernel.printInfo(term.center("Exiting Evaluator"))
                        break
                    
                    if not expression:
                        kernel.printWarning(term.center("Please enter an expression"))
                        continue
                    
                    # Additional input validation
                    kernel.printSuccess(term.center(f"Result: {eval(expression)}"))
                    
                except ValueError as e:
                    kernel.printError(term.center(str(e)))
                except Exception as e:
                    kernel.printError(term.center(f"Error: {str(e)}"))
                
                print()
                kernel.centered_input(term, "Press Enter to continue...")
                
        else:
            kernel.printError(term.center("This version of evaluator is incompatible with current version of ProcyonCLS"))
    else:
        kernel.printError(term.center("OS Scope Error"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        kernel.printWarning(term.center("\nOperation cancelled by user"))
    except Exception as e:
        kernel.printError(term.center(f"An error occurred: {str(e)}"))