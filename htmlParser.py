import requests
from bs4 import BeautifulSoup, Comment

def get_clean_html_body(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract body content
        body = soup.body
        if not body:
            return "No body tag found."

        # Remove unnecessary elements
        for tag in body(["script", "style", "meta", "noscript", "iframe", "link"]):
            tag.decompose()  # Remove tag completely
        
        # Remove comments
        for comment in body.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()

        # Convert cleaned body to string
        cleaned_body = str(body)

        return cleaned_body

    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

def comma_to_bullets(text):
    items = [item.strip() for item in text.split(',')]
    return "\n".join(f"- {item}" for item in items)
