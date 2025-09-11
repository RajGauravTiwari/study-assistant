import os
import json
import re
from dotenv import load_dotenv

load_dotenv()
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")

# --- Configure AI clients ---
if AI_PROVIDER == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

elif AI_PROVIDER == "openai":
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

elif AI_PROVIDER == "claude":
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))


def safe_json_parse(text: str):
    """Extract JSON array/object from text safely."""
    try:
        match = re.search(r'(\[.*\]|\{.*\})', text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except:
        pass
    return []


def summarize_text(text: str) -> str:
    """Generate detailed summary of notes."""
    if not text.strip():
        return ""
    prompt = f"Provide a detailed summary for the following notes:\n{text}"
    try:
        if AI_PROVIDER == "gemini":
            model = genai.GenerativeModel("gemini-1.5-flash")
            return model.generate_content(prompt).text

        elif AI_PROVIDER == "openai":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return response.choices[0].message.content.strip()

        elif AI_PROVIDER == "claude":
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return response.content[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def generate_flashcards(text: str, num_cards: int = 3) -> list:
    """Generate flashcards in JSON format."""
    if not text.strip():
        return []
    prompt = f"""
You are a study assistant. Create {num_cards} flashcards from the following notes.
Return ONLY valid JSON:
[
  {{ "q": "Question text", "a": "Answer text" }},
  ...
]
Notes:
{text}
"""
    try:
        if AI_PROVIDER == "gemini":
            model = genai.GenerativeModel("gemini-1.5-flash")
            response_text = model.generate_content(prompt).text

        elif AI_PROVIDER == "openai":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400
            )
            response_text = response.choices[0].message.content

        elif AI_PROVIDER == "claude":
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=400
            )
            response_text = response.content[0].text

        cards = safe_json_parse(response_text)
        return cards if cards else [{"q": "Could not generate flashcards", "a": ""}]
    except:
        return [{"q": "Could not generate flashcards", "a": ""}]


def generate_mcqs(text: str, num_mcqs: int = 3) -> list:
    """Generate multiple-choice questions in JSON format."""
    if not text.strip():
        return []
    prompt = f"""
You are a study assistant. Create {num_mcqs} multiple-choice questions from the following notes.
Return ONLY valid JSON:
[
  {{
    "q": "Question text",
    "options": ["Option A","Option B","Option C","Option D"],
    "answer": "Correct option"
  }},
  ...
]
Notes:
{text}
"""
    try:
        if AI_PROVIDER == "gemini":
            model = genai.GenerativeModel("gemini-1.5-flash")
            response_text = model.generate_content(prompt).text

        elif AI_PROVIDER == "openai":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            response_text = response.choices[0].message.content

        elif AI_PROVIDER == "claude":
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            response_text = response.content[0].text

        mcqs = safe_json_parse(response_text)
        return mcqs if mcqs else [{"q": "Could not generate MCQs", "options": [], "answer": ""}]
    except:
        return [{"q": "Could not generate MCQs", "options": [], "answer": ""}]


def answer_question(question: str, context: str) -> str:
    """Answer user question based on notes."""
    if not context.strip():
        return "No notes provided."
    prompt = f"Answer the following question based on the notes:\nNotes:\n{context}\nQuestion:\n{question}"
    try:
        if AI_PROVIDER == "gemini":
            model = genai.GenerativeModel("gemini-1.5-flash")
            return model.generate_content(prompt).text.strip()

        elif AI_PROVIDER == "openai":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            return response.choices[0].message.content.strip()

        elif AI_PROVIDER == "claude":
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            return response.content[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
