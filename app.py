# app.py
import streamlit as st
import random

st.title("Vocabulary Quiz 📝")
st.write("Test your vocabulary! Choose the correct meaning for each word.")

# Sample vocabulary list: word -> list of options with first being correct
vocab = {
    "gregarious": ["sociable", "angry", "lazy", "shy"],
    "ephemeral": ["short-lived", "eternal", "boring", "happy"],
    "altruistic": ["selfless", "selfish", "greedy", "lazy"],
    "ambiguous": ["unclear", "obvious", "bright", "happy"],
    "candid": ["honest", "secretive", "shy", "rude"]
}

# Select a random word
word, options = random.choice(list(vocab.items()))
shuffled_options = options.copy()
random.shuffle(shuffled_options)

st.subheader(f"Word: {word}")
user_answer = st.radio("Select the correct meaning:", shuffled_options)

if st.button("Submit"):
    if user_answer == options[0]:
        st.success("Correct! ✅")
    else:
        st.error(f"Wrong! ❌ The correct meaning is: {options[0]}")
