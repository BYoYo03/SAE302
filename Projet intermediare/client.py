import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import socket
import psutil
import platform


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Socket sur l'adresse {} et le port {}".format(host, port))
        labrien = QLabel("________________________________")
        self.__lab = QLabel("Saisir une commande")
        self.__text = QLineEdit("")
        self.lab2 = QLabel("")
        entrer = QPushButton("Entrer")
        ramB = QPushButton("RAM")
        cpuB = QPushButton("CPU")
        ipB = QPushButton("IP")
        osB = QPushButton("OS")
        nameB = QPushButton("name")
        QUIT = QPushButton("Disconnect")



        # Ajouter les composants au grid ayout
        grid.addWidget(lab, 0, 0)
        grid.addWidget(labrien, 0, 1)
        grid.addWidget(self.__text, 2, 0)
        grid.addWidget(self.lab2, 1, 1)
        grid.addWidget(entrer, 3, 0)
        grid.addWidget(ramB, 4, 0)
        grid.addWidget(cpuB, 5, 0)
        grid.addWidget(ipB, 6, 0)
        grid.addWidget(osB, 7, 0)
        grid.addWidget(nameB, 8, 0)
        grid.addWidget(QUIT, 9, 0)

        entrer.clicked.connect(self.__actionentrer)
        ramB.clicked.connect(self.__actionram)
        cpuB.clicked.connect(self.__actioncpu)
        ipB.clicked.connect(self.__actionip)
        osB.clicked.connect(self.__actionos)
        nameB.clicked.connect(self.__actionname)
        QUIT.clicked.connect(self.__actionQUIT)

        self.setWindowTitle("SAE302")

    def __actionentrer(self):
        message = self.__text.text()
        client_socket.send(message.encode())
        print("Message envoyé")
        if message == "arret" or "bye":
            client_socket.close()
            QCoreApplication.exit(0)
        data = client_socket.recv(1024).decode()
        self.lab2.setText(f"{data}")

    def __actionram(self):
        message = "ram"
        client_socket.send(message.encode())
        print("Message ram envoyé")
        data = client_socket.recv(1024).decode()
        self.lab2.setText(f"{data}")

    def __actioncpu(self):
        message = "cpu"
        client_socket.send(message.encode())
        print("Message cpu envoyé")
        data = client_socket.recv(1024).decode()
        self.lab2.setText(f"{data}")

    def __actionip(self):
        message = "ip"
        client_socket.send(message.encode())
        print("Message ip envoyé")
        data = client_socket.recv(1024).decode()
        self.lab2.setText(f"{data}")

    def __actionos(self):
        message = "os"
        client_socket.send(message.encode())
        print("Message os envoyé")
        data = client_socket.recv(1024).decode()
        self.lab2.setText(f"{data}")

    def __actionname(self):
        message = "name"
        client_socket.send(message.encode())
        print("Message name envoyé")
        data = client_socket.recv(1024).decode()
        self.lab2.setText(f"{data}")

    def __actionQUIT(self):
        message = "arret"
        client_socket.send(message.encode())
        print("Message QUIT envoyé")
        client_socket.close()
        QCoreApplication.exit(0)





if __name__ == '__main__':
    client_socket = socket.socket()
    print("Socket créé.")
    host = "localhost"
    port = 1111
    client_socket.connect((host, port))
    print("Connecté au serveur.")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()



