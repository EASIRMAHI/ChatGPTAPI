import openai
import os

# Retrieve API key from environment variable
APIKEY = os.getenv("APIKEY")
openai.api_key = APIKEY

# Retrieve prompt from environment variable or use a default
prompt = os.getenv("PROMPT", "Write me a script for hosting a conference on technology")

# Make the API call with the prompt
output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": prompt}]
)

# Print out the whole output dictionary
print(output)

# Get the output text only
print(output['choices'][0]['message']['content'])
