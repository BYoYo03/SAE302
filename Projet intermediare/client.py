import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QShortcut, QKeySequence
import socket


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        widget1 = QWidget()
        self.setCentralWidget(widget1)
        grid = QGridLayout()
        widget1.setLayout(grid)


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

        
        # Style des composants
        QUIT.setStyleSheet("""
            QPushButton {
                background-color: rgba(159, 215, 255, 0.756);
                }
            QPushButton:hover {
                color: "red";
                }""")
        disc.setStyleSheet("""
            QPushButton {
                background-color: rgba(159, 215, 255, 0.756);
                }
            QPushButton:hover {
                color: "Orange";
                }""")
        reset.setStyleSheet("""
            QPushButton {
                background-color: rgba(159, 215, 255, 0.756);
                }
            QPushButton:hover {
                color: "Yellow";
                }""")
        
        entrer.setStyleSheet("""
            QPushButton {
                width: 80px;
            }""")

        # Ajouter les composants au grid ayout
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


        entrer.clicked.connect(self.__actionentrer)
        entrerpress = QShortcut(QKeySequence("Return"), self)
        entrerpress.activated.connect(self.__actionentrer)
        quitter = QShortcut(QKeySequence("Esc"), self)
        quitter.activated.connect(self.__actionQUIT)
        commandeavnt = QShortcut(QKeySequence("Up"), self)
        commandeavnt.activated.connect(self.__actioncommandeavnt)
        ramB.clicked.connect(self.__actionram)
        cpuB.clicked.connect(self.__actioncpu)
        ipB.clicked.connect(self.__actionip)
        osB.clicked.connect(self.__actionos)
        nameB.clicked.connect(self.__actionname)
        QUIT.clicked.connect(self.__actionQUIT)
        disc.clicked.connect(self.__actiondisc)
        reset.clicked.connect(self.__actionreset)

        self.setWindowTitle("Client")


    def __actionentrer(self):
        message = self.__text.text()
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print(f"Message {message} envoyé")
        if message == "arret" or message == "quit" or message == "exit" or message == "kill":
            client_socket.close()
            QCoreApplication.exit(0)
        elif message == "deco" or message == "disconnect" or message == "deconnexion" or message == "deconnect": 
            client_socket.close()
            QCoreApplication.exit(0)
        elif message == "reset":
            client_socket.close()
            QCoreApplication.exit(0)
        elif message == "clear":
            self.sortie.setText("")
        else:
            data = client_socket.recv(10000).decode()
            self.sortie.append(f"{data}")
        self.__text.setText("")
        self.__text.setFocus()

    def __actioncommandeavnt(self):
        message="commandeavant"
        client_socket.send(message.encode())
        print(f"Message {message} envoyé")
        data = client_socket.recv(10000).decode()
        self.__text.setText(data[:-1])

    def __actionram(self):
        message = "ram"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message ram envoyé")
        data = client_socket.recv(10000).decode()
        self.sortie.append(f"{data}")

    def __actioncpu(self):
        message = "cpu"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message cpu envoyé")
        data = client_socket.recv(10000).decode()
        self.sortie.append(f"{data}")

    def __actionip(self):
        message = "ip"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message ip envoyé")
        data = client_socket.recv(10000).decode()
        self.sortie.append(f"{data}")

    def __actionos(self):
        message = "os"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message os envoyé")
        data = client_socket.recv(10000).decode()
        self.sortie.append(f"{data}")

    def __actionname(self):
        message = "name"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message name envoyé")
        data = client_socket.recv(10000).decode()
        self.sortie.append(f"{data}")

    def __actionQUIT(self):
        message = "arret"
        box = QMessageBox(self)
        box.setWindowTitle("Question")
        box.setText("Voulez-vous vraiment quitter ?")
        box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        box.setStyleSheet("""
            QPushButton {
                width: 80px;
            }
            QPushButton:hover {
                background-color: rgba(159, 215, 255, 0.756);
                color:red;
            }""")
        box.setIcon(QMessageBox.Icon.Question)
        button = box.exec()
        if button == QMessageBox.StandardButton.Yes:
            client_socket.send(message.encode())
            client_socket.close()
            QCoreApplication.exit(0)
            print("Message arret envoyé")
            print("Socket client fermé")
        else:
            print("No!")


    def __actiondisc(self):
        message = "disconnect"
        
        box = QMessageBox(self)
        box.setWindowTitle("Question")
        box.setText("Voulez-vous vraiment vous déconnecter ?")
        box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        box.setStyleSheet("""
            QPushButton {
                width: 80px;
            }
            QPushButton:hover {
                background-color: rgba(159, 215, 255, 0.756);
                color:red;
            }
            """)

        box.setIcon(QMessageBox.Icon.Question)
        button = box.exec()
        if button == QMessageBox.StandardButton.Yes:
            client_socket.send(message.encode())
            print("Message disconnect envoyé")
            client_socket.close()
            QCoreApplication.exit(0)
            print("Message deconnecter envoyé")
            print("Socket client fermé")
        else:
            print("No!")
            pass



    def __actionreset(self):
        message = "reset"
        
        box = QMessageBox(self)
        box.setWindowTitle("Question")
        box.setText("Voulez-vous vraiment reset le serveur ?")
        box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        box.setStyleSheet("""
            QPushButton {
                width: 80px;
            }
            QPushButton:hover {
                background-color: rgba(159, 215, 255, 0.756);
                color:red;
            }""")
        box.setIcon(QMessageBox.Icon.Question)
        button = box.exec()
        if button == QMessageBox.StandardButton.Yes:
            client_socket.send(message.encode())
            print("Message reset envoyé")
            print("Socket client fermé")
            client_socket.close()
            QCoreApplication.exit(0)
        else:
            print("No!")
        
        


