from openai import OpenAI
from dotenv import load_dotenv
import os
from promptStuff import ex_link_names_one
from promptStuff import ex_generated_link_names_one
from promptStuff import ex_html_one

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_link_names(new_html, new_links, ex_link_names_one=ex_link_names_one, ex_generated_link_names_one=ex_generated_link_names_one, ex_html_one=ex_html_one):
    prompt = f"""
    You are an expert at assigning meaningful names to links based on their position in HTML emails.

    ### Naming Conventions:
    - "Current Month X: [Event Name]" → If in the Current Month section, with ordering based on placement.
    - "Save The Date: [Event Name]" → If it’s a special upcoming event.
    - "Footer: Opt Out" → If it’s an unsubscribe link in the footer.
    - "Footer: Manage Preferences" → If it allows email preference management.
    - "View All Button" → If it is a call-to-action button for all events.
    - "Header: Alumni Lockup" → If it is a branding-related link near the top.

    ### Example:

    
    HTML: {ex_html_one}
    Links: {ex_link_names_one}
    Generated Names:{ex_generated_link_names_one}



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