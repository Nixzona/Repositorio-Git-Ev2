archi1=open("datos.txt","a")
archi1.write("nueva linea 1\n")
archi1.write("nueva linea 2\n")
archi1.close()
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()