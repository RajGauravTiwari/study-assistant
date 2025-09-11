import streamlit as st
from PyPDF2 import PdfReader
from agents.qa_generator import summarize_text, generate_flashcards, generate_mcqs, answer_question


# --- Helper to display flashcards in grid (styled boxes) ---
# --- Helper to display flashcards in grid (styled equal-height boxes) ---
def display_flashcards(flashcards, page_num=None):
    if page_num:
        st.subheader(f"Page {page_num} Flashcards")

    for i in range(0, len(flashcards), 3):  # 3 cards per row
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(flashcards):
                card = flashcards[i + j]
                with col:
                    st.markdown(
                        f"""
                        <div style="border: 2px solid #4CAF50; border-radius: 10px; 
                                    padding: 12px; margin: 6px; background-color: #f9f9f9;
                                    box-shadow: 1px 1px 6px rgba(0,0,0,0.1); 
                                    font-size:14px; display:flex; flex-direction:column; 
                                    justify-content:space-between; min-height:180px;">
                            <p style="color:#2E7D32; font-weight:bold;">Q: {card['q']}</p>
                            <p style="color:#000000; margin-top:6px;"><b>A:</b> {card['a']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )



# --- Helper to display MCQs (plain text, no styling) ---
def display_mcqs(mcqs, page_num=None):
    if page_num:
        st.subheader(f"Page {page_num} MCQs")

    for idx, mcq in enumerate(mcqs, start=1):
        st.markdown(f"**Q{idx}: {mcq['q']}**")
        options = mcq.get("options", [])
        for opt in options:
            st.write(f"- {opt}")
        st.write(f"**Answer:** {mcq.get('answer', 'N/A')}")
        st.write("")  # spacing


def run_app():
    st.title("📘 Study Assistant")

    uploaded_file = st.file_uploader("Upload PDF/TXT notes", type=["pdf", "txt"])
    text_input = st.text_area("Or write/paste notes here:")

    if not uploaded_file and not text_input.strip():
        st.info("Please provide notes via file or text to start generating content.")
        return

    pages_text = []

    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            for i, page in enumerate(reader.pages):
                pages_text.append(page.extract_text())
        else:
            pages_text = [uploaded_file.read().decode("utf-8")]

    if text_input.strip():
        pages_text.append(text_input)

    # --- Process each page ---
    for i, page_text in enumerate(pages_text, start=1):
        st.subheader(f"Page {i} Summary")
        page_summary = summarize_text(page_text)
        st.write(page_summary)

        flashcards = generate_flashcards(page_text)
        display_flashcards(flashcards, page_num=i)

        mcqs = generate_mcqs(page_text)
        display_mcqs(mcqs, page_num=i)

    # --- Ask a question about the whole document ---
    st.subheader("Ask a question about your notes:")
    question = st.text_input("Type your question here", label_visibility="visible")
    if question.strip():
        all_text = "\n".join(pages_text)
        answer = answer_question(question, context=all_text)
        st.write("**Answer:**", answer)


if __name__ == "__main__":
    run_app()
