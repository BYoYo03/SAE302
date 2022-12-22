import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPalette
import socket

"""import os

#ls = os.system('dir', )
#print(f"-------------------> {ls}")

recv = "Powershell:ls"
se="Powershell"
cmd = "dir"
l = os.system(cmd)
print(f"-----------> {l}")

if l == 0:
    ls = os.popen(cmd).read()
    print(f"-----------> {ls}")
else:
    print(f"Erreur d'éxcution de la command {cmd}")

#print(os.system('get-process'))

#print(os.listdir())
##print(os.getcwd())

elif data.startswith("DOS:mkdir "):
data1 = data.split()[1]
os.mkdir(data1)
reply = str(f"Le dossier {data1} a été créé")
conn.send(reply.encode())
print("Message envoyé")
data = conn.recv(1024).decode()
print("Message reçue du client:")
print(data)

elif data == "Linux:ls":
data2 = os.listdir()
reply = str(f"Les fichiers dans le dossier sont: {data2}")
conn.send(reply.encode())
print("Message envoyé")
data = conn.recv(1024).decode()
print("Message reçue du client:")
print(data)

elif data == "Linux:ls":
data2 = os.listdir()
reply = str(f"Les fichiers dans le dossier sont: {data2}")
conn.send(reply.encode())
print("Message envoyé")
data = conn.recv(1024).decode()
print("Message reçue du client:")
print(data)

def serveur():
    msg = ""
    conn = None
    server_socket = None
    while msg != "kill" :
        msg = ""
        server_socket = socket.socket()
         options qui permette de réutiliser l'adresse et le port rapidement
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server_socket.bind(("localhost", 15001))

        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            msg = ""
            try :
                conn, addr = server_socket.accept()
                print (addr)
            except ConnectionError:
                print ("erreur de connection")
                break
            else :
                while msg != "kill" and msg != "reset" and msg != "disconnect":
                    msg = conn.recv(1024).decode()
                    print ("Received from client: ", msg)
                    # msg = input('Enter a message to send: ')
   
                    le serveur va ici récupere les commandes du client et lui renvoyer. Dans la suite de la SAÉ, 
                    le serveur fera pareil mais en renvoyant le résultat des commandes demandées par le client.

                    conn.send(msg.encode())
                conn.close()
        print ("Connection closed")
        server_socket.close()
        print ("Server closed")

"""

box = QMessageBox()
box.setWindowTitle("Reconnexion ?")
box.setText("Voulez vous reconnecter au serveur ?")
box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
ret = box.exec()
    if ret == QMessageBox.setStandardButtons.Yes:
        message = "reco"
        client_socket.send(message.encode())
        print("Message envoyé")
        data = client_socket.recv(10000).decode()
    else:
        client_socket.send(message.encode())
        client_socket.close()
        QCoreApplication.exit(0)