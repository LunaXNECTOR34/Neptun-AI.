import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- KONFIGURASI SISTEM NEPTUN.AI ---
st.set_page_config(page_title="Neptun.AI v2.0", page_icon="🔱", layout="centered")

# TAMPILAN KHUSUS LUNA
def apply_style(theme):
    if theme == "Hitam (Deep Sea)":
        bg, txt, accent = "#000b1a", "#e0f2ff", "#00d4ff"
    else:
        bg, txt, accent = "#ffffff", "#1a1a1a", "#005f73"
    
    st.markdown(f"""
        <style>
        .stApp {{ background-color: {bg}; color: {txt}; }}
        h1 {{ color: {accent} !important; text-align: center; font-family: 'Arial'; }}
        .stChatMessage {{ border-radius: 15px; border: 1px solid {accent}44; }}
        footer {{ visibility: hidden; }}
        .luna-footer {{ position: fixed; bottom: 10px; width: 100%; text-align: center; color: gray; font-size: 10px; }}
        </style>
        """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🔱 Neptun Console")
    st.write("Created by: **Luna**")
    theme = st.selectbox("Tema:", ["Putih (Clean)", "Hitam (Deep Sea)"])
    apply_style(theme)
    st.divider()
    api_key = st.text_input("Dev Key (API Key):", type="password")
    st.info("Status: Alpha 2.0.0 - Secure")

# --- KONEKSI AI ---
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Nama kamu Neptun.AI v2.0.0. Creator: Luna. Kamu sangat sopan, cerdas, dan dilarang menjawab hal negatif/sensitif."
    )
else:
    st.warning("⚠️ Masukkan API Key Developer Luna untuk aktivasi.")
    st.stop()

# --- INTERFACE ---
st.markdown("<h1>🔱 NEPTUN.AI</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

if prompt := st.chat_input("Apa perintah Anda, Luna?"):
    # Filter Keamanan
    if any(x in prompt.lower() for x in ["bokep", "porn", "hack", "judi"]):
        with st.chat_message("assistant"):
            st.error("Maaf, Neptun.AI hanya memproses permintaan positif sesuai protokol keamanan Luna.")
    else:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.chat_history.append({"role": "assistant", "content": response.text})

st.markdown("<div class='luna-footer'>Created by: Luna | Neptun System © 2026</div>", unsafe_allow_html=True)
          
