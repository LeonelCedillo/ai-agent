# import os
# Loads Python’s OS module.
# Lets your program read or write environment variables (temporary in your process) and do other OS stuff (files, paths, commands).
# from dotenv import load_dotenv
# Imports the function load_dotenv from the python-dotenv library.
# This function knows how to read a .env file and put its key-value pairs into your program’s environment memory.

# load_dotenv()
# Actually loads the .env file from your project folder.
# After this, the keys in .env exist in your program’s temporary environment (not the OS).

# api_key = os.environ.get("GEMINI_API_KEY")
# Uses os to read the value of GEMINI_API_KEY from the program’s environment.
# Stores it in the Python variable api_key for your code to use.

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions


def main():
    load_dotenv()
    args = sys.argv[1:]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: uv run main.py "your prompt here"')
        print('Example: uv run main.py "How do I build a calculator app?"')
        sys.exit(1)
    # user_prompt = " ".join(args)
    user_prompt = args[0]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose_flag = "--verbose" in args
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client, messages, verbose_flag)


def generate_content(client, messages, verbose_flag):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    
    if verbose_flag:
        user_prompt = messages[0].parts[0].text
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        return response.text


if __name__ == "__main__":
    main()
