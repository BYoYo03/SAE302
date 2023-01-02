# Projet SAE 302 : Interface de surveillance de serveurs ou de machines clients

Mon projet correspond aux demandes du projet intermédiaire en entier avec des points du cahier de charge du projet difficile.

# Contexte

A l’image du protocole SNMP, nous souhaitons réaliser un système client-serveur permettant d’envoyer des commandes systèmes permettant de superviser et de diagnostiquer des machines ou serveurs à distance.

### Contenue du dossier :

`Fichier texte :`             

historique.txt : ce fichier sert d'historique pour les commandes

access.txt : ce fichier nous permet de définir le port et l'adresse ip des deux serveurs

help.txt : ce fichier est une aide des commandes pouvant être effectués.

`Fichier de prog : `      

serv.py : serveur en python numéro 1

serv2.py : serveur en python numéro 2

style.css : fichier css permettant de réaliser le style de l'interface graphique

client.py : fichier client,utilisateur

### **Preparation**

Les paquets/librairies à installer sur python :

PyQt6,
sys,
socket,
psutil,
platform,
os.

Dans le fichier access.txt vous pouvez définir l'adresse ip des deux serveurs ainsi que leur port afin de vous connecter.
Il faut garder ce schéma d'écriture.

Exemple :

127.0.0.1 1222 localhost 1227

    ^       ^      ^      ^  
    ip    port     ip    port

Il faut que tout sois sur la premiere ligne avec des epsaces entre l'adresse ip et le port.

Donc la premiere adresse ip ce cas-là "127.0.0.1" avec le port "1222" corresponde au serveur 1.

La deuxième adresse ip dans ce cas-là "localhost" avec le port "1227" correspond au serveur 2.

Apres tous ces changements effectués vous pouvez désormais lancer les programmes :

serv.py
serv2.py

Ensuite celui-ci:

client.py

Une premiere interface pour la sélection du serveur s'affichera et par la suite vous aurez accès apres ce choix à l'interface pour l'échange des commandes entre le client et le serveur.

### **Ne pas tenir compte du dossier projet protype.**
