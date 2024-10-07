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

# Commande pour exécuter le script, en passant les variables d'environnement
CMD ["sh", "-c", "python revolut_importer.py --firefly-url $FIREFLY_III_URL --access-token $FIREFLY_III_ACCESS_TOKEN --api-key $REVOLUT_API_KEY --account-id $REVOLUT_ACCOUNT_ID"]
