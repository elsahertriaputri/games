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
st.title("🔒 **Game Riddle: Buka Pintu Misterius** 🔓")

# Cerita awal
st.write("""
**Kamu terjebak di sebuah ruangan gelap. Di depanmu, ada pintu besar dengan ukiran aneh.**
Di sisi pintu, terdapat petunjuk tertulis: 

_"Tujuh putaran roda kehidupan dan lima belas langkah ke depan akan membuka jalanmu."_  
_"Pecahkan kode ini untuk membukanya:"_
""")

# Tampilkan kata terenkripsi
st.code(ciphertext, language='plaintext')

# Input jawaban
user_input = st.text_input("Apa kode rahasianya?", "").strip().lower()

# Cek jawaban
if user_input:
    if user_input == plaintext:
        st.success("🎉 Selamat! Kamu berhasil membuka pintu!")
        # Narasi sukses
        st.write("""
        Kamu berhasil memecahkan kode dan pintu terbuka lebar.  
        Di balik pintu, kesunyian menerpa. Lanjutkan misteri ini! 🌟
        """)

        # Tambahkan teka-teki baru setelah pintu terbuka
        st.write("""
        **Di balik gelombang kesunyian, rahasia yang terlupakan tetap ada, merajut kisah-kisah yang tak terucapkan oleh gema yang memudar, namun hrhzpspc tetap bersembunyi di antara kita.**  
        **Kehadirannya ditunggu setiap akhir hari ke-7 dan bulan ke-15 dalam penanggalan kuno Mesir.**  
        
        **Pecahkan teka-teki berikut untuk melanjutkan:**
        """)
        plaintext= "hrhzpspc"
        # Tampilkan teka-teki baru
        st.write("""
        Teka-teki: hrhzpspc adalah sebuah kode yang tersemat dalam gelombang.  
        Gunakan petunjuk yang ada dan temukan jawabannya.
        
        **Petunjuk:**  
        - Kode ini berhubungan dengan angka 7 dan bulan 15.  
        - hrhzpspc mengandung sebuah pesan tersembunyi.
        """)

        # Input jawaban riddle kedua
        second_input = st.text_input("Apa jawabannya?", "").strip().lower()

        # Cek jawaban untuk teka-teki kedua
        if second_input:
            if second_input == "silent":
                st.success("🎉 Kamu berhasil memecahkan teka-teki kedua! Gelombang hilang, dan rahasia tersembunyi terbongkar!")
                st.write("""
                **Selamat! Kamu telah berhasil keluar dari ruangan misterius ini dan mengungkap semua rahasia tersembunyi.**  
                Gelombang yang sunyi kini menghilang, tergantikan oleh kekuatan dan kamu bisa melihat cahaya yang menerangi jalanmu. Kamu telah menyelesaikan tantangan ini dengan sukses! 🌟
                """)
            else:
                st.error("❌ Jawaban salah. Coba lagi!")
                st.write("**Petunjuk tambahan:** Kode ini memiliki hubungan dengan kata 'silent'.")
        
    else:
        st.error("❌ Jawaban salah. Coba lagi!")
        st.write("**Petunjuk:** Ingat, \(7\) adalah kunci, dan ada \(15\) langkah untuk maju.")

# Clue visual tambahan untuk teka-teki pertama
with st.expander("🔑 Lihat petunjuk tambahan"):
    st.write("""
    - \(a = 7\): "Tujuh roda kehidupan."  
    - \(b = 15\): "Lima belas langkah ke depan."  
    Gunakan ini untuk memecahkan kode yang ada.
    """)
