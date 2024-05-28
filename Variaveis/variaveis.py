print ("Variáveis: ")

x = 5
y = "Eli"

print (x)
print (y)

print ("\nTroca do valor das variáveis: ")
print (x) 
print ("'x' equivale a uma variável INTEIRA!")
x = "Eli"
print (x)
print ("Agora 'x' equivale a uma STRING\n")

print ("Especificando o tipo de uma variável: \n")
x = str(3)
y = int(3)
z = float(3)
print (x)
print (y)
print (z)
print(" X = String")
print (" Y = Inteiro")
print (" Z = Float\n")

print("Obtendo o Tipo de Dado de uma variável: \n")

print (type(x))
print(type(y))
print (type(z))

print("\nAtribuindo múltiplos valores em uma linha: ")
x, y, z = "Laranja", 155, 3.14
print (x)
print (y)
print (z)

print("\nAtribuindo múltiplos a uma MESMA variável em uma linha: ")
x = y = z = "Banana"
print (x)
print (y)
print (z)

print ("\nDescompactaçao: ")
frutas = ["Banana", "Cereja", "Melao"]
x, y, z = frutas
print (x)
print (y)
print (z)