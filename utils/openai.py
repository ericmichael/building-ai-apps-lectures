from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("OPENAI_API_BASE"),
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def completion(prompt, max_tokens=None, temperature=0):
    completion = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prompt,
      max_tokens=max_tokens,
      temperature=temperature
    )
    return completion.choices[0].text.strip()

def chat_completion(message, model="gpt-3.5-turbo", prompt=None, temperature=0, messages=[]):    
    # Add the prompt to the messages list
    if prompt is not None:
        messages += [{"role": "system", "content": prompt}]
    
    if message:
        # Add the user's message to the messages list
        messages += [{"role": "user", "content": message}]

    # Make an API call to the OpenAI ChatCompletion endpoint with the model and messages
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    
    # Extract and return the AI's response from the API response
    return completion.choices[0].message.content.strip()