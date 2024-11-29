import openai
import os
from prompt_toolkit import prompt
import kernel
import sys
import ekernel

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
    print("Welcome to Procyon ChatCLS")
    print("Type 'exit' to end the conversation.")
    while True:
        user_input = prompt("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print(f"ChatCLS : {response}")

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "0.9GC2":
            ekernel.splashScreen("Procyon ChatCLS", "Version 0.9GC2")
            ekernel.printHeader("ChatCLS")
            openai.api_key = os.getenv(input("Enter your OpenAI API key: "))
            chat()
        else:
            kernel.printError("This version of market is incompatible with current version of ProcyonCLS")
    else:
        kernel.printError("OS Scope Error")

if __name__ == "__main__":
    main()
