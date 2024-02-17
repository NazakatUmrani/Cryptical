import streamlit as st
import string
from streamlit_option_menu import option_menu

def insertAt(s, index, value):
    return s[:index] + value + s[index:]

# Generate Table with specified key
def key_generation(key):
    # initializing all and generating key_matrix
    main=string.ascii_lowercase.replace('j','.')
    # convert all alphabets to lower
    key=key.lower()
    
    key_matrix=['' for i in range(5)]
    # if we have spaces in key, those are ignored automatically
    i=0;j=0
    for c in key:
        if c in main:
            # putting into matrix
            key_matrix[i]+=c

            # to make sure repeated characters in key
            # doesnt include in the key_matrix, we replace the
            # alphabet into . in the main, whenever comes in iteration
            main=main.replace(c,'.')
            # counting column change
            j+=1
            # if column count exceeds 5
            if(j>4):
                # row count is increased
                i+=1
                # column count is set again to zero
                j=0

    # to place other alphabets in the key_matrix
    # the i and j values returned from the previous loop
    # are again used in this loop, continuing the values in them
    for c in main:
        if c!='.':
            key_matrix[i]+=c

            j+=1
            if j>4:
                i+=1
                j=0
                
    return(key_matrix)

#Function to encrypt the text
def encrypt(plain_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]

    indexes=[]
    for i in range(len(plain_text)):
        if(plain_text[i]==' '):
            indexes.append(i)
    # RULE1: if both letters in the pair are same or one letter is left at last,
    # replace second letter with x or add x, else continue with normal pairing

    plain_text=plain_text.replace(' ','')

    i=0
    # let plain_text be nazakat
    while i<len(plain_text):
        # i=0,1,2,3
        a=plain_text[i]
        b=''

        if((i+1)==len(plain_text)):
            # if the chosen letter is last and doesnt have pair
            # then the pai will be x
            b='x'
        else:
            # else the next letter will be pair with the previous letter
            b=plain_text[i+1]

        if(a!=b):
            plain_text_pairs.append(a+b)
            # if not equal then leave the next letter,
            # as it became pair with previous alphabet
            i+=2
        else:
            plain_text_pairs.append(a+'x')
            # else dont leave the next letter and put x
            # in place of repeated letter and conitnue with the next letter
            # which is repeated (according to algo)
            i+=1
            
    for pair in plain_text_pairs:
        # RULE2: if the letters are in the same row, replace them with
        # letters to their immediate right respectively
        flag=False
        for row in key_matrix:
            if(pair[0].lower() in row and pair[1].lower() in row):
                # find will return index of a letter in string
                j0=row.find(pair[0].lower())
                j1=row.find(pair[1].lower())
                if(pair[0].isupper()):
                    cipher_text_pair=(row[(j0+1)%5]).upper()
                else:
                    cipher_text_pair=(row[(j0+1)%5]).lower()
                if(pair[1].isupper()):
                    cipher_text_pair=str(cipher_text_pair)+(row[(j1+1)%5]).upper()
                else:
                    cipher_text_pair=str(cipher_text_pair)+(row[(j1+1)%5]).lower()
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue

        # RULE3: if the letters are in the same column, replace them with
        # letters to their immediate below respectively
                
        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])
            if(pair[0].lower() in col and pair[1].lower() in col):
                # find will return index of a letter in string
                i0=col.find(pair[0].lower())
                i1=col.find(pair[1].lower())
                if(pair[0].isupper()):
                    cipher_text_pair=(col[(i0+1)%5]).upper()
                else:
                    cipher_text_pair=(col[(i0+1)%5]).lower()
                if(pair[1].isupper()):
                    cipher_text_pair=str(cipher_text_pair)+str(col[(i1+1)%5].upper())
                else:
                    cipher_text_pair=str(cipher_text_pair)+str(col[(i1+1)%5].lower())
                cipher_text_pairs.append(cipher_text_pair)
                flag=True
        if flag:
            continue
        #RULE:4 if letters are not on the same row or column,
        # replace with the letters on the same row respectively but
        # at the other pair of corners of rectangle,
        # which is defined by the original pair

        i0=0
        i1=0
        j0=0
        j1=0

        cipher_text_pair=""
        for i in range(5):
            row=key_matrix[i]
            if(pair[0].lower() in row):
                i0=i
                j0=row.find(pair[0].lower())
            if(pair[1].lower() in row):
                i1=i
                j1=row.find(pair[1].lower())
        if(pair[0].isupper()):
            cipher_text_pair=key_matrix[i0][j1].upper()
        else:
            cipher_text_pair=key_matrix[i0][j1].lower()
        if(pair[1].isupper()):
            cipher_text_pair=str(cipher_text_pair)+""+str(key_matrix[i1][j0].upper())
        else:
            cipher_text_pair=str(cipher_text_pair)+str(key_matrix[i1][j0].lower())
        cipher_text_pairs.append(cipher_text_pair)
    retStr="".join(cipher_text_pairs)
    for i in indexes:
        retStr=insertAt(retStr,i,"#")
    return retStr

