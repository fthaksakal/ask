import streamlit as st
import base64
from datetime import datetime

# --- 1. SAYFA AYARLARI ---
st.set_page_config(page_title="Nazira", page_icon="❤️", layout="centered")

# --- 2. ÖNBELLEKLEME ---
@st.cache_data
def get_base64_cached(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# --- 3. VERİ HAVUZLARI ---

# İspanyolca Havuzu (Örnek başlangıç)
kelime_havuzu = [
    {"es": "Hola", "tr": "Merhaba", "cumle": "Hola, ¿cómo estás?", "cumle_tr": "Merhaba, nasılsın?"},
    {"es": "Gracias", "tr": "Teşekkürler", "cumle": "Muchas gracias por todo.", "cumle_tr": "Her şey için çok teşekkürler."},
    {"es": "Amor", "tr": "Aşk", "cumle": "Te quiero, mi amor.", "cumle_tr": "Seni seviyorum aşkım."},
]

# Matematik Havuzu (Örnek başlangıç)
matematik_havuzu = [
    {"soru": "12 + 8 = ?", "cevap": 20},
    {"soru": "15 - 7 = ?", "cevap": 8},
    {"soru": "9 x 4 = ?", "cevap": 36},
    {"soru": "24 / 3 = ?", "cevap": 8},
]

def get_daily_items(havuz):
    day_of_year = datetime.now().timetuple().tm_yday
    # Havuzun boş olma ihtimaline karşı kontrol
    if not havuz: return []
    start_idx = (day_of_year * 3) % len(havuz)
    return havuz[start_idx : start_idx + 3]

# --- 4. ARKA PLAN ---
bin_str = get_base64_cached('test.png')
if bin_str:
    st.markdown(f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.65); 
        border-radius: 20px;
        padding: 2rem;
        margin-top: 2rem;
        text-align: center;
    }}
    </style>
    ''', unsafe_allow_html=True)

# --- 5. SESSION STATE (Giriş, Müzik ve Sayfa Takibi) ---
if 'giris_yapildi' not in st.session_state:
    st.session_state.giris_yapildi = False
if 'muzik_caliyor' not in st.session_state:
    st.session_state.muzik_caliyor = True

# --- 6. SIDEBAR (MENÜ) VE MÜZİK KONTROLÜ ---
if st.session_state.giris_yapildi:
    st.sidebar.title("❤️ Menü")
    
    # MÜZİK KONTROLÜ (Kesin çözüm)
    if st.session_state.muzik_caliyor:
        if st.sidebar.button("⏸️ Müziği Durdur"):
            st.session_state.muzik_caliyor = False
            st.rerun()
    else:
        if st.sidebar.button("▶️ Müziği Başlat"):
            st.session_state.muzik_caliyor = True
            st.rerun()

    st.sidebar.write("---")
    sayfa = st.sidebar.radio("Gitmek istediğin yer:", ["Ana Sayfa", "İspanyolca Öğreniyorum", "Matematik Öğreniyorum"])
else:
    sayfa = "Giriş"

# --- 7. EKRAN YÖNETİMİ ---

if not st.session_state.giris_yapildi:
    # GİRİŞ EKRANI
    st.title("Hoş Geldin Sevgilim... ❤️")
    st.write("Sana küçük bir sürpriz hazırladım.")
    
    if st.button("❤️ İçeri Gir"):
        st.session_state.giris_yapildi = True
        st.rerun()
    
    st.markdown('<p style="font-size: 11px; color: #555; font-style: italic;">Giriş yaparak bir ömür boyu kalbinizi teslim etmeyi kabul etmiş sayılırsınız.</p>', unsafe_allow_html=True)

else:
    # MÜZİK OYNATMA (Sadece muzik_caliyor True ise kod basılır)
    if st.session_state.muzik_caliyor:
        audio_str = get_base64_cached("Ricchi E Poveri - Sara Perche Ti Amo.mp3")
        if audio_str:
            audio_html = f"""
                <audio autoplay loop id="myAudio">
                    <source src="data:audio/mp3;base64,{audio_str}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)

    # SAYFA İÇERİKLERİ
    if sayfa == "Ana Sayfa":
        st.balloons()
        st.title("Hayatımız Anlam Kazanalı...")
        
        # Zaman Hesaplama
        baslangic = datetime(2025, 6, 30, 19, 30)
        fark = datetime.now() - baslangic
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Gün", fark.days)
        c2.metric("Saat", fark.seconds // 3600)
        c3.metric("Dakika", (fark.seconds % 3600) // 60)
        
        st.write("---")
        st.image("111.JPG", caption="Seni tanıdığımdan beri her günüm daha güzel ❤️")
        st.subheader("Seni Çok Seviyorum! ✨")

    elif sayfa == "İspanyolca Öğreniyorum":
        st.title("İspanyolca Öğreniyorum")
        
        bugun_esp = get_daily_items(kelime_havuzu)
        for i, k in enumerate(bugun_esp, 1):
            with st.expander(f"Kelime {i}: {k['es']}", expanded=True):
                st.write(f"**Türkçe Anlamı:** {k['tr']}")
                st.info(f"💬 **Cümle:** {k['cumle']}\n\n**Çeviri:** {k['cumle_tr']}")
        
        st.write("---")
        st.caption("Ar-Ge çalışmalarımız devam etmektedir.- Fatih Aksakal")

    elif sayfa == "Matematik Öğreniyorum":
        st.title("Matematik Öğreniyorum")
        
        bugun_mat = get_daily_items(matematik_havuzu)
        for i, soru_verisi in enumerate(bugun_mat, 1):
            st.subheader(f"Soru {i}: {soru_verisi['soru']}")
            
            # number_input ile cevap alıyoruz
            user_ans = st.number_input(f"Cevabını buraya yaz:", key=f"mat_{i}", step=1, value=None)
            
            if user_ans is not None:
                if user_ans == soru_verisi['cevap']:
                    st.success("Tebrikler! Doğru cevap ✅")
                else:
                    st.error("Opss... Tekrar dene! ❌")
            st.write("---")
