import streamlit as st
from streamlit_option_menu import option_menu

#Function to encrypt the text
def encrypt(text):
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        result=result+chr(ord(char)+13)
    return result

#Function to decrypt the text
def decrypt(text):
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        result=result+chr(ord(char)-13)
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
    icons=["lock-fill", "unlock-fill"], # icons names comes from bootstrap icons [https://icons.getbootstrap.com/]
    orientation="horizontal",
    styles={
        "container": {"padding": "2%","padding-top": "1%","padding-bottom": "1%"},
        "nav-item": {"margin-right": "2%"},
        "nav-link": {"margin": "2%","padding": "10px 20px","border-radius": "5px","background-color": "white","color": "black"},
        "nav-link-selected": {"background-color": "orange"}
    }
)


if(selected=="Encryption"):
    text=st.text_input("Enter Plain Text:")
    cipher=encrypt(text)
    st.write(f"Encrypted text:")
    st.code(cipher, language="text")
else:
    cipher1=st.text_input("Enter Cipher Text:")
    text1=decrypt(cipher1)
    st.write(f"Decrypted text:")
    st.code(text1, language="text")

# Explanation of the Monoalphabetic Cipher Algorithm
st.markdown("""
<h2 style='color:orange;'>How Monoalphabetic Ciphers Work</h2>
""",unsafe_allow_html=True)

st.markdown("""
It utilizes a **fixed shift value of 13** to scramble and unscramble messages. It works by shifting each letter of the plaintext **13 positions forward** in the alphabet for encryption and **13 positions backward** for decryption.

**Steps (Encryption):**

For each character in the plaintext:
  - Add 13 to it's ASCII code

**Steps (Decryption):**

For each character in the plaintext:
  - Subtract 13 from it's ASCII code

**Example:**

 - Plaintext: "Hello, world!"
 - Encrypted text: "Uryy|9-|yq."
 - Decrypted text: "Hello, world!"

**Note:** Monoalphabetic Cipher is a basic encryption technique and easily breakable. For stronger security, consider more complex ciphers.
""")