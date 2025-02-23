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


Ce projet utilise Docker pour gérer les conteneurs nécessaires à l'application.

## Commandes de base

### 1. Démarrer les conteneurs

Pour démarrer les conteneurs, exécutez la commande suivante :

```bash
docker-compose up
```

Cela lancera tous les services définis dans le fichier `docker-compose.yml`.

### 2. Arrêter les conteneurs

Pour arrêter les conteneurs, exécutez la commande suivante :

```bash
docker-compose down
```

Cela arrêtera et supprimera tous les conteneurs, réseaux et volumes associés.


