import streamlit as st
import string
from streamlit_option_menu import option_menu

main=string.ascii_lowercase

#Function to encrypt the text
def encrypt(plain_text,key):  
    index=0
    cipher_text=""

    # convert into lower case    
    key=key.lower()

    # For generating key, the given keyword is repeated
    # in a circular manner until it matches the length of
    # the plain text.
    for c in plain_text:
        if c.lower() in main:
            # to get the number corresponding to the alphabet
            off=ord(key[index])-ord('a')

            # implementing algo logic here
            encrypt_num=(ord(c.lower())-ord('a')+off)%26
            encrypt=chr(encrypt_num+ord('a'))

            # adding into cipher text to get the encrypted message
            if(c.isupper()):
                cipher_text+=encrypt.upper()
            else:
                cipher_text+=encrypt.lower()

            # for cyclic rotation in generating key from keyword
            index=(index+1)%len(key)
        # to not to change spaces or any other special
        # characters in their positions
        else:
            cipher_text+=c
    return cipher_text

#Function to decrypt the text
#Function to decrypt the text
def decrypt(cipher_text,key):
    index=0
    plain_text=""

    # convert into lower case
    key=key.lower()

    for c in cipher_text:
        if c.lower() in main:
            # to get the number corresponding to the alphabet
            off=ord(key[index])-ord('a')

            positive_off=26-off
            decrypt=chr((ord(c.lower())-ord('a')+positive_off)%26+ord('a'))

            # adding into plain text to get the decrypted messag
            if(c.isupper()):
                plain_text+=decrypt.upper()
            else:
                plain_text+=decrypt.lower()

            # for cyclic rotation in generating key from keyword
            index=(index+1)%len(key)
        else:
            plain_text+=c
    return plain_text

st.markdown("""
<style>
#vigenere-cipher {
    color: orange;
}
</style>
""", unsafe_allow_html=True)

#Title
st.write("""# Vigenere Cipher""")

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

st.warning("Note: The Vigenere Cipher is not case-sensitive and it can convert alphabets, spaces and special characters as well.")

if(selected=="Encryption"):
    text=st.text_input("Enter Plain Text:")
    key=st.text_input("Enter Key:")
    if(key==""):
        key="a"
    cipher=encrypt(text,key)
    st.write(f"Encrypted text:")
    st.code(cipher, language="text")
else:
    cipher1=st.text_input("Enter Cipher Text:")
    key=st.text_input("Enter Key:")
    if(key==""):
        key="a"
    text1=decrypt(cipher1,key)
    st.write(f"Decrypted text:")
    st.code(text1, language="text")

# Explanation of the Vigenere Cipher Algorithm
st.markdown("""
<h2 style='color:orange;'>How Vigenere Cipher Works?</h2>
""",unsafe_allow_html=True)

st.markdown("""
The Vigenère Cipher is a classic encryption technique that utilizes multiple Caesar Ciphers based on a keyword, enhancing security compared to its simpler cousin. It focuses on encrypting alphabetical characters while preserving other symbols.

**Key Features:**

- **Polyalphabetic:** Employs multiple shift values generated from a chosen keyword.
- **Character-Focused:** Primarily encrypts alphabetic characters (A-Z, a-z).
- **Symbol Preservation:** Leaves special characters and other symbols unchanged.

**Steps for Encryption:**

1. **Keyword Preparation:**
    - Select a keyword and repeat it to match the plaintext length.

2. **Shift Values:**
    - Convert each letter of the keyword to its numerical position (A=1, B=2, etc.).

3. **Character Encryption:**
    - Iterate through each character in the plaintext:
        - For alphabetic characters:
            - Add the corresponding keyword letter's numerical position to its ASCII code.
            - Wrap around the alphabet if the new code exceeds 'Z' (90) or 'z' (122).
            - Convert the new code back to a letter.
        - For non-alphabetic characters:
            - Leave them unchanged.

4. **Combining Encrypted Characters:**
    - The ciphertext is the final string formed by combining the encrypted characters and preserved non-alphabetic characters.

**Decryption:**

1. Follow the encryption steps, but subtract the keyword letter's numerical position instead of adding.

**Example:**

- Plaintext: "Attack at dawn!"
- Keyword: "SECRET"
- Encrypted text: "Sxvrgd sx frag!" (Non-alphabetic characters preserved)
- Decrypted text: "Attack at dawn!"

**Note:** While more secure than the Caesar Cipher, Vigenère Cipher remains susceptible to frequency analysis. Consider more complex techniques for highly sensitive data.

**Additional Notes:**

- Feel free to adapt the example and wording to match your specific implementation.
- If your implementation handles uppercase and lowercase letters differently, you can clarify that in the explanation.
- Remember to emphasize the importance of using a strong and unpredictable keyword for better security.
""")