import socket
import psutil
import platform
import os
from platform import python_version


if __name__ == '__main__':
    os1 = platform.release()
    os3 = platform.system()
    name = socket.gethostname()
    ipadd = socket.gethostbyname(name)
    cpu = psutil.cpu_percent(4)
    ram = psutil.virtual_memory()[0] / 1000000000
    ram1 = psutil.virtual_memory()[3] / 1000000000
    ram2 = psutil.virtual_memory()[4] / 1000000000

    server_socket = socket.socket()
    print("Socket crée.")
    host = "localhost"

    port = 1222
    server_socket.bind((host, port))
    print("Socket sur l'adresse {} et le port {}".format(host, port))
    server_socket.listen(5)

    print("En attente du client")
    conn, address = server_socket.accept()
    print("Connexion établie au client {}".format(address))

    data = conn.recv(1024).decode()
    print("Message reçue du client:")
    print(data)

    while data !="arret":

        if data =="os" or data =="OS":
            reply = str(f"Sserveur 1 : {os3} {os1}")
            conn.send(reply.encode())
            print("Message envoyé")
            data = conn.recv(1024).decode()
            print("Message reçue du client:")
            print(data)

        elif data == "ram"or data =="RAM":
            reply = str(f"Serveur 1 : Ram Total : {round(ram, 2)} Go\nRam utilisé : {round(ram1,0)} Go\nRam libre: {round(ram2,2)} Go")
            conn.send(reply.encode())
            print("Message envoyé")
            data = conn.recv(1024).decode()
            print("Message reçue du client:")
            print(data)

        elif data == "cpu" or data =="CPU":
            reply = str(f"Serveur 1 : CPU utilisé : {cpu} %")
            conn.send(reply.encode())
            print("Message envoyé")
            data = conn.recv(1024).decode()
            print("Message reçue du client:")
            print(data)

        elif data =="ip" or data == "IP":
            reply = str(f"Serveur 1 : L'adresse ip est : {ipadd}")
            conn.send(reply.encode())
            print("Message envoyé")
            data = conn.recv(1024).decode()
            print("Message reçue du client:")
            print(data)

        elif data =="name" or data =="Name":
            reply = str(f"Serveur 1 : Le nom de la machine est: {name}")
            conn.send(reply.encode())
            print("Message envoyé")
            data = conn.recv(1024).decode()
            print("Message reçue du client:")
            print(data)

        elif data =="python --version":
            reply = str(f"La version de python qu'on utilise actullement est la {python_version()}")
            conn.send(reply.encode())
            print("Message envoyé")
            data = conn.recv(1024).decode()
            print("Message reçue du client:")
            print(data)

        else:
            cmd = data
            ps = os.system(cmd)
            print("ps",ps)
            ls = os.popen(cmd).read()
            if ps == 0:
                conn.send(ls.encode())
            else:
                cmd = (f"Erreur d'éxcution de la commande {data}, n'existe pas sur le shell windows")
                conn.send(cmd.encode())
            print("Message envoyé")
            data = conn.recv(1024).decode()
            print("Message reçue du client:")
            print(data)

    print("Connexion terminé.")
    conn.close()

    """
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
    
        elif data.startswith("ping"):
            ip = data.split()[1]
            result = os.system("ping -c 1" + ip)
            if result == 0:
                conn.send("{} atteint".format(ip).encode())
            else:
                conn.send("inconnu".encode())
    """


