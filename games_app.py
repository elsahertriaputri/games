import streamlit as st
import time

# Improved typewriter effect
def typewriter(text, speed=0.05):
    """Display text as if being typed."""
    output = ""
    for char in text:
        output += char
        st.markdown(f"<p style='display:inline'>{output}</p>", unsafe_allow_html=True)
        time.sleep(speed)
    st.markdown("<br>", unsafe_allow_html=True)  # Final line break

# Affine Cipher Functions
def affine_encrypt(text, a, b):
    """Encrypts text using the Affine Cipher."""
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr(((a * (ord(char) - offset) + b) % 26) + offset)
        else:
            encrypted += char
    return encrypted

def affine_decrypt(text, a, b):
    """Decrypts text using the Affine Cipher."""
    decrypted = ""
    a_inv = pow(a, -1, 26)  # Modular inverse of a
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted += chr(((a_inv * ((ord(char) - offset) - b)) % 26) + offset)
        else:
            decrypted += char
    return decrypted

# Initial Setup
st.set_page_config(page_title="Riddle Breaker: The Encrypted Door", layout="centered")
st.title("Riddle Breaker: The Encrypted Door")
st.subheader("Can you uncover the secrets hidden in the code?")

# First Riddle
typewriter("You stand before a locked door. An ancient code must be cracked to proceed.", speed=0.07)
st.markdown("---")
st.write("The code is encrypted with an Affine Cipher.")
st.write("Clue: The key values are hidden in plain sight.")
st.write("- 'a' must be **relatively prime** to 26.")
st.write("- 'b' is a mysterious offset.")

# Input for First Riddle
a1, b1 = 3, 25  # Hardcoded values for first riddle
encrypted_word = affine_encrypt("bukapintu", a1, b1)
user_input = st.text_input(f"Decode this word to unlock the door: `{encrypted_word}`").lower()

if user_input == "bukapintu":
    st.success("The door creaks open!")
    st.balloons()
    typewriter("The door reveals another clue...", speed=0.07)

    # Second Riddle
    st.markdown("---")
    typewriter(
        "In the silence beneath the waves, a forgotten secret lies...\n"
        "It whispers: SLPTMLE\n"
        "Clue: It arrives every 7th day and 17th month.\n"
        "(a = 7, b = 17)",
        speed=0.07,
    )
    
    # Input for Second Riddle
    a2, b2 = 7, 17
    encrypted_second_word = "SLPTMLE"  # Encrypted form of the answer
    user_input2 = st.text_input("Decode this message to move forward:").upper()

    if user_input2 == affine_decrypt(encrypted_second_word, a2, b2).upper():
        st.success("You solved the second riddle!")
        typewriter("A hidden path appears before you. The journey continues...", speed=0.07)
else:
    if user_input:
        st.error("The door remains locked. Try again.")
