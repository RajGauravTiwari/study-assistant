import wikipediaapi
from googlesearch import search  # pip install google
import re

def find_resources(topic: str) -> dict:
    """Find relevant websites and YouTube channels for a given topic."""
    websites = []
    youtube_channels = []

    # --- Wikipedia ---
    try:
        wiki = wikipediaapi.Wikipedia(language="en", user_agent="study-assistant-app")
        page = wiki.page(topic)
        if page.exists():
            websites.append(page.fullurl)
    except:
        pass

    # --- Google search for educational sites ---
    try:
        for url in search(f"{topic} tutorial site:edu OR site:khanacademy.org", num_results=3):
            websites.append(url)
    except:
        pass

    # --- YouTube ---
    try:
        for url in search(f"{topic} tutorial site:youtube.com", num_results=3):
            youtube_channels.append(url)
    except:
        pass

    return {
        "websites": websites if websites else ["No relevant websites found."],
        "youtube": youtube_channels if youtube_channels else ["No relevant YouTube channels found."]
    }
