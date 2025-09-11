import os
from dotenv import load_dotenv


# Load .env variables
load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")

if AI_PROVIDER == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

elif AI_PROVIDER == "openai":
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

elif AI_PROVIDER == "claude":
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))


def summarize_text(text: str) -> str:
    """
    Summarize study notes into key points using the selected AI provider.
    """
    if AI_PROVIDER == "gemini":
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Summarize this text into key study points:\n\n{text}")
        return response.text.strip()

    elif AI_PROVIDER == "openai":
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful study assistant."},
                {"role": "user", "content": f"Summarize this text into key study points:\n\n{text}"}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()

    elif AI_PROVIDER == "claude":
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[
                {"role": "user", "content": f"Summarize this text into key study points:\n\n{text}"}
            ]
        )
        return response.content[0].text.strip()

    else:
        return "No valid AI provider configured."
