# Étape 1 : build de l'app avec Node
FROM node:18 AS builder

# Créer un répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY package*.json ./
RUN npm install

# Copier tout le code source
COPY . .

# Construire l'application React
RUN npm run build

# Étape 2 : serveur web pour servir les fichiers statiques
FROM nginx:alpine

# Copier le build React dans le dossier de Nginx
COPY --from=builder /app/build /usr/share/nginx/html

# Copier un fichier de configuration nginx personnalisé (facultatif)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exposer le port 80
EXPOSE 80

# Commande par défaut
CMD ["nginx", "-g", "daemon off;"]
