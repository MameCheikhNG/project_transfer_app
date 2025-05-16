# Application de Transfert de Fichiers Lourds

Cette application permet aux utilisateurs de **transférer des fichiers volumineux (≥1 Go)** en réseau interne entre collègues, en renseignant les emails de l'expéditeur et du destinataire. Le destinataire est notifié automatiquement par **email** lorsqu’un fichier lui est partagé.

---

## 🚀 Fonctionnalités

- Interface web simple pour :
  - Sélectionner un fichier lourd à transférer
  - Indiquer l’email de l’expéditeur et du récipiendaire
- Transfert de fichiers en réseau local sécurisé
- Notification par **email (via SMTP Gmail)** au récipiendaire avec :
  - Le nom de l’expéditeur
  - Le nom du fichier transféré
  - Un lien vers le dossier partagé (si applicable)

---

## 📂 Structure du projet

```bash
project_transfer_app/
│
├── main.py              # Backend Flask pour la réception des fichiers
├── app.py               # Interface Streamlit (frontend)
├── .env                 # Fichier des variables sensibles (non commit)
├── requirements.txt     # Dépendances du projet
└── README.md
