import streamlit as st
import os
from email_sender import send_email

st.set_page_config(page_title="Transfert de fichiers", layout="centered")
st.title("📤 Transfert de fichiers lourds + notification")

# Saisie des infos
expediteur = st.text_input("Votre adresse e-mail").strip()
destinataire = st.text_input("Adresse e-mail du destinataire").strip()

# Upload fichier
uploaded_file = st.file_uploader("Choisissez un fichier à partager")

if uploaded_file:
    st.info("⏳ Upload en cours...")

    # Sauvegarde temporaire dans Streamlit
    save_path = os.path.join(".", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ Fichier uploadé avec succès.")

    # Générer un lien de téléchargement fictif (Streamlit Community Cloud ne permet pas l'accès public direct)
    # À remplacer par un lien Dropbox / GDrive / S3 si tu veux
    simulated_link = f"(Fichier temporaire uploadé : **{uploaded_file.name}**)"

    if st.button("Envoyer l'e-mail avec le lien"):
        if expediteur and destinataire:
            sujet = "📁 Nouveau fichier à télécharger"
            message = f"""
Bonjour,

{expediteur} vous a envoyé un fichier via l'application Streamlit.

⚠️ Lien local (non public) : le fichier '{uploaded_file.name}' est temporairement stocké sur l'application. 

✅ Pour le partage réel, utilisez Google Drive, Dropbox ou AWS S3.

Cordialement,  
L’équipe de transfert
"""
            success = send_email(sujet, message, destinataire)
            if success:
                st.success("📨 E-mail envoyé avec succès.")
            else:
                st.error("❌ Échec de l'envoi de l'e-mail.")
        else:
            st.warning("Veuillez remplir les deux adresses e-mail.")
