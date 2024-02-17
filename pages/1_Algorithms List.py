import streamlit as st

# Define function to create algorithm block
def create_algorithm_block(title, description, link):
    st.markdown(f"<div style='background-color: #1F2022; border:1px solid grey; border-radius: 5%; padding: 10px;'><h2 style='color:orange;'>{title}</h2><p>{description} <a href='{link}' target='_top' style='color:orange;'>Try it!</a></p></div><br>", unsafe_allow_html=True)

# Create algorithm blocks
create_algorithm_block("Monoalphabetic Cipher",
"""A type of substitution cipher where each letter of the plaintext is replaced by another letter, resulting in a scrambled message. Popular examples include Caesar Cipher and Atbash Cipher.""","Monoalphabetic")

create_algorithm_block("Caesar Cipher",
"""A simple monoalphabetic cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet.""","Caesar")

create_algorithm_block("PlayFair Cipher",
"""A more complex substitution cipher that uses a 5x5 matrix to encrypt and decrypt messages. It involves combining pairs of letters.""","Playfair")

create_algorithm_block("Vigenere Cipher",
"""A polyalphabetic substitution cipher where each letter of the plaintext is shifted by a different amount based on a keyword.""","Vigenere")

# Add "More coming soon!" message
st.subheader("More Coming Soon!")
st.write("Stay tuned for exciting new additions to the algorithm list, including RSA, AES, and others!")