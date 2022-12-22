import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPalette
import socket


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        widget1 = QWidget()
        self.setCentralWidget(widget1)
        grid = QGridLayout()
        widget1.setLayout(grid)
 

        lab = QLabel("Connexion information : Socket sur l'adresse {} et le port {}".format(host, port))
        self.__lab = QLabel("Saisir une commande")
        self.__text = QLineEdit("")
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


        # Ajouter les composants au grid ayout
        grid.addWidget(lab, 0, 2,)
        grid.addWidget(self.__text, 10, 0, 1 , 3)
        grid.addWidget(self.sortie, 1, 2,8,10)
        grid.addWidget(entrer, 10, 5,)
        grid.addWidget(ramB, 2, 0)
        grid.addWidget(cpuB, 3, 0)
        grid.addWidget(ipB, 4, 0)
        grid.addWidget(osB, 5, 0)
        grid.addWidget(nameB, 6, 0)
        grid.addWidget(disc, 7, 0)
        grid.addWidget(QUIT, 8, 0)
        grid.addWidget(reset, 9, 0)

        entrer.clicked.connect(self.__actionentrer)
        ramB.clicked.connect(self.__actionram)
        cpuB.clicked.connect(self.__actioncpu)
        ipB.clicked.connect(self.__actionip)
        osB.clicked.connect(self.__actionos)
        nameB.clicked.connect(self.__actionname)
        QUIT.clicked.connect(self.__actionQUIT)
        disc.clicked.connect(self.__actiondisc)
        reset.clicked.connect(self.__actionreset)

        self.setWindowTitle("SAE302")

    def __actionentrer(self):
        message = self.__text.text()
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message envoyé")
        if message == "arret":
            client_socket.close()
            QCoreApplication.exit(0)
        else:
            data = client_socket.recv(10000).decode()
            self.sortie.append(f"{data}")

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
        client_socket.send(message.encode())
        client_socket.close()
        QCoreApplication.exit(0)


    def __actiondisc(self):
        message = "disconnect"
        client_socket.send(message.encode())
        client_socket.close()
        QCoreApplication.exit(0)


    def __actionreset(self):
        message = "reset"
        client_socket.send(message.encode())
        print("Message reset envoyé")
        client_socket.close()
        QCoreApplication.exit(0)


if __name__ == '__main__':
    name = socket.gethostname()
    app = QApplication(sys.argv)
    port = 1224
    client_socket = socket.socket()
    print("Socket créé.")
    host = "localhost"
    client_socket.connect((host, port))
    print("Connecté au serveur.")
    window = MainWindow()
    window.show()
    app.exec()




