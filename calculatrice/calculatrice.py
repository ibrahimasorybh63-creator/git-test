# main.py
import math

def addition(a,b):
	return a + b

def soustraction(a,b):
	return a - b 
	
def multiplication(a,b):
	return a * b

def division(a,b):
	if b == 0:
		raise ValueError("Erreur , division par 0 impossible")
	return a / b

def puissance(a,b):
	return a**b

print(" --- CALCULATRICE PYTHON --- ")
print(" 1: addition")
print(" 2: soustraction")
print(" 3: multiplication")
print(" 4: division")
print(" 5: puissance")
print(" 6: racine carré")
print(" 0: Quitter")

while True:
	choix = input("Choisis un une operation (0-6):")
	if choix == "0":
		print("bye , bye ")
		break
	if choix in ["1","2","3","4","5"]:
		a = float(input("Entrez le premier nombre : "))
		b = float(input("Entrez le second nombre :  "))
		
	if choix == "1":
		print("Résultat : " ,addition(a,b))
	elif choix == "2":
		print("Résultat : " ,soustraction(a,b))
	elif choix =="3":
		print("Résultat : " , multiplication(a,b))
	elif choix == "4":
		print("Résultat : " , division(a,b))
	elif choix == "5":
		print("Résultat : " , puissance(a,b))
	elif  choix == "6":
		a = float(input("Entrez un nombre:"))
		print("Résultat : ",  math.sqrt(a))
	else:
		print(" Choix invalide, réesaie ")
	
