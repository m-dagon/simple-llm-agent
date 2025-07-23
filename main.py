import sys
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)


def main():
    if not len(sys.argv) >= 2:
        exit(1)

    user_prompt = str(sys.argv[1])
    verbose_flag = len(sys.argv) >= 3 and sys.argv[2] == "--verbose"
    gemini_model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=gemini_model,
        contents=messages,
    )
    
    if verbose_flag:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(response.text)



if __name__ == "__main__":
    main()
