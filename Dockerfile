# Utiliser une image officielle Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt


# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y default-mysql-client


# Copier le reste des fichiers du projet
COPY . .

# Exposer le port 5000 (Flask)
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["./wait-for-mysql.sh", "mysql", "python", "main.py"]


