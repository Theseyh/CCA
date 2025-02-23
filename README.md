
# Cloud Computing - Projet de Stack de Développement

Ce projet consiste à configurer une infrastructure de stack de développement à l'aide de Docker et Docker Compose, pour tester et déployer du code dans un environnement containerisé. L'objectif est de créer un environnement de test dans un conteneur Docker, tout en développant et testant le code en dehors du conteneur.

## Prérequis

Avant de commencer, vous devez vous assurer que Docker et Docker Compose sont installés sur votre machine. Vous pouvez suivre les instructions ci-dessous pour installer ces outils :

- [Installer Docker](https://docs.docker.com/get-docker/)
- [Installer Docker Compose](https://docs.docker.com/compose/install/)

## Structure du Projet

Le projet est structuré comme suit :

- **app** : Contient les fichiers de l'application, tels que les scripts Python pour la logique d'application (`main.py`, `db.py`), ainsi qu'un script pour attendre la disponibilité de MySQL (`wait-for-mysql.sh`).
- **database** : Contient les fichiers liés à la base de données MySQL (dumps, configurations, etc.).
- **docker-compose.yml** : Le fichier de configuration Docker Compose pour la création de l'infrastructure de conteneurs.
- **Dockerfile** : Le fichier de configuration pour la construction de l'image Docker personnalisée.
- **requirements.txt** : Liste des dépendances Python nécessaires à l'application.

## Configuration et Déploiement

### 1. Créer les Conteneurs avec Docker Compose

Pour lancer les conteneurs et créer l'environnement de test, il suffit d'exécuter la commande suivante dans le répertoire principal du projet :

```bash
docker-compose up
```

Cela lancera tous les services définis dans le fichier `docker-compose.yml`.

### 2. Arrêter les Conteneurs

Pour arrêter les conteneurs, exécutez la commande suivante :

```bash
docker-compose down
```

Cela arrêtera et supprimera tous les conteneurs, réseaux et volumes associés.

---

## Intégration entre les Conteneurs MySQL et Flask

Le projet utilise deux conteneurs Docker : un pour la base de données MySQL et un autre pour l'application Flask. L'objectif est de permettre à l'application Flask de se connecter à la base de données MySQL et d'exécuter un programme Python qui décrit l'architecture de la base de données.

### 1. Conteneur MySQL
Le conteneur MySQL contient la base de données qui sera utilisée par l'application Flask. Il est configuré pour démarrer une base de données `users_db` avec un utilisateur `root` ayant pour mot de passe `root`. Ce conteneur permet de gérer les données nécessaires à l'application.

### 2. Conteneur Flask
Le conteneur Flask lance un serveur Flask qui interagit avec la base de données MySQL pour récupérer et manipuler des données via une API REST. L'application Flask est configurée pour attendre la disponibilité de MySQL avant de démarrer, garantissant ainsi une initialisation fluide des services.

Le fichier `docker-compose.yml` définit les deux services et permet de configurer les connexions réseau nécessaires pour que Flask puisse accéder à MySQL.

---


### **Projet Initial : Data Battle (ING2)**

Le projet initial visait à mettre en œuvre le moteur de recherche de la **Data Battle** d'ING2. L'objectif était de créer un moteur de recherche à l'aide d'un modèle **Transformer** et de trouver la meilleure réponse possible en fonction de la question posée.

Cependant, en raison du grand nombre de dépendances et des difficultés associées à leur gestion, nous avons décidé d'abandonner cette possibilité et de réorienter le projet.
