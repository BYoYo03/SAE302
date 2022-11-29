import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import socket
import psutil
import platform
from PyQt5.QtGui import QPalette

name = socket.gethostname()


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        qp = QPalette()
        qp.setColor(QPalette.ButtonText, Qt.black)
        qp.setColor(QPalette.Window, Qt.lightGray)
        qp.setColor(QPalette.Button, Qt.darkGray)
        qp.setColor(QPalette.Text, Qt.black)


        app.setPalette(qp)

        lab = QLabel("Socket sur l'adresse {} et le port {}".format(host, port))
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



        # Ajouter les composants au grid ayout
        grid.addWidget(lab, 0, 2,)
        grid.addWidget(self.__text, 9, 0, 1 , 3)
        grid.addWidget(self.sortie, 1, 2,8,10)
        grid.addWidget(entrer, 9, 5,)
        grid.addWidget(ramB, 2, 0)
        grid.addWidget(cpuB, 3, 0)
        grid.addWidget(ipB, 4, 0)
        grid.addWidget(osB, 5, 0)
        grid.addWidget(nameB, 6, 0)
        grid.addWidget(disc, 7, 0)
        grid.addWidget(QUIT, 8, 0)

        entrer.clicked.connect(self.__actionentrer)
        ramB.clicked.connect(self.__actionram)
        cpuB.clicked.connect(self.__actioncpu)
        ipB.clicked.connect(self.__actionip)
        osB.clicked.connect(self.__actionos)
        nameB.clicked.connect(self.__actionname)
        QUIT.clicked.connect(self.__actionQUIT)
        disc.clicked.connect(self.__actiondisc)

        self.setWindowTitle("SAE302")

    def __actionentrer(self):
        message = self.__text.text()
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message envoyé")
        if message == "arret":
            client_socket.close()
            QCoreApplication.exit(0)
        elif message == "ram" or message =="RAM" :
            print("Message ram envoyé")
            data = client_socket.recv(1024).decode()
            self.sortie.append(f"{data}")
        elif message == "os" or message =="OS":
            print("Message os envoyé")
            data = client_socket.recv(1024).decode()
            self.sortie.append(f"{data}")

        elif message == "cpu" or message =="CPU":
            print("Message cpu envoyé")
            data = client_socket.recv(1024).decode()
            self.sortie.append(f"{data}")

        elif message == "name" or message =="Name":
            print("Message name envoyé")
            data = client_socket.recv(1024).decode()
            self.sortie.append(f"{data}")

        elif message == "ip" or message =="IP":
            print("Message ip envoyé")
            data = client_socket.recv(1024).decode()
            self.sortie.append(f"{data}")
        else:
            pass


    def __actionram(self):
        message = "ram"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message ram envoyé")
        data = client_socket.recv(1024).decode()
        self.sortie.append(f"{data}")

    def __actioncpu(self):
        message = "cpu"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message cpu envoyé")
        data = client_socket.recv(1024).decode()
        self.sortie.append(f"{data}")

    def __actionip(self):
        message = "ip"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message ip envoyé")
        data = client_socket.recv(1024).decode()
        self.sortie.append(f"{data}")

    def __actionos(self):
        message = "os"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message os envoyé")
        data = client_socket.recv(1024).decode()
        self.sortie.append(f"{data}")

    def __actionname(self):
        message = "name"
        client_socket.send(message.encode())
        self.sortie.append(f"{name}> {message}")
        print("Message name envoyé")
        data = client_socket.recv(1024).decode()
        self.sortie.append(f"{data}")

    def __actionQUIT(self):
        message = "arret"
        client_socket.send(message.encode())
        print("Message QUIT envoyé")
        client_socket.close()
        QCoreApplication.exit(0)

    def __actiondisc(self):
        pass

if __name__ == '__main__':
    a = int(input("Tapez 1 (Serveur 1) ou 2 (Serveur 2) : "))

    if a == 1:
        port = 1222
    else:
        port = 1223
    client_socket = socket.socket()
    print("Socket créé.")
    host = "localhost"
    client_socket.connect((host, port))
    print("Connecté au serveur.")
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec()



