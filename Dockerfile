# Utiliser une image Python de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Exposer le port 5000 pour Flask
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "app.py"]
