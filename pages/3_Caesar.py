import streamlit as st
from streamlit_option_menu import option_menu

#Function to encrypt the text
def encrypt(text,s):
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        result=result+chr(ord(char)+s)
    return result

#Function to decrypt the text
def decrypt(text,s):
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        result=result+chr(ord(char)-s)
    return result

st.markdown("""
<style>
#caesar-cipher {
    color: orange;
}
</style>
""", unsafe_allow_html=True)

#Title
st.write("""# Caesar Cipher""")

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

st.warning("Note: The Caesar Cipher is not case-sensitive and it converts alphabets, spaces and special characters as well.")

if(selected=="Encryption"):
    text=st.text_input("Enter Plain Text:")
    k=st.text_input("Enter Key:")
    if(k==""):
        k=0
    k=int(k)
    cipher=encrypt(text,k)
    st.write(f"Encrypted text:")
    st.code(cipher, language="text")
else:
    cipher1=st.text_input("Enter Cipher Text:")
    k=st.text_input("Enter Key:")
    if(k==""):
        k=0
    k=int(k)
    text1=decrypt(cipher1,k)
    st.write(f"Decrypted text:")
    st.code(text1, language="text")

# Explanation of the Caesar Cipher Algorithm
st.markdown("""
<h2 style='color:orange;'>How Caesar Cipher Works?</h2>
""",unsafe_allow_html=True)

st.markdown("""
It is a simple substitution cipher where each letter of the plaintext is shifted a specific number of positions down the alphabet (forward for encryption, backward for decryption).

**Steps:**

1. Enter a **shift value**.
2. For each character in the plaintext:
    - Add shift to it's ASCII Code.

**Decryption:**

1. Enter a **shift value**.
2. For each character in the plaintext:
    - Subtract shift from it's ASCII Code.

**Example:**

 - Plaintext: "Hello, world!"
 - Encrypted text: "Khoor/#Zruog$"
 - Decrypted text: "Hello, world!"

**Note:** Caesar Cipher is a basic encryption technique and easily breakable with frequency analysis. For stronger security, consider more complex ciphers.
""")