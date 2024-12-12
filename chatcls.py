import openai
import os
from prompt_toolkit import prompt
import kernel
import sys
import ekernel
from blessed import Terminal

term = Terminal()

def generate_response(prompt_text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9,
    )
    return response.choices[0].text.strip()

def chat():
    kernel.printInfo("Type 'exit' to end the conversation.")
    openai.api_key = os.getenv(kernel.centered_input(term, "Enter your OpenAI API key: "))
    while True:
        user_input = prompt("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print(f"ChatCLS : {response}")

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] >= "2.0.3":
            ekernel.splashScreen("Procyon ChatCLS", "Version 2.0.3")
            ekernel.printHeader("ChatCLS")
            chat()
        else:
            kernel.printError("This version of market is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()
