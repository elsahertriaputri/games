import streamlit as st

# === Konfigurasi affine cipher untuk Game 1 ===
a1 = 7  # Harus relatif prima dengan 26
b1 = 15  # Pergeseran
plaintext1 = "bukapintu"  # Kata rahasia Game 1

# === Konfigurasi affine cipher untuk Game 2 ===
a2 = 17  # Harus relatif prima dengan 26
b2 = 6   # Pergeseran
plaintext2 = "kekuatan"  # Kata rahasia Game 2

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

# Hasil enkripsi untuk Game 1 dan Game 2
ciphertext1 = affine_encrypt(plaintext1, a1, b1)
ciphertext2 = affine_encrypt(plaintext2, a2, b2)

# === Tampilan Streamlit ===
st.title("🔒 **Game Riddle: Dua Tantangan Misterius** 🔓")

# === Game 1: Buka Pintu Misterius ===
st.write("""
**Kamu terjebak di sebuah ruangan gelap. Di depanmu, ada pintu besar dengan ukiran aneh.**  
Di sisi pintu, terdapat petunjuk tertulis:  

_"Tujuh putaran roda kehidupan dan lima belas langkah ke depan akan membuka jalanmu."_  
_"Pecahkan kode ini untuk membukanya:"_
""")

# Tampilkan kata terenkripsi untuk Game 1
st.code(ciphertext1, language='plaintext')

# Input jawaban untuk Game 1
user_input1 = st.text_input("Apa kode rahasianya?", "").strip().lower()

# Cek jawaban untuk Game 1
if user_input1:
    if user_input1 == plaintext1:
        st.success("🎉 Selamat! Kamu berhasil membuka pintu!")
        st.write("""
        **Pintu terbuka lebar, tetapi misteri belum selesai.**  
        Di balik pintu, kesunyian dan teka-teki baru menunggumu. 🌟
        """)

        # === Game 2: Kekuatan Misterius ===
        st.write("""
        **Tantangan Baru:**  
        Sebuah kekuatan tersembunyi memanggilmu dari balik bayangan.  
        Gunakan pengetahuanmu untuk memecahkan kode berikut:
        """)

        # Tampilkan kata terenkripsi untuk Game 2
        st.code(ciphertext2, language='plaintext')

        # Input jawaban untuk Game 2
        user_input2 = st.text_input("Apa jawabannya?", "").strip().lower()

        # Cek jawaban untuk Game 2
        if user_input2:
            if user_input2 == plaintext2:
                st.success("🎉 Kamu berhasil memecahkan teka-teki kedua!")
                st.write("""
                **Selamat! Kamu telah menyelesaikan semua tantangan.**  
                Cahaya terang menyinari ruangan, dan kebebasan menunggumu.
                """)
            else:
                st.error("❌ Jawaban salah. Coba lagi!")
                st.write("**Petunjuk:** Kekuatan tersembunyi ada di balik kata 'kekuatan'.")
    else:
        st.error("❌ Jawaban salah. Coba lagi!")
        st.write("**Petunjuk:** Ingat, \(7\) adalah kunci, dan ada \(15\) langkah untuk maju.")

# Clue tambahan untuk Game 1
with st.expander("🔑 Lihat petunjuk tambahan untuk membuka pintu"):
    st.write("""
    - \(a = 7\): "Tujuh roda kehidupan."  
    - \(b = 15\): "Lima belas langkah ke depan."  
    Gunakan ini untuk memecahkan kode.
    """)

# Clue tambahan untuk Game 2
with st.expander("🔑 Lihat petunjuk tambahan untuk tantangan kedua"):
    st.write("""
    - \(a = 17\): "Tujuh belas lingkaran kekuatan tersembunyi."  
    - \(b = 6\): "Enam langkah menuju inti kekuatan."  
    Cari pola tersembunyi di kata terenkripsi.
    """)
