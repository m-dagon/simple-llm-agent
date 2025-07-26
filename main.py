

import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from config import MAX_ITERATIONS
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *
from functions.call_function import call_function

def main():
    if not len(sys.argv) >= 2:
        exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = str(sys.argv[1])
    verbose_flag = len(sys.argv) >= 3 and sys.argv[2] == "--verbose"
    gemini_model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )
    try:
        for i in range(0, MAX_ITERATIONS):
            if verbose_flag:
                print(f'Sending request num: {i}')
            response = client.models.generate_content(
                model=gemini_model,
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=SYSTEM_PROMPT
                )
            )

            # Update conversation message history
            for candidate in response.candidates:
                messages.append(candidate.content)
            # Print the function calls
            if verbose_flag:
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            if response.function_calls:
                for f in response.function_calls:
                    function_call_result = call_function(f, verbose_flag)
                    if not function_call_result.parts[0].function_response.response:
                        raise Exception("Error: function call did not return a response.")
                    if verbose_flag:
                        print(f"-> {function_call_result.parts[0].function_response.response}")

                    messages.append(
                        types.Content(
                            parts=function_call_result.parts,
                            role="tool")
                    )

            # Print result and end iterations
            else:
                print(response.text)
                break

    except Exception as e:
        print(f'Exception e: {e}')



if __name__ == "__main__":
    main()
