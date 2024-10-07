# Importateur Revolut - Dockerfile

FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Commande pour exécuter le script avec les variables d'environnement
CMD ["sh", "-c", "python firefly_revolut_cli.py --firefly-url $FIREFLY_III_URL --firefly-token $TOKEN --revolut-token $REV_PASS --account-id $REVOLUT_ACCOUNT_ID --device-id $REVOLUT_DEVICE_ID"]
