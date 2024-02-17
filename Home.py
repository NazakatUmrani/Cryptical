import streamlit as st

st.title("Cryptical - A Python Based Web App")

# Hero section
st.markdown(
    """
    **Welcome to Cryptical!**

    This web app empowers you to explore the fascinating world of cryptography using the power of Python. Unleash a diverse arsenal of cipher algorithms for encryption and decryption, safeguarding your messages and unlocking hidden secrets.

    **Key Features:**

    - **Multiple Ciphers:** Experiment with Caesar Cipher, Vigenère Cipher, and more, each with customizable parameters.
    - **Simple Interface:** Navigate seamlessly through our intuitive interface tailored for ease of use.
    - **Real-time Results:** Witness instant encryption and decryption as you input your text and select your preferred cipher.
    - **Detailed Explanations:** Gain valuable insights into the inner workings of each algorithm through comprehensive explanations.

    **Coming Soon:**

    - Additional ciphers, including RSA and AES.
    - File encryption and decryption capabilities.
    - Interactive tutorials and guides.

    **Get Started:**

    Navigate through the sidebar to delve into the specific ciphers offered by Cryptical. Unleash your inner cryptographer and secure your messages with confidence!

    """
)

# Explore ciphers button
st.page_link(
    "pages/1_Algorithms List.py",
    label="Explore Ciphers",
    icon="🔐"
)

# Additional info and features
st.subheader("Learn More")
st.write(
    """
    Cryptical is a valuable tool for:

    - **Security enthusiasts:** Explore different encryption techniques and understand their underlying mechanisms.
    - **Developers:** Integrate cryptographic functionalities into their applications seamlessly.
    - **Educators:** Engage students in interactive learning experiences related to cryptography.

    **Stay tuned for regular updates and exciting new features!**
    """
)

# Social media links (optional)
st.subheader("About")
st.markdown(
    """
    Nazakat Umrani, is the developer of this web app, he is proficient in C++, Java, C and a little bit of python as well. He is linux user and lover as well, He is currently pursuing his Bachelor's Degree in Software Engineering from Quaid-e-Awam University of Engineering, Science and Technology, Nawabshah, Sindh, Pakistan.

    **Connect with him:**

    - [GitHub](https://github.com/NazakatUmrani)
    - [Source Code Repo](https://github.com/NazakatUmrani/Cryptical)
    - [Linkedin](https://linkedin.com/in/NazakatUmrani)
    - [Twitter/X](https://twitter.com/NazakatUmrani)

    """
)

