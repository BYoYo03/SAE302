import os

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