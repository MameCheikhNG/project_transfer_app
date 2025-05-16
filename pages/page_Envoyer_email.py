import streamlit as st
from email_sender import send_email

st.title("📧 Transfert de fichier avec notification e-mail")

# Champs du formulaire utilisateur
expediteur = st.text_input("Votre adresse e-mail").strip()
destinataire = st.text_input("Adresse e-mail du destinataire").strip()
lien_fichier = st.text_input("Lien vers le fichier (URL)").strip()

# Affichage pour débogage (optionnel, tu peux retirer ensuite)
# st.write(f"Expéditeur : {expediteur}")
# st.write(f"Destinataire : {destinataire}")
# st.write(f"Lien : {lien_fichier}")

if st.button("Envoyer l'e-mail"):
    if expediteur and destinataire and lien_fichier:
        sujet = "📁 Nouveau fichier à télécharger"
        message = f"""
Bonjour,

{expediteur} vous a envoyé un fichier.

Vous pouvez le récupérer ici : {lien_fichier}

Cordialement,
L’équipe de transfert
"""
        success = send_email(sujet, message, destinataire)
        if success:
            st.success(f"✅ E-mail envoyé à {destinataire}")
        else:
            st.error("❌ Une erreur est survenue lors de l'envoi.")
    else:
        st.warning("⚠️ Veuillez remplir tous les champs.")
