# pages/algorithms.py
import streamlit as st

def monoalphabetic():
    st.title("Monoalphabetic Cipher")
    st.write("The monoalphabetic cipher is a substitution cipher where each letter in the plaintext is replaced with another letter.")

def caesar():
    st.title("Caesar Cipher")
    st.write("The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.")

def playfair():
    st.title("Playfair Cipher")
    st.write("The Playfair cipher is a digraph substitution cipher where pairs of letters in the plaintext are replaced with other pairs.")

def app():
    st.title("Algorithms")
    algorithms = ["Monoalphabetic Cipher", "Caesar Cipher", "Playfair Cipher", "Vigenere Cipher (Coming Soon)"]
    choice = st.selectbox("Choose an algorithm", algorithms)

    if choice == "Monoalphabetic Cipher":
        monoalphabetic()
    elif choice == "Caesar Cipher":
        caesar()
    elif choice == "Playfair Cipher":
        playfair()
    else:
        st.write("Vigenere Cipher implementation coming soon...")
