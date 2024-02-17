import streamlit as st

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

#Title
st.write("""# Monoalphabetic Cipher Alogrithm""")

#Encryption
st.write("""## Encryption""")
text=st.text_input("Enter your text here:")
cipher=encrypt(text)
st.write(f"Encrypted text: {cipher}")

#Decryption
st.write("""## Decryption""")
cipher1=st.text_input("Enter your cipher here:")
text1=decrypt(cipher1)
st.write(f"Decrypted text: {text1}")