if __name__ == '__main__':
    name = socket.gethostname()
    fch = open('access.txt', 'r')
    ipadd = fch.read()
    fch.close()
    print("tout", ipadd)
    host = ipadd.split()[0]
    port = int(ipadd.split()[1])
    host1 = ipadd.split()[2]
    port1 = int(ipadd.split()[3])
    ip1 = host+ ":" + str(port)
    ip2 = host1 + ":" + str(port1)

    app2 = QApplication(sys.argv)
    box = QMessageBox()
    box.setStyleSheet("""
        QWidget {
            width: 400px;
            background-color: rgba(167, 173, 241, 0.669);
            color: "white";
            font-size: 13px;
            font-family: 'Verdana';

        }
        QPushButton {
            background-color: rgb(159, 215, 255);
            color: rgb(255, 159, 215);
            font-size: 13px;
            border: 2px solid white;
            border-radius: 5px;
            padding: 3px;

        }
        QPushButton:hover {
            background-color: rgb(159, 167, 255);
            color: "white";
            font-size: 16px;
        }
        
        
        QLabel {
        background-color: rgba(167, 173, 241, 0.669);
        color: "white";
        font-size: 20px;
        text-align: center;
    
        }
        """)
  

    box.setWindowTitle("Question")
    box.setText("Voulez-vous vous connecter au serveur 1 ou 2 ?")
    box.addButton(QPushButton("Serveur 1 : " + ip1), QMessageBox.ButtonRole.YesRole)
    box.addButton(QPushButton("Serveur 2 : " + ip2), QMessageBox.ButtonRole.NoRole)

    button = box.exec()
    if button == 0:
        host = host
        port = port
        print("Serveur 1")
    else:
        host = host1
        port = port1
        print("Serveur 2")

    window = MainWindow()
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Socket créé")
    print("Connecté au serveur.")

    with open("style.css","r") as file:
        window.setStyleSheet(file.read())

    window.show()
    app2.exec()




