#!/usr/bin/python


print ("\n### Cadenas de texto ###")
print("En python 3 no hace falta usar coding=utf-8 pero hay que añadir los paréntesis en print ('cadena')")

# cadenas normales
c = 'áèïóù'
print ("áèïóù" , type(c))
# cadenas unicode
c = u'áèïóù'
print ("u'áèïóù'" , type(c))
# cadenas raw
r = r"\n"
print ("r\"\\n\"= " + r)

# cadenas con varias lineas triple comilla
s = """
         Ésto
     parece texto
       centrado
    """
print (s)

# concatenar y multiplicar cadenas

c1 = "Hola"
c2 = " Mundo "
s = c1 + c2
print (s)

s = (c1 + c2) * 3
print (s)
