import openai
from pydantic import BaseModel
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the schema using Pydantic
class MarkdownResponse(BaseModel):
    title: str
    content: str

# Function to interact with OpenAI API
def generate_structured_response(markdown_template):
    # Define the messages and the schema
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": markdown_template}
    ]

    # Call the OpenAI API with the structured output format
    response = openai.ChatCompletion.create(
        model="gpt-4o-2024-08-06",
        messages=messages,
        response_format=MarkdownResponse
    )

    # Parse the response
    structured_output = response.choices[0].message.parsed
    return structured_output

# Example markdown template
markdown_template = """
# Title
Write a brief introduction about OpenAI's Structured Outputs.

## Content
Provide details on how structured outputs can be used in applications.
"""

# Generate and print the structured response
structured_response = generate_structured_response(markdown_template)
print(f"Title: {structured_response.title}")
print(f"Content: {structured_response.content}")