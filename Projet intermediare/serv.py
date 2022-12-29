# Description: Programme qui permet de faire des commandes sur un serveur distant
import socket
import psutil
import platform
import os
from platform import python_version

# Fonction qui permet de créer le serveur

def serveur():
 
    # On récupère les informations des caractéristiques du serveur
    os1 = platform.release()
    os3 = platform.system()
    name = socket.gethostname()
    cpu = psutil.cpu_percent(4)
    ram = psutil.virtual_memory()[0] / 1000000000
    ram1 = psutil.virtual_memory()[3] / 1000000000
    ram2 = psutil.virtual_memory()[1] / 1000000000

    # On crée une boucle tant que le mot "arret" qui permet de garder le serveur en ligne
    data = ""  
    while data != "arret":
        data = ""
        # On crée le serveur
        server_socket = socket.socket()
        # On affiche sur la console ue le serveur est crée
        print("Socket crée.")
        # On ouvre le fichier qui contient l'adresse ip et le port
        fch = open('access.txt', 'r')
        ipadd = fch.read()
        fch.close()
        # On récupère l'adresse ip et le port
        host = ipadd.split()[0]
        port = int(ipadd.split()[1])
        # On récupère l'adresse ip
        ipadd = socket.gethostbyname(host)
        # On lie l'adresse ip et le port pour se connecter
        server_socket.bind((host, port))
        # On affiche sur la console l'adresse ip et le port
        print("Socket sur l'adresse {} et le port {}".format(host, port))
        # On met le serveur en écoute
        server_socket.listen(5)
        # On affiche sur la console que le serveur est en attente d'un client
        print("En attente du client")

        #  On crée une boucle tant que le mot "arret" ou "reset" qui permet de garder le serveur en ligne
        while data != "arret" and data != "reset":
            data = ""
            # On accepte la connexion du client
            conn, address = server_socket.accept()
            # On affiche sur la console que la connexion est établie
            print("Connexion établie au client {}".format(address))
            # On crée une boucle tant que le mot "arret" ou "reset" ou "disconnect" qui permet de garder le serveur en ligne
            while data != "arret" and data != "reset" and data != "disconnect":
                # On récupère les données du client
                data = conn.recv(1024).decode()
                # On affiche sur la console le message reçu du client
                print(f"Message reçue {data} du client:")
                # Si le message est os ou OS on envoie le nom de l'os
                if data =="os" or data =="OS":
                    # On envoie le nom de l'os
                    reply = str(f"Sserveur 1 : {os3} {os1}")
                    conn.send(reply.encode())
                    # On affiche sur la console que le message a été envoyé
                    print("Message envoyé")
                    # On ouvre le fichier qui contient l'historique des commandes
                    fichier = open('historique.txt', 'a')
                    # On écrit dans le fichier la commande envoyé
                    fichier.write(data + "\n")
                    # On affiche sur la console que le fichier a été écrit
                    print("fait")
                    # On ferme le fichier
                    fichier.close()

                #  Si le message est ram on envoie la ram du serveur
                elif data == "ram" or data =="RAM":
                    # On envoie la ram du serveur
                    reply = str(f"Serveur 1 : Ram Total : {round(ram, 2)} Go\nRam utilisé : {round(ram1, 0)} Go\nRam libre: {round(ram2, 2)} Go")
                    conn.send(reply.encode())
                    # On affiche sur la console que le message a été envoyé
                    print("Message envoyé")
                    # On ouvre le fichier qui contient l'historique des commandes
                    fichier = open('historique.txt', 'a')
                    # On écrit dans le fichier la commande envoyé
                    fichier.write(data + "\n")
                    # On affiche sur la console que le fichier a été écrit
                    print("fait")
                    # On ferme le fichier
                    fichier.close()

                #  Si le message est cpu on envoie le cpu du serveur
                elif data == "cpu" or data =="CPU":
                    # On envoie le cpu du serveur
                    reply = str(f"Serveur 1 : CPU utilisé : {cpu} %")
                    conn.send(reply.encode())
                    # On affiche sur la console que le message a été envoyé
                    print("Message envoyé")
                    # On ouvre le fichier qui contient l'historique des commandes
                    fichier = open('historique.txt', 'a')
                    # On écrit dans le fichier la commande envoyé
                    fichier.write(data + "\n")
                    # On affiche sur la console que le fichier a été écrit
                    print("fait")
                    # On ferme le fichier
                    fichier.close()

                #  Si le message est ip on envoie l'ip du serveur
                elif data =="ip" or data == "IP":
                    # On envoie l'ip du serveur
                    reply = str(f"Serveur 1 : L'adresse ip est : {ipadd}")
                    conn.send(reply.encode())
                    # On affiche sur la console que le message a été envoyé
                    print("Message envoyé")
                    # On ouvre le fichier qui contient l'historique des commandes
                    fichier = open('historique.txt', 'a')
                    # On écrit dans le fichier la commande envoyé
                    fichier.write(data + "\n")
                    # On affiche sur la console que le fichier a été écrit
                    print("fait")
                    # On ferme le fichier
                    fichier.close()
                    

                elif data =="name" or data =="Name":
                    reply = str(f"Serveur 1 : Le nom de la machine est: {name}")
                    conn.send(reply.encode())
                    print("Message envoyé")
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")
                    fichier.close()
                
                elif data =="clear" or data =="CLEAR":
                    os.system("clear")
                    print(f"Message {data} reçu")
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")
                    fichier.close()
                    
                elif data =="python --version":
                    reply = str(f"La version de python qu'on utilise actullement est la {python_version()}")
                    conn.send(reply.encode())
                    print("Message envoyé")
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")

                elif data =="disc":
                    print("Le client s'est deconnecté")
                    print("Message envoyé")
                    data = ""
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")
                    fichier.close()

                elif data == "help" or data == "HELP":
                    fichier = open('help.txt', 'r')
                    reply = str(fichier.read())
                    conn.send(reply.encode())
                    fichier.close()
                    print("Message envoyé")
                    fichier = open('historique.txt', 'w')
                    fichier.write(data + "\n")
                    print("fait")
                    fichier.close()


                elif data.startswith("ping "):
                    try: 
                        ip = data.split()[1]
                        print(ip)
                        result = os.system("ping -c 1 " + ip)
                        if result == 0:
                            ping = str(f"PING {ip} OK ")
                            conn.send(ping.encode())
                        else:
                            ping = str(f"PING {ip} FAIL ")
                            conn.send(ping.encode())
                        print("Message envoyé")
                        fichier = open('historique.txt', 'w')
                        fichier.write(data + "\n")
                        print("fait")
                        fichier.close()
                    except:
                        print("Erreur de saisie")
                        conn.send("Erreur de saisie".encode())
                        fichier = open('historique.txt', 'w')
                        fichier.write(data + "\n")
                        print("fait")
                        fichier.close()
                
                elif data == "commandeavant" or data == "COMMANDEAVANT":
                    fichier = open('historique.txt', 'r')
                    with open('historique.txt', 'r') as f:
                        last_line = f.readlines()[-1]
                    conn.send(last_line.encode())
                    fichier.close()
                    print(f"Message {last_line} envoyé")

                elif data == "reset" or data == "RESET":
                    print("Reset du serveur")
                    print("Message envoyé")
                    data = "reset"
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")
                
                elif data == "arret" or data == "ARRET":
                    print("Le client et le serveur sont deconnectés")
                    print("Message envoyé")
                    data = "arret"
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")

                
                elif data == "disconnect" or data == "DISCONNECT":
                    print("Le client s'est deconnecté")
                    print("Message envoyé")
                    data = ""
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")
                    break
                
                else :
                    ps = os.system(data)
                    print("ps", ps)
                    ls = os.popen(data).read()
                    if ps != 0:
                        cmd = (f"Erreur d'éxcution de la commande {data}, n'existe pas sur cette os : {os3} {os1}")
                        conn.send(cmd.encode())
                    else:
                        conn.send(ls.encode())
                    print("Message envoyé")
                    fichier = open('historique.txt', 'a')
                    fichier.write(data + "\n")
                    print("fait")
                    fichier.close()
        
        print("Connexion fermé")
        server_socket.close()
        print("Socket fermé")
    

if __name__ == '__main__':
    serveur()


