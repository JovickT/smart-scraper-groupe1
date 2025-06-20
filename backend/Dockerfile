# Étape 1 : image de base officielle Python
FROM python:3.11-slim

# Étape 2 : définition du répertoire de travail
WORKDIR /app

# Étape 3 : copier les fichiers nécessaires
COPY . /app

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt


# Étape 5 : exposer le port utilisé par Flask
EXPOSE 5000

# Étape 6 : définir la variable d’environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Étape 7 : lancer l’application
CMD ["flask", "run"]
