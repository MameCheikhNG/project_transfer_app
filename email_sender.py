import smtplib
from email.message import EmailMessage

def send_email(sujet, contenu, destinataire):
    expediteur = "mamecheikh095@gmail.com"  # Remplace par ton adresse Gmail
    mot_de_passe = "xwts mlpa scnu jews"  # Utilise un mot de passe d'application Gmail

    message = EmailMessage()
    message["Subject"] = sujet
    message["From"] = expediteur
    message["To"] = destinataire
    message.set_content(contenu)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(expediteur, mot_de_passe)
            smtp.send_message(message)
            return True
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
        return False