#Function to decrypt the text
def decrypt(cipher_text):
    plain_text_pairs=[]
    cipher_text_pairs=[]

    # RULE1: if both letters in the pair are same or one letter is left at last,
    # replace second letter with x or add x, else continue with normal pairing
    
    indexes=[]
    for i in range(len(cipher_text)):
        if(cipher_text[i]=='#'):
            indexes.append(i)

    cipher_text=cipher_text.replace('#','')

    i=0
    while i<len(cipher_text):
        # i=0,1,2,3
        a=cipher_text[i]
        b=cipher_text[i+1]

        cipher_text_pairs.append(a+b)
        # else dont leave the next letter and put x
        # in place of repeated letter and conitnue with the next letter
        # which is repeated (according to algo)
        i+=2

    for pair in cipher_text_pairs:
        # RULE2: if the letters are in the same row, replace them with
        # letters to their immediate right respectively
        flag=False
        for row in key_matrix:
            if(pair[0].lower() in row and pair[1].lower() in row):
                # find will return index of a letter in string
                j0=row.find(pair[0].lower())
                j1=row.find(pair[1].lower())
                # same as reverse
                # instead of -1 we are doing +4 as it is modulo 5
                if(pair[0].isupper()):
                    plain_text_pair=row[(j0+4)%5].upper()
                else:
                    plain_text_pair=row[(j0+4)%5].lower()
                if(pair[1].isupper()):
                    plain_text_pair=plain_text_pair+row[(j1+4)%5].upper()
                else:
                    plain_text_pair=plain_text_pair+row[(j1+4)%5].lower()
                if(plain_text_pair[1].lower()=='x'): #issue x not getting removed
                    plain_text_pairs.append(plain_text_pair[0])
                else:
                    plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue

        # RULE3: if the letters are in the same column, replace them with
        # letters to their immediate below respectively
                
        for j in range(5):
            col="".join([key_matrix[i][j] for i in range(5)])
            if(pair[0].lower() in col and pair[1].lower() in col):
                # find will return index of a letter in string
                i0=col.find(pair[0].lower())
                i1=col.find(pair[1].lower())
                # same as reverse
                # instead of -1 we are doing +4 as it is modulo 5
                if(pair[0].isupper()):
                    plain_text_pair=col[(i0+4)%5].upper()
                else:
                    plain_text_pair=col[(i0+4)%5].lower()
                if(pair[1].isupper()):
                    plain_text_pair=plain_text_pair+col[(i1+4)%5].upper()
                else:
                    plain_text_pair=plain_text_pair+col[(i1+4)%5].lower()
                if(plain_text_pair[1].lower()=='x'): #issue x not getting removed
                    plain_text_pairs.append(plain_text_pair[0])
                else:
                    plain_text_pairs.append(plain_text_pair)
                flag=True
        if flag:
            continue
        #RULE:4 if letters are not on the same row or column,
        # replace with the letters on the same row respectively but
        # at the other pair of corners of rectangle,
        # which is defined by the original pair

        i0=0
        i1=0
        j0=0
        j1=0

        for i in range(5):
            row=key_matrix[i]
            if(pair[0].lower() in row):
                i0=i
                j0=row.find(pair[0].lower())
            if(pair[1].lower() in row):
                i1=i
                j1=row.find(pair[1].lower())
        if(pair[0].isupper()):
            plain_text_pair=key_matrix[i0][j1].upper()
        else:
            plain_text_pair=key_matrix[i0][j1].lower()
        if(pair[1].isupper()):
            plain_text_pair=plain_text_pair+key_matrix[i1][j0].upper()
        else:
            plain_text_pair=plain_text_pair+key_matrix[i1][j0].lower()
        if(plain_text_pair[1].lower()=='x'): #issue x not getting removed
            plain_text_pairs.append(plain_text_pair[0])
        else:
            plain_text_pairs.append(plain_text_pair)
    retStr="".join(plain_text_pairs)
    for i in indexes:
        retStr=insertAt(retStr,i," ")
    return retStr
