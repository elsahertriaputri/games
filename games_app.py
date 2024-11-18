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

# Cerita
st.write("""
**Kamu terjebak di sebuah ruangan gelap. Di depanmu, ada pintu besar dengan ukiran aneh.**
Di sisi pintu, terdapat petunjuk tertulis: 

_"Tujuh putaran roda kehidupan dan lima belas langkah ke depan akan membuka jalanmu."_  
_"Pecahkan kode ini untuk membukanya:"_
""")

# Gambar pintu tertutup
st.image(
    "https://cdn.pixabay.com/photo/2014/04/05/11/39/door-316723_960_720.jpg",  # Ganti dengan gambar pintu tertutup
    caption="Pintu misterius terkunci...",
    use_column_width=True,
)

# Tampilkan kata terenkripsi
st.code(ciphertext, language='plaintext')

# Input jawaban
user_input = st.text_input("Apa kode rahasianya?", "").strip().lower()

# Cek jawaban
if user_input:
    if user_input == plaintext:
        st.success("🎉 Selamat! Kamu berhasil membuka pintu!")
        # Gambar pintu terbuka
        st.image(
            "https://cdn.pixabay.com/photo/2016/08/03/23/55/door-1560814_960_720.png",  # Ganti dengan gambar pintu terbuka
            caption="Pintu terbuka lebar!",
            use_column_width=True,
        )
        # Narasi sukses
        st.write("""
        Kamu berhasil memecahkan kode dan pintu terbuka lebar.  
        Di balik pintu, cahaya terang menyinari ruangan. Selamat, kamu keluar dari ruangan misteri ini! 🌟
        """)
    else:
        st.error("❌ Jawaban salah. Coba lagi!")
        st.write("**Petunjuk:** Ingat, \(7\) adalah kunci, dan ada \(15\) langkah untuk maju.")

# Clue visual tambahan
with st.expander("🔑 Lihat petunjuk tambahan"):
    st.write("""
    - \(a = 7\): "Tujuh roda kehidupan."  
    - \(b = 15\): "Lima belas langkah ke depan."  
    Gunakan ini untuk memecahkan kode yang ada.
    """)
    st.image(
        "https://cdn.pixabay.com/photo/2016/04/01/10/03/clock-1296408_960_720.jpg",  # Gambar roda/angka 7
        caption="Clue: 7 adalah kunci.",
        use_column_width=True,
    )
