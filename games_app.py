import streamlit as st
import time

# Helper function for Affine Cipher
def affine_encrypt(text, a, b):
    result = ""
    for char in text.lower():
        if char.isalpha():
            result += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    # Find modular inverse of a
    a_inv = pow(a, -1, 26)
    result = ""
    for char in cipher.lower():
        if char.isalpha():
            result += chr(((a_inv * (ord(char) - 97 - b)) % 26) + 97)
        else:
            result += char
    return result

# Typewriter effect
def typewriter(text, speed=0.05):
    for char in text:
        st.write(char, end="", unsafe_allow_html=True)
        time.sleep(speed)
    st.write("")  # Add a new line after finishing

# Streamlit App
st.title("**Riddle Breaker: The Encrypted Door**")
st.write("### Can you uncover the secrets hidden in the code?")

# Initialize session state
if "stage" not in st.session_state:
    st.session_state.stage = 1

if st.session_state.stage == 1:
    st.subheader("**The Mysterious Door**")
    typewriter(
        "You stand before a locked door. Carved into the wood are the words:\n\n"
        "**'The key lies in **a** and **b**, where they dance in harmony. "
        "For those who seek, the answer hides in the equation that binds them.'**\n\n"
        "The values of **a** and **b** can be found where the harmony lies: "
        "**a = 3** and **b = 25**."
    )

    encrypted_word = affine_encrypt("bukapintu", 3, 25)
    st.write(f"**Encrypted word on the door:** `{encrypted_word}`")

    answer = st.text_input("Enter the decryption key:", max_chars=50)

    if st.button("Submit"):
        if answer.lower() == "bukapintu":
            st.success("The door creaks open, revealing a dimly lit corridor.")
            st.session_state.stage = 2
            st.experimental_rerun()
        else:
            st.error("The key doesn't fit. Try again.")

elif st.session_state.stage == 2:
    st.subheader("**The Forgotten Waves**")
    typewriter(
        "Di bawah gelombang yang sunyi, rahasia yang terlupakan tetap ada, "
        "merajut kisah-kisah yang tak terucapkan oleh gema yang memudar.\n\n"
        "Namun, **SLPTMLE** tetap bersembunyi di antara kita. Kehadirannya "
        "ditunggu setiap akhir hari ke-7 dan bulan ke-17."
    )

    st.write("**Clue:** 'a = 7; b = 17'")
    encrypted_word_2 = "SLPTMLE"
    st.write(f"**Encrypted word:** `{encrypted_word_2}`")

    answer_2 = st.text_input("Enter the decryption key for the second riddle:", max_chars=50)

    if st.button("Submit Answer"):
        if answer_2.lower() == affine_decrypt(encrypted_word_2, 7, 17):
            st.success("The secret is revealed. The riddle ends, but another mystery begins...")
            st.balloons()
            st.write("To be continued...")
        else:
            st.error("The answer remains hidden. Try again.")