st.markdown("""
<style>
#playfair-cipher {
    color: orange;
}
</style>
""", unsafe_allow_html=True)

#Title
st.write("""# Playfair Cipher""")

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

st.warning("Note: The Playfair Cipher is not case-sensitive and it only converts alphabets and spaces.")

if(selected=="Encryption"):
    text=st.text_input("Enter Plain Text:")
    key=st.text_input("Enter Key:")
    # calling first function
    key_matrix=key_generation(key)
    cipher=encrypt(text)
    st.write(f"Encrypted text:")
    st.code(cipher, language="text")
else:
    cipher1=st.text_input("Enter Cipher Text:")
    key=st.text_input("Enter Key:")
    # calling first function
    key_matrix=key_generation(key)
    text1=decrypt(cipher1)
    st.write(f"Decrypted text:")
    st.code(text1, language="text")

# Explanation of the Caesar Cipher Algorithm
st.markdown("""
<h2 style='color:orange;'>How Playfair Cipher Works?</h2>
""",unsafe_allow_html=True)

st.markdown("""
The Playfair Cipher is a digraph substitution cipher that encrypts pairs of letters (digraphs) instead of single letters. It uses a 5x5 matrix, known as the key square, to map letter pairs to their encrypted counterparts.

**Key Features:**

- **Digraph encryption:** Encrypts two letters at a time, enhancing security over simple substitution ciphers.
- **Key square:** Uses a 5x5 matrix based on a keyword to determine letter substitutions.
- **Space handling:** Converts spaces to # during encryption and vice versa during decryption.

**Steps for Encryption:**

1. **Create the key square:**
   - Remove any duplicate letters from the keyword.
   - Fill the 5x5 matrix with the remaining letters of the keyword, followed by the remaining letters of the alphabet (usually excluding J).
2. **Prepare the plaintext:**
   - Split the plaintext into digraphs (pairs of letters).
   - If a digraph has two identical letters, insert an 'X' between them.
   - If the plaintext has an odd number of letters, add an 'X' at the end.
3. **Encrypt each digraph:**
   - Locate the two letters of the digraph in the key square.
   - If the letters are in the same row:
     - Replace them with the letters to their immediate right (wrapping around to the beginning of the row if necessary).
   - If the letters are in the same column:
     - Replace them with the letters directly below them (wrapping around to the top of the column if needed).
   - If the letters are in different rows and columns:
     - Replace them with the letters in the same row, but in the column of the opposite corner of the rectangle formed by the two original letters.
4. **Handle spaces:**
   - Replace spaces with # during encryption.

**Decryption:**

1. Follow the same steps as encryption, but apply the rules in reverse.
2. Replace # with spaces during decryption.

**Example:**

- Plaintext: "Hello, world!"
- Key: "keyword" (key square generated from this)
- Encrypted text: "HG#OZ/#SRNB$"
- Decrypted text: "HELLO, WORLD!"

**Note:** Playfair Cipher is more secure than Caesar Cipher but can still be broken with advanced techniques. For highly sensitive data, consider modern encryption algorithms.
""")