import random
dgt = [1,2]
dgt_special = [3,4]
soin = [1,2]
class Player:
	def __init__(self,pdv):
		#pdv = points_de_vie
		self.pdv = pdv
	def attaquer(self,cible):
		degats = random.choice(dgt)
		print("dégats : ", degats)
		cible.pdv -= degats
		return cible.pdv
	def attaque_speciale(self,cible):
		degats = random.choice(dgt_special)
		print("dégats : " , degats)
		cible.pdv -= degats
		return cible.pdv
	def soin(self):
		soins = random.choice(soin)
		print("pdv récuperées : ", soins)
		self.pdv += soins
		return self.pdv
p1 = Player(20)
p2 = Player(20)
tour = 1
def afficher_etat():
	print(f"player 1 : {p1.pdv} cœurs restants")
	print(f"player 2 : {p2.pdv} cœurs restants")
def menu():
	print("------Action------")
	print("1_ attaque normale (dgts = 1 ou 2)")
def menu_2():
	print("-------Action-------")
	print(" 1_ attaque normale (dgts = 1 ou 2)")
	print(" 2_ attaque speciale (dgts = 3 ou 4)")
	print(" 3_ soins (pv = +1 ou +2)")		

while True:
	if p1.pdv <=0 or p2.pdv <=0 :
		break
	print(f"------Tour {tour}------")
	afficher_etat()
	
	if tour % 2 ==0:
		menu_2()
		choix_p1 = input("Choisis une action (joueur 1) : ")
		if choix_p1 == "1":
			print(" p1 attaque p2 !")
			print( p1.attaquer(p2))
			afficher_etat()
		elif choix_p1 == "2":
			print("p1 lance son attaque speciale !")
			print(p1.attaque_speciale(p2))
			afficher_etat()
		elif choix_p1 == "3":
			print("p1 se soigne !")
			print(p1.soin())
			afficher_etat()
		menu_2()
		choix_p2 = input("Choisis une action (joueur 2 ) : ")
		if choix_p2 == "1":
			print(" p2 attaque p1 !")
			print( p2.attaquer(p1))
			afficher_etat()
		elif choix_p2 == "2":
			print("p2 lance son attaque speciale !")
			print(p2.attaque_speciale(p1))
			afficher_etat()
		elif choix_p2 == "3":
			print("p2 se soigne !")
			print(p2.soin())
			afficher_etat()
	else:
		menu()
		choix_p1 = input("Choisis une action (joueur 1) : ")
		if choix_p1 == "1":
			print(" p1 attaque p2 !")
			print( p1.attaquer(p2))
			afficher_etat()
		menu()
		choix_p2 = input("Choisis une action (joueur 2 ) : ")
		if choix_p2 == "1":
			print(" p2 attaque p1 !")
			print( p2.attaquer(p1))
			afficher_etat()						
		
	tour += 1	