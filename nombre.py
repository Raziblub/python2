import random

nombre_a_trouver=random.randint(1, 100)
nombre=0
coup=0

while (nombre != nombre_a_trouver):
    nombre = input("entrez un nombre : ")
    nombre = int(nombre)
    coup += 1
    if (nombre > nombre_a_trouver ):
        print ("trop grand") 
    if (nombre < nombre_a_trouver ):
        print ("trop petit") 

print ("bravo ! tu as trouvé en",coup,"coups")
