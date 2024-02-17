import streamlit as st

# with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
<style>
#cryptical-a-python-based-web-app {
    color: orange;
}

div.stPageLink a {
  background-color: orange;
  padding: 10px 20px;
  border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

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
# Use st.columns for flexible layout
col1, col2 = st.columns([2, 1])

# Display profile picture in the right column
with col2:
    profile_pic = st.image('img/me.jpeg', width=150)  # Replace with your image path

# Display description and social links in the left column
with col1:
    st.markdown("""
        Nazakat Umrani is passionate about exploring the world of software development and enjoy mastering diverse programming languages like C++, Java, C, and Python. As a Linux user and enthusiast, I value its open-source philosophy and community. Currently, I'm pursuing my Bachelor's degree in Software Engineering at Quaid-e-Awam University of Engineering, Science and Technology in Nawabshah, Sindh, Pakistan.

        **Connect with me:**

        - [GitHub](https://github.com/NazakatUmrani)
        - [Source Code Repo](https://github.com/NazakatUmrani/Cryptical)
        - [Linkedin](https://linkedin.com/in/NazakatUmrani)
        - [Twitter](https://twitter.com/NazakatUmrani)
    """)