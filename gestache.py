print(" ----- Gestionnaire De Tâche Python -----")

try:
	with open("text.txt","r") as file:
		f = [x for x in file]
		liste = f
except FileNotFoundError:
	liste = []
def sauvegarder():
	with open("text.txt", "w") as file:
		for note in liste:
			file.write(note + "\n")
def afficher_tache():
	if liste == []:
		print("Aucune tâche")
	else:
		for i , tache in enumerate(liste,start = 1):
			print(i , tache)
def afficher_menu():
	print(" ----- Menu ----- ")
	print("1_ ajouter tâche")
	print("2_ valider tâche")
	print("3_ supprimer tâche")
	print("0_ arrêter le programme")
afficher_tache()
afficher_menu()		
while True:
	choix = input("Choisissez une action (0 - 3) : ")
	if choix == "0":
		break
	if choix == "1":
		ajout = input(" Saisissez une tâche : ")
		liste.append(ajout)
		sauvegarder()
		afficher_tache()
		afficher_menu()
	if choix == "2":
		choix_2 = int(input("Sélectionnez la tâche accompli (numero de la tâche) : "))
		liste[choix_2  - 1] =  liste[choix_2  -  1] + " [FAIT]"
		afficher_tache()
		sauvegarder()
		afficher_menu()
	if choix == "3":
		choix_3 = int(input("Sélectionnez la tâche a retirer (numero de la tâche) :  "))
		liste.pop(choix_3 - 1)
		sauvegarder()
		afficher_tache()
		afficher_menu()