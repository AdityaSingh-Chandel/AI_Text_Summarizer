import streamlit as st
from summarizer import summarize_text

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝"
)

st.title("📝 AI Text Summarizer")

st.write(
    "Paste any article, notes, blog, or document and generate AI summaries."
)

text = st.text_area(
    "Enter Text",
    height=300
)

if st.button("Generate Summary"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        with st.spinner("Generating Summary..."):

            result = summarize_text(text)

        st.success("Done!")

        st.markdown(result)