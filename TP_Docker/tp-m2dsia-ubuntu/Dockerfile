FROM ubuntu:22.04
RUN echo “Je suis à l’étape .....”
# Empêcher les prompts interactifs (important pour apt)
ENV DEBIAN_FRONTEND=noninteractive
# Mettre à jour le système et installer quelques paquets
RUN apt-get update && \
apt-get install -y curl && \
apt-get clean
# Commande par défaut à exécuter
CMD ["bash"]

FROM mysql:8
# Expose le port MySQL
# Copie du script d'initialisation SQL dans le répertoire de démarrage
COPY init.sql /docker-entrypoint-initdb.d/
EXPOSE 3306