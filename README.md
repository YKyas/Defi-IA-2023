<h1 align="center">
1001 nights: prédire le prix d'une réservation d'hôtel
</h1>

![alt text](https://github.com/YKyas/Defi-IA-2023/blob/master/final.jpg)

## Organisation du Projet
```
|
|
+--- data  		        <- Dossier contenant les données collectées 
+--- data_preparation           <- Dossier contenant les résultats des requêtes et les premières analyses de données  
+--- models                     <- Contient les modèles entrainés et sérialisés 
|   +--- regressor_xgb.joblib   <- Example de modèle entraîné et sérialisé (XGboost)
+--- notebook                   <- Dossier contenant le notebook final du projet avec les requirements pour la préparion de données 
|   +--- AIF_Final.ipynb        <- Le notebook utilisé pour entraîner les modèles enrigistrés au niveau du dossier models
|   +--- None-requirements.txt  <- Fichier de requirements pour exécuter le notebook 
|   +--- __init__.py
+--- predictions                <- Dossier contenant les prédictions sur le test set par models 
|   +--- Y_pred_34.csv          
|   +--- Y_pred_34_stack.csv    
+--- processed_data             <- Dossier contenant des csv qui représentent les différentes phases de traitement de données 
+--- webapp                     <- Dossier contenant l'application web Gradio
|   +--- app.py                 <- le fichier python pour exécuter l'application Gradio
|   +--- prepare.py             <- le fichier de prépration de données provenant de l'interface web pour les prédictions 
|   +--- __init__.py            
+--- DockerfileGradio           <- Dockerfile pour déployer l'application Gradio
+--- DockerfileImage            <- Dockerfile pour préparer une image de base contenant les différents requirements python du projet 
+--- DockerfileJup              <- Dockerfile pour déployer Jupyter pour explorer le code et le tester
+--- requirements.txt           <- Fichier contenant les requirements python du projet
+--- __init__.py                
```
> 📝 **_NOTE:_** Avant de commencer la création des images doker, il faut télécharger le modèle Joblib à partir du drive <a href="https://drive.google.com/uc?id=1JKSCVvMCDbVyLiamoe1J77pMq5XPq8YJ" target="_blank">(xgboost model)</a> et le mettre au dossier models. 

## Requirements

- Python 3.7+

- Docker

## Usage
### Etape 1 : Cloner ce repository

Dans cet objectif vous pouvez executer les commande suivante: 

```bash
# Cloner le repo
git clone https://github.com/YKyas/Defi-IA-2023.git
# Ouvrir le dossier du projet 
cd Defi-IA-2023
```

### Etape 2 : Images docker

Afin de créer les images docker nous pourrons suivre deux approches:

#### Approche 1: Build étape par étape
Dans cette approche nous construisons une image de base contenant les dépendance du projet que nous utilisons pour construires les autres images.  

> 📝 **_NOTE:_** Vous aurez besoin du modèle joblib qu'on vous a demandé de télécharger à partir du lien suivant <a href="https://drive.google.com/uc?id=1JKSCVvMCDbVyLiamoe1J77pMq5XPq8YJ" target="_blank"> (xgboost model)</a>. Ensuite, vous devez l'enregistrer dans le dossier models

Puis, vous pouvez utiliser les commandes  suivantes pour créer l'image : 

Nous commençons par la  création une image de base contenant les requirements nécessaires pour le projet 

```docker
docker build -t defiia:BaseImage -f DockerfileImage . 
```
La deuxième étape consiste a créer l'image de l'application Gradio en utilisant la commande suivante :  
```docker
docker build -t defiia:gradiov1 -f DockerfileGradio . 
```
La troisième étape est de construire une image pour une application jupyter pour explorer et modifier le code source du projet : 
```docker
docker build -t defiia:Jupv1 -f DockerfileJup .
```
####  Approche 2: One shot build
La difference avec l'autre approche est que n'installe les dépendances à la création de chaque image du projet.

Si vous ne voulez pas télécharger le modèle entraîné, vous pouvez utiliser les commandes suivantes qui permettent de télécharger automatiquement le modèle entraîné: 

Création de l'image de l'application Gradio en utilisant la commande suivante : 

```docker
docker build -t defiia:gradiov1 -f DockerfileGradioALL . 
```
Création de l'image pour une application jupyter pour explorer et modifier le code source du projet : 
```docker
docker build -t defiia:Jupv1 -f DockerfileJupALL .
```
### Etape 3 : Démarrage des conteneurs Docker

Une fois les images sont prêtes nous pouvons démarrer les conteneurs: 

Nous commençons par l'application Gradio en exposant le port 7860 du hôte pour accéder a l'interface web Gradio ;
```docker
docker run -it -p  7860:7860  defiia:gradiov1 
```
Une fois l'application Gradio a bien démarré, vous pouvez copier une des liens (privé ou publique) proposés selon votre configuration et le coller sur la  barre de votre navigateur. Une page web sera afficher comme montre la figure ci-dessous pour choisir les entrées necessaires au modèle pour la prédictions. 

![alt text](https://github.com/YKyas/Defi-IA-2023/blob/master/gradio.png)

<p align="center">Interface de l'application Gradio</p>

Le deuxième conteneur est le serveur jupyter. Pour cela, vous pouvez exécuter la commande suivante en exposant le port 8888 (selon votre configuration)

```docker
docker run -it -p  8888:8888  defiia:Jupv1 
```

Une page web comme montre la figure ci-dessous sera afficher en copiant un des liens affichés au moment du démarrage du conteneur. 
Vous pouvez utiliser le token **DefiIa** pour s'authentifier à jupyter. En cas de problème un token est généré par défaut et affiché au niveau de la console au démarrage du conteneur.




![alt text](https://github.com/YKyas/Defi-IA-2023/blob/master/juptoken.png)
<p align="center">Authentification au niveau jupyter avec le token DefiIa </p>

![alt text](https://github.com/YKyas/Defi-IA-2023/blob/master/jupinterface.png)
<p align="center">L'interface jupyter au niveau du dossier du projet</p>

