import streamlit as st
import base64
from datetime import datetime

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Nazira", page_icon="❤️", layout="centered")

# --- 2. ÖNBELLEKLEME (Takılmayı Önler) ---
@st.cache_data
def get_base64_cached(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- 3. ARKA PLAN ---
try:
    bin_str = get_base64_cached('test.png')
    st.markdown(f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.6); 
        border-radius: 20px;
        padding: 2rem;
        margin-top: 2rem;
        text-align: center;
    }}
    </style>
    ''', unsafe_allow_html=True)
except:
    st.error("Arka plan dosyası (test.png) bulunamadı!")

# --- 4. GİRİŞ KONTROLÜ ---
if 'giris_yapildi' not in st.session_state:
    st.session_state.giris_yapildi = False

# --- 5. EKRAN YÖNETİMİ ---

if not st.session_state.giris_yapildi:
    # GİRİŞ EKRANI
    st.title("Hoş Geldin Nazira Bebek ❤️")
    st.write("*Giriş yaparak bir ömür boyu kalbinizi teslim etmeyi kabul etmiş sayılırsınız. KKVK Aydınlatma Metni Geçerli Değildir.")
    
    if st.button("Giriş Yap"):
        st.session_state.giris_yapildi = True
        st.rerun()

else:
    # ANA İÇERİK (Giriş yapıldıktan sonra)
    
    # 🎈 Balonları buraya aldık, sayfa açılır açılmaz patlayacaklar!
    st.balloons()
    
    # Müzik
    try:
        audio_base64 = get_base64_cached("Ricchi E Poveri - Sara Perche Ti Amo.mp3")
        audio_html = f"""
            <audio id="bg-audio" autoplay loop>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
    except:
        st.warning("Müzik dosyası yüklenemedi.")
    
    # İçerikler
    st.title("Hayatımız Anlam Kazanalı...")
    
    baslangic_tarihi = datetime(2025, 6, 30, 19, 30)
    bugun = datetime.now()
    fark = bugun - baslangic_tarihi
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Gün", fark.days)
    col2.metric("Saat", fark.seconds // 3600)
    col3.metric("Dakika", (fark.seconds % 3600) // 60)
    
    st.write("---")
    
    try:
        st.image("111.jpg", caption="Seni tanıdığımdan beri her günüm daha güzel ❤️")
    except:
        st.error("Fotoğraf (111.jpg) bulunamadı!")
        
    st.subheader("Seni Çok Seviyorum ✨")