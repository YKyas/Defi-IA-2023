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
> 📝 **_NOTE:_** Avant de commencer la création des images doker, il faut télécharger le modèle Joblib <a href="https://drive.google.com/uc?id=1JKSCVvMCDbVyLiamoe1J77pMq5XPq8YJ" target="_blank">(xgboost model)</a> et le mettre au dossier models. 

## Requirements

Python 3.7+

## Usage

### Image docker

Afin de création les images docker nous utilisons les commandes  suivantes : 

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
Une fois les images sont prêtes nous pouvons démarrer les conteneurs: 

Nous commençons par l'application Gradio en exposant le port 7860 du hôte pour accéder a l'interface web Gradio ;
```docker
docker run -p  7860:7860  defiia:gradiov1 
```
![alt text](https://github.com/YKyas/Defi-IA-2023/blob/master/gradio.png)

<p align="center">Interface de l'application Gradio</p>

Le deuxième conteneur est le serveur jupyter. Pour cela, vous pouvez exécuter la commande suivante en exposant le port 8888

```docker
docker run -p  8888:8888  defiia:Jupv1 
```

> 📝 **_NOTE:_** Le token pour s'authentifier à jupyter est par défaut **DefiIa**. En cas de problème un token par défaut est généré et affiché au niveau de la console au démarrage du conteneur.

![alt text](https://github.com/YKyas/Defi-IA-2023/blob/master/juptoken.png)
<p align="center">Authentification au niveau jupyter avec le token DefiIa </p>

![alt text](https://github.com/YKyas/Defi-IA-2023/blob/master/jupinterface.png)
<p align="center">L'interface jupyter au niveau du dossier du projet</p>

