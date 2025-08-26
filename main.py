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

def main():
    if len(sys.argv) < 2: 
        print("Usage: uv run main.py <prompt>")
        sys.exit(1)
    prompt = sys.argv[1]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
