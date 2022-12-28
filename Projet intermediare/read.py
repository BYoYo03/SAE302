fch = open('access.txt', 'r')
ipadd = fch.read()
fch.close()
print(ipadd)
ipadd1 = ipadd.split()[0]
print(ipadd1)
port = int(ipadd.split()[1])
print(port)
