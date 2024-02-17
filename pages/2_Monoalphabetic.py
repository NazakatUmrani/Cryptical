import streamlit as st
from streamlit_option_menu import option_menu

#Function to encrypt the text
def encrypt(text):
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        if(ord(char)==32):
            result=result+chr(35)
        elif(char.isupper()):  #if the text[i] is in upper case
            result=result+chr((ord(char)+13-65)%26+65)
        else: #if it is lower
            result=result+chr((ord(char)+13-97)%26+97)
    return result

#Function to decrypt the text
def decrypt(text):
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        if(ord(char)==35):
            result=result+chr(32)
        elif(char.isupper()):  #if the text[i] is in upper case
            result=result+chr((ord(char)-13-65)%26+65)
        else: #if it is lower
            result=result+chr((ord(char)-13-97)%26+97)
    return result

st.markdown("""
<style>
#monoalphabetic-cipher {
    color: orange;
}
</style>
""", unsafe_allow_html=True)
#Title
st.write("""# Monoalphabetic Cipher""")

selected = option_menu(
    menu_title=None,
    options=["Encryption", "Decryption"],
    default_index=0,
    icons=["🔒", "🔓"],
    orientation="horizontal",
    styles={
        "container": {"padding": "2%","padding-top": "1%","padding-bottom": "1%"},
        "nav-link": {"margin": "2%","padding": "10px 20px","border-radius": "5px","background-color": "white","color": "black"},
        "nav-link-selected": {"background-color": "orange"}
    }
)


if(selected=="Encryption"):
    text=st.text_input("Enter your plain text here:")
    cipher=encrypt(text)
    st.write(f"Encrypted text:")
    st.code(cipher, language="text")
else:
    cipher1=st.text_input("Enter your cipher text here:")
    text1=decrypt(cipher1)
    st.write(f"Decrypted text:")
    st.code(text1, language="text")

# Explanation of the Monoalphabetic Cipher Algorithm
st.markdown("""
<h2 style='color:orange;'>How Monoalphabetic Ciphers Work</h2>
""",unsafe_allow_html=True)

st.markdown("""
The Monoalphabetic Cipher is a simple substitution cipher where each letter of the plaintext is replaced by another letter, resulting in a scrambled message. This particular Caesar Cipher variation shifts letters by 13 positions.

**Steps:**

1. Split the alphabet into two groups of 13 letters each:
    - Uppercase: A-M, N-Z
    - Lowercase: a-m, n-z
2. For each letter in the plaintext:
    - If it's a space, replace it with #.
    - If it's an uppercase letter, shift it 13 positions forward within its group (cyclically wrapping around if it reaches the end).
    - If it's a lowercase letter, shift it 13 positions forward within its group.
    - Otherwise, leave it unchanged (e.g., punctuation).
3. The resulting string is the ciphertext.

**Decryption:**

1. Follow the same steps as encryption, but shift letters 13 positions backward instead.
2. Replace # with spaces.

This explanation assumes a shift of 13 positions. Other shift values can be used, creating different Caesar Ciphers.

""")

# Add styling to explanation if desired
# st