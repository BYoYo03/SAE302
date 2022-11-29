import socket
import psutil
import platform

os1 = platform.release()
os = platform.system()
name = socket.gethostname()
ipadd = socket.gethostbyname(name)
cpu = psutil.cpu_percent(4)
ram = psutil.virtual_memory()[0] / 1000000000
ram1 = psutil.virtual_memory()[3] / 1000000000
ram2 = psutil.virtual_memory()[4] / 1000000000

server_socket = socket.socket()
print("Socket crée.")
host = "localhost"
port = 1111
server_socket.bind((host, port))
print("Socket sur l'adresse {} et le port {}".format(host, port))
server_socket.listen(5)

print("En attente du client")
conn, address = server_socket.accept()
print("Conexion établie au client {}".format(address))

data = conn.recv(1024).decode()
print("Message received from the client:")
print(data)

while data !="arret":

    if data =="os":
        reply = str(f"Sserveur 1 : {os} {os1}")
        conn.send(reply.encode())
        print("Message envoyé")
        data = conn.recv(1024).decode()
        print("Message reçue du client:")
        print(data)

    elif data == "ram":
        reply = str(f"Serveur 1 : Ram Total : {round(ram, 2)} Go\nRam utilisé : {round(ram1,0)} Go\nRam libre: {round(ram2,2)} Go")
        conn.send(reply.encode())
        print("Message envoyé")
        data = conn.recv(1024).decode()
        print("Message reçue du client:")
        print(data)

    elif data == "cpu":
        reply = str(f"Serveur 1 : CPU utilisé : {cpu} %")
        conn.send(reply.encode())
        print("Message envoyé")
        data = conn.recv(1024).decode()
        print("Message reçue du client:")
        print(data)

    elif data =="ip":
        reply = str(f"Serveur 1 : L'adresse ip est : {ipadd}")
        conn.send(reply.encode())
        print("Message envoyé")
        data = conn.recv(1024).decode()
        print("Message reçue du client:")
        print(data)

    elif data =="name":
        reply = str(f"Serveur 1 : Le nom de la machine est: {name}")
        conn.send(reply.encode())
        print("Message envoyé")
        data = conn.recv(1024).decode()
        print("Message reçue du client:")
        print(data)

    else:
        reply = ""
        conn.send(reply.encode())
        print("Message envoyé")
        data = conn.recv(1024).decode()
        print("Message reçue du client:")
        print(data)

print("Connexion terminé.")
conn.close()




