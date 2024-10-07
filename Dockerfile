# Utiliser une image de base officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Créer le fichier de configuration config.json
RUN echo '{\n  "api_key": "${REVOLUT_API_KEY}"\n}' > config.json

# Commande pour exécuter le script
CMD ["python", "revolut_importer.py"]
