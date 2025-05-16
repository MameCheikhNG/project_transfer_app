import streamlit as st
import requests

BACKEND_URL = "http://10.8.15.164:8000"

st.set_page_config(page_title="Transfert de fichiers", layout="centered")
st.title("📤 Transfert de fichiers lourds")

uploaded_file = st.file_uploader("Choisissez un fichier à partager", type=None)

if uploaded_file:
    st.info("⏳ Upload en cours...")
    response = requests.post(
        f"{BACKEND_URL}/upload/",
        files={"file": (uploaded_file.name, uploaded_file.getvalue())}
    )
    if response.status_code == 200:
        data = response.json()
        download_link = f"{BACKEND_URL}/download/{data['file_id']}/{data['filename']}"
        st.success("✅ Fichier envoyé avec succès !")
        st.markdown(f"[📥 Télécharger le fichier]({download_link})")
    else:
        st.error("❌ Une erreur est survenue.")
