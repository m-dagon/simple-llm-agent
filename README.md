Simple llm-agent in python using google gemini.

This project is a learning exercise in implementing an AI coding agent.
The AI accepts a prompt from the user to solve a problem.
The AI can only call predefined functions that are scoped to the working directory.

The AI will examine the output of functions and make progress towards a solution.
There are MAX_ITERATIONS the AI will run before the program terminates to prevent
exhausting your api key limits.

You must have a google genai api_key loaded in your environment to run the program.
GEMINI_API_KEY="YOUR_GENAI_API_KEY"

