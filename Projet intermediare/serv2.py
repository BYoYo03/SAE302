import socket
import psutil
import platform
import os
from platform import python_version


def serveur():
    os1 = platform.release()
    os3 = platform.system()
    name = socket.gethostname()
    cpu = psutil.cpu_percent(4)
    ram = psutil.virtual_memory()[0] / 1000000000
    ram1 = psutil.virtual_memory()[3] / 1000000000
    ram2 = psutil.virtual_memory()[4] / 1000000000

    data = ""
    while data != "arret":
        data = ""
        server_socket = socket.socket()
        print("Socket crée.")
        fch = open('access.txt', 'r')
        ipadd = fch.read()
        fch.close()
        print(ipadd)
        host = ipadd.split()[2]
        print(host)
        port = int(ipadd.split()[3])
        print(port)
        ipadd = socket.gethostbyname(host)
        server_socket.bind((host, port))
        print("Socket sur l'adresse {} et le port {}".format(host, port))
        server_socket.listen(5)
        print("En attente du client")

        while data != "arret" and data != "reset":
            data = ""
            conn, address = server_socket.accept()
            print("Connexion établie au client {}".format(address))
            while data != "arret" and data != "reset" and data != "disconnect":
                data = conn.recv(1024).decode()
                print("Message reçue du client:")
                print(data)
                if data =="os" or data =="OS":
                    reply = str(f"Serveur 2 : {os3} {os1}")
                    conn.send(reply.encode())
                    print("Message envoyé")

                elif data == "ram" or data =="RAM":
                    reply = str(f"Serveur 2 : Ram Total : {round(ram, 2)} Go\nRam utilisé : {round(ram1, 0)} Go\nRam libre: {round(ram2, 2)} Go")
                    conn.send(reply.encode())
                    print("Message envoyé")

                elif data == "cpu" or data =="CPU":
                    reply = str(f"Serveur 2 : CPU utilisé : {cpu} %")
                    conn.send(reply.encode())
                    print("Message envoyé")

                elif data =="ip" or data == "IP":
                    reply = str(f"Serveur 2 : L'adresse ip est : {ipadd}")
                    conn.send(reply.encode())
                    print("Message envoyé")

                elif data =="name" or data =="Name":
                    reply = str(f"Serveur 2 : Le nom de la machine est: {name}")
                    conn.send(reply.encode())
                    print("Message envoyé")

                elif data =="python --version":
                    reply = str(f"Serveur 2 : La version de python qu'on utilise actullement est la {python_version()}")
                    conn.send(reply.encode())
                    print("Message envoyé")

                elif data =="disc":
                    print("Le client s'est deconnecté")
                    print("Message envoyé")
                    data = ""

                elif data == "help" or data == "HELP":
                    fichier = open('help.txt', 'r')
                    reply = str(fichier.read())
                    conn.send(reply.encode())
                    fichier.close()
                    print("Message envoyé")

                elif data.startswith("ping"):
                    ip = data.split()[1]
                    print(ip)
                    result = os.system("ping -c 1 " + ip)
                    if result == 0:
                        conn.send("{} atteint".format(ip).encode())
                    else:
                        conn.send("inconnu".encode())

                else:
                    ps = os.system(data)
                    print("ps", ps)
                    ls = os.popen(data).read()
                    if ps != 0:
                        cmd = (f"Serveur 2 :Erreur d'éxcution de la commande {data}, n'existe pas sur cette os : {os3} {os1}")
                        conn.send(cmd.encode())
                    else:
                        conn.send(ls.encode())
                    print("Message envoyé")

        print("Connection closed")
        server_socket.close()
        print("Server fermé")

if __name__ == '__main__':
    serveur()

