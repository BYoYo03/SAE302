# Description: Client de l'application de chat

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QShortcut, QKeySequence
import socket

# Création de l'interface graphique
# Création de la fenêtre principale
class MainWindow(QMainWindow):


    def __init__(self):
        # Initialisation de la fenêtre
        super().__init__()

        # Création de la fenêtre
        widget1 = QWidget()
        self.setCentralWidget(widget1)
        grid = QGridLayout()
        widget1.setLayout(grid)

        # Création des composants de la fenêtre
        lab = QLabel("Connexion information : Socket sur l'adresse {} et le port {}".format(host, port))
        self.__lab = QLabel("Commandes rapides :")
        self.__text = QLineEdit("")
        self.__text.setPlaceholderText("Saisir une commande")
        self.sortie = QTextEdit("")
        entrer = QPushButton("Entrer")
        ramB = QPushButton("RAM")
        cpuB = QPushButton("CPU")
        ipB = QPushButton("IP")
        osB = QPushButton("OS")
        nameB = QPushButton("name")
        QUIT = QPushButton("Kill")
        disc = QPushButton("Disconnect")
        reset = QPushButton("Reset")

        
        # Style des composants précis 
        QUIT.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                }
            QPushButton:hover {
                color: "red";
                }""")
        disc.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                }
            QPushButton:hover {
                color: "Orange";
                }""")
        reset.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                }
            QPushButton:hover {
                color: "Yellow";
                }""")
        
        entrer.setStyleSheet("""
            QPushButton {
                width: 80px;
            }""")

        # Placement des composants dans la fenêtre
        grid.addWidget(lab, 0, 2,)
        grid.addWidget(self.__lab, 0, 0,)
        grid.addWidget(self.__text, 10, 0, 1 , 3)
        grid.addWidget(self.sortie, 1, 2,8,10)
        grid.addWidget(entrer, 10, 5,)
        grid.addWidget(ramB, 1, 0)
        grid.addWidget(cpuB, 2, 0)
        grid.addWidget(ipB, 3, 0)
        grid.addWidget(osB, 4, 0)
        grid.addWidget(nameB, 5, 0)
        grid.addWidget(disc, 6, 0)
        grid.addWidget(QUIT, 7, 0)
        grid.addWidget(reset, 8, 0)

        # Création des raccourcis clavier 
        entrerpress = QShortcut(QKeySequence("Return"), self)
        entrerpress.activated.connect(self.__actionentrer)
        quitter = QShortcut(QKeySequence("Esc"), self)
        quitter.activated.connect(self.__actionQUIT)
        commandeavnt = QShortcut(QKeySequence("Up"), self)
    
        # Connexion des composants aux fonctions
        entrer.clicked.connect(self.__actionentrer)
        commandeavnt.activated.connect(self.__actioncommandeavnt)
        ramB.clicked.connect(self.__actionram)
        cpuB.clicked.connect(self.__actioncpu)
        ipB.clicked.connect(self.__actionip)
        osB.clicked.connect(self.__actionos)
        nameB.clicked.connect(self.__actionname)
        QUIT.clicked.connect(self.__actionQUIT)
        disc.clicked.connect(self.__actiondisc)
        reset.clicked.connect(self.__actionreset)

        # Affichage du titre de la fenêtre
        self.setWindowTitle("Client")

        #fonction entrer du clavier ou envoyer du bouton
    def __actionentrer(self):
        # Récupération du message
        message = self.__text.text()
        # Envoi du message au serveur
        client_socket.send(message.encode())
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{name}> {message}")
        # Affichage du message de confirmation dans la console
        print(f"Message {message} envoyé")

         # Commandes spéciales
        if message == "arret" or message == "quit" or message == "exit" or message == "kill":
            # Fermeture de la connexion
            client_socket.close()
            QCoreApplication.exit(0)
        elif message == "deco" or message == "disconnect" or message == "deconnexion" or message == "deconnect": 
            # Fermeture de la connexion côte client
            client_socket.close()
            QCoreApplication.exit(0)
        elif message == "reset":
            # Reset de la connexion côte serveur donc fermeture socket client
            client_socket.close()
            QCoreApplication.exit(0)
        elif message == "clear":
            # Effacement de la console
            self.sortie.setText("")
        else:
            # Réception du message du serveur
            data = client_socket.recv(10000).decode()
            # Affichage du message dans l'interface graphique
            self.sortie.append(f"{data}")
        # Effacement de la ligne d'entrée aprés l'envoi du message
        self.__text.setText("")
        self.__text.setFocus()

        # Commandes rapides de l'histotique en appuyant sur la touche haut
    def __actioncommandeavnt(self):
        message="commandeavant"
        # Envoi du message au serveur
        client_socket.send(message.encode())
        # Affichage du message dans la console
        print(f"Message {message} envoyé")
        # Réception du message du serveur
        data = client_socket.recv(10000).decode()
        # Affichage du message dans la ligne d'entrée
        self.__text.setText(data[:-1])

        # Commandes rapides
    def __actionram(self):
        # Envoi du message au serveur
        message = "ram"
        client_socket.send(message.encode())
        # Affichage du message dans la console
        self.sortie.append(f"{name}> {message}")
        # Affichage du message dans l'interface graphique
        print("Message ram envoyé")
        # Réception du message du serveur
        data = client_socket.recv(10000).decode()
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{data}")

    def __actioncpu(self):
        message = "cpu"
        # Envoi du message au serveur
        client_socket.send(message.encode())
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{name}> {message}")
        # Affichage du message dans la console
        print("Message cpu envoyé")
        # Réception du message du serveur
        data = client_socket.recv(10000).decode()
        # Affichage du message dans l'interface graphique 
        self.sortie.append(f"{data}")

    def __actionip(self):
        message = "ip"
        # Envoi du message au serveur
        client_socket.send(message.encode())
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{name}> {message}")
        # Affichage du message dans la console
        print("Message ip envoyé")
        # Réception du message du serveur
        data = client_socket.recv(10000).decode()
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{data}")

    def __actionos(self):
        message = "os"
        # Envoi du message au serveur
        client_socket.send(message.encode())
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{name}> {message}")
        # Affichage du message dans la console
        print("Message os envoyé")
        # Réception du message du serveur
        data = client_socket.recv(10000).decode()
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{data}")

    def __actionname(self):
        message = "name"
        # Envoi du message au serveur
        client_socket.send(message.encode())
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{name}> {message}")
        # Affichage du message dans la console
        print("Message name envoyé")
        # Réception du message du serveur
        data = client_socket.recv(10000).decode()
        # Affichage du message dans l'interface graphique
        self.sortie.append(f"{data}")

    # Commandes pour quitter le serveur et le client
    def __actionQUIT(self):
        message = "arret"
        # Boite de dialogue pour quitter
        box = QMessageBox(self)
        box.setWindowTitle("Question")
        box.setText("Voulez-vous vraiment quitter ?")
        box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # Style de la boite de dialogue
        box.setStyleSheet("""
            QPushButton {
                width: 80px;
            }
            QPushButton:hover {
                background-color: rgba(159, 215, 255, 0.756);
                color:red;
            }""")
        box.setIcon(QMessageBox.Icon.Question)
        # Execution de la boite de dialogue
        button = box.exec()

        # Si on clique sur oui alors on quitte
        if button == QMessageBox.StandardButton.Yes:
            # Envoi du message au serveur
            client_socket.send(message.encode())
            # Fermeture de la socket client
            client_socket.close()
            # Fermeture de l'application
            QCoreApplication.exit(0)
            # Affichage du message de confirmation dans la console
            print("Message arret envoyé")
            print("Socket client fermé")
        # Sinon on ne fait rien
        else:
            # Affichage du message de confirmation dans la console
            print("No!")


    # Commande pour reset le serveur
    def __actiondisc(self):
        message = "disconnect"

        # Boite de dialogue pour quitter
        box = QMessageBox(self)
        box.setWindowTitle("Question")
        box.setText("Voulez-vous vraiment vous déconnecter ?")
        box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        # Style de la boite de dialogue
        box.setStyleSheet("""
            QPushButton {
                width: 80px;
            }
            QPushButton:hover {
                background-color: rgba(159, 215, 255, 0.756);
                color:red;
            }
            """)
         # Icone de la boite de dialogue
        box.setIcon(QMessageBox.Icon.Question)
        # Affichage de la boite de dialogue
        button = box.exec()

        # Si on clique sur oui alors on quitte
        if button == QMessageBox.StandardButton.Yes:
            # On envoie le message de déconnexion au serveur
            client_socket.send(message.encode())
            # On ferme la socket client
            print("Message disconnect envoyé")
            client_socket.close()
            # On quitte l'application 
            QCoreApplication.exit(0)
            # On affiche un message sur la console pour dire que la socket est fermée
            print("Message deconnecter envoyé")
            print("Socket client fermé")
        # Sinon on ne fait rien
        else:
            print("No!")
            pass



    def __actionreset(self):
        message = "reset"
        
        # Boite de dialogue pour quitter
        box = QMessageBox(self)
        box.setWindowTitle("Question")
        #  Texte de la boite de dialogue
        box.setText("Voulez-vous vraiment reset le serveur ?")
        # Boutons de la boite de dialogue yes et no
        box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # Style de la boite de dialogue
        box.setStyleSheet("""
            QPushButton {
                width: 80px;
            }
            QPushButton:hover {
                background-color: rgba(159, 215, 255, 0.756);
                color:red;
            }""")
        box.setIcon(QMessageBox.Icon.Question)
        # Affichage de la boite de dialogue
        button = box.exec()
        # Si on clique sur oui alors on quitte
        if button == QMessageBox.StandardButton.Yes:
            # Envoi du message au serveur
            client_socket.send(message.encode())
            # Affichage du message de confirmation dans la console
            print("Message reset envoyé")
            print("Socket client fermé")
            # Fermeture de la socket client et de l'application
            client_socket.close()
            QCoreApplication.exit(0)
        else:
            print("No!")
        
        


if __name__ == '__main__':
    # On récupère l'adresse IP et le port du serveur
    name = socket.gethostname()
    # Ouverture du fichier contenant l'adresse IP et le port du serveur
    fch = open('access.txt', 'r')
    # Lecture du fichier
    ipadd = fch.read()
    # Fermeture du fichier
    fch.close()
    # Affichage de l'adresse IP et du port du serveur
    print("Access :", ipadd)
    # On récupère l'adresse ip du serveur
    host = ipadd.split()[0]
    # On récupère le port du serveur
    port = int(ipadd.split()[1])
    # On récupère l'adresse ip du serveur 2
    host1 = ipadd.split()[2]
    # On récupère le port du serveur 2
    port1 = int(ipadd.split()[3])
    # On remet ensmble l'adresse IP et le port du serveur chacun dans une variable
    ip1 = host+ ":" + str(port)
    ip2 = host1 + ":" + str(port1)

    # On crée une socket client
    app2 = QApplication(sys.argv)
    # Affichage de la fenêtre de connexion
    box = QMessageBox()
    # style de la boite de dialogue
    box.setStyleSheet("""
        QWidget {
            width: 400px;
            background-color: #666666;
            color: "white";
            font-size: 13px;
            font-family: 'Verdana';
        }
        QPushButton {
            background-color: #4d4d4d;
            color: "white";
            font-size: 13px;
            border: 1px solid white;
            border-radius: 2px;
            padding: 3px;
        }
        QPushButton:hover {
            background-color: rgba(159, 215, 255, 0.756);
            color: "white";
            font-size: 16px;
        }
        QLabel {
        color: "white";
        font-size: 20px;
        text-align: center;
    
        }
        """)
  
    # Boite de dialogue pour choisir le serveur
    box.setWindowTitle("Question")
    # On ajoute le texte
    box.setText("Voulez-vous vous connecter au serveur 1 ou 2 ?")
    # On ajoute les boutons
    box.addButton(QPushButton("Serveur 1 : " + ip1), QMessageBox.ButtonRole.YesRole)
    box.addButton(QPushButton("Serveur 2 : " + ip2), QMessageBox.ButtonRole.NoRole)

    button = box.exec()
    #  Si on clique sur oui alors on choisit le serveur 1
    if button == 0:
        host = host
        port = port
        print("Serveur 1")
    # Sinon on choisit le serveur 2
    else:
        host = host1
        port = port1
        print("Serveur 2")

    # On crée une fenêtre  
    window = MainWindow()
    #  On crée une socket client
    client_socket = socket.socket()
    #  On se connecte au serveur
    client_socket.connect((host, port))
    #  On affiche un message sur la console pour dire que la socket est créée
    print("Socket créé")
    print("Connecté au serveur.")

    # On récupère le style de la fenêtre
    with open("style.css","r") as file:
        window.setStyleSheet(file.read())

    # On affiche la fenêtre
    window.show()
    app2.exec()




