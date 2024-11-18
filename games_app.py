import streamlit as st

# Konfigurasi affine cipher
a = 7  # Harus relatif prima dengan 26
b = 15  # Pergeseran

# Kata rahasia
plaintext = "bukapintu"

# Fungsi enkripsi Affine Cipher
def affine_encrypt(plaintext, a, b):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Hanya mengenkripsi huruf
            x = ord(char) - ord('a')
            encrypted_char = chr(((a * x + b) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-huruf tetap
    return encrypted_text

# Enkripsi kata rahasia
ciphertext = affine_encrypt(plaintext, a, b)

# Judul website
st.title("Riddle: Pecahkan Kode!")

# Cerita petunjuk
st.write("""
**Selamat datang di game riddle!**
Kamu berada di depan pintu besar yang terkunci. Di dinding sebelah pintu, ada tulisan tua dengan ukiran aneh:
 
_"Tujuh kali putar roda waktu, lalu tambahkan lima belas langkah ke depan."_  
_"Dengan ini, kamu bisa membuka pintu yang terkunci."_

Kamu menduga ini adalah petunjuk untuk memecahkan kode di bawah ini:
""")
st.code(ciphertext, language='plaintext')

# Input jawaban
user_input = st.text_input("Masukkan jawabanmu:", "").strip().lower()

# Cek jawaban
if user_input:
    if user_input == plaintext:
        st.success("Selamat! Kamu berhasil membuka pintu!")
        # Menampilkan pintu terbuka
        st.image(
            "https://cdn.pixabay.com/photo/2016/08/03/23/55/door-1560814_960_720.png",  # Ganti dengan gambar pintu terbuka
            caption="Pintu telah terbuka!"
        )
    else:
        st.error("Jawabanmu salah. Coba lagi!")
