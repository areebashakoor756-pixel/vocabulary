import streamlit as st
import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# App title
st.title("Adjective vs. Adverb Identifier")
st.write("""
Enter a sentence, and the app will highlight **adjectives** and **adverbs** separately.
""")

# User input
sentence = st.text_area("Enter your sentence here:")

if sentence:
    doc = nlp(sentence)
    
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    adverbs = [token.text for token in doc if token.pos_ == "ADV"]
    
    st.subheader("Adjectives:")
    st.write(", ".join(adjectives) if adjectives else "No adjectives found.")
    
    st.subheader("Adverbs:")
    st.write(", ".join(adverbs) if adverbs else "No adverbs found.")
