from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_link_names(promptArgs, new_html, new_links,):
    prompt = f"""
    You are an expert at assigning meaningful names to links based on their position in HTML emails.

    ### Naming Conventions:
    {promptArgs.naming_conventions}

    ### Example:

    
    HTML: {promptArgs.html_example_one}
    Links: {promptArgs.link_names_example_one}
    Generated Names:{promptArgs.generated_link_names_example_one}



    ### New Task:
    HTML: {new_html}
    Links: {new_links}

    Generate the correct names for these links, and return them in the same order they were passed in:
    """

    response = client.chat.completions.create(
        model="gpt-4.5-preview-2025-02-27",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content