import socket


client_socket = socket.socket()
print("Socket créé.")
host = "localhost"
port = 1111
client_socket.connect((host, port))
print("Connecté au serveur.")
message =input("envoi d'un message : ")
client_socket.send(message.encode())
print("Message envoyé")

if message == "arret" or message == "bye":
    print("Connexion terminé.")
    client_socket.close()
else:
    data = client_socket.recv(1024).decode()
    print("Message reçu du serveur:")
    print(data)
    if data == "arret":
        print("Connexion terminé.")
        client_socket.close()
    else:
        while data !="bye":
            message = input("envoi d'un message : ")
            client_socket.send(message.encode())
            print("Message envoyé")
            if message == "arret" or message == "bye":
                print("Connexion terminé.")
                client_socket.close()
                break
            data = client_socket.recv(1024).decode()
            print("Message reçu du serveur:")
            print(data)
            if data == "arret":
                print("Connexion terminé.")
                client_socket.close()
                break

client_socket.close()