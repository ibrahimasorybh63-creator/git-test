from random import *
from player import *
#classe Assassin : faible dégats, joue sur la durée, poison et camouflage.
class Assassin(Player):
    def __init__(self,pseudo, hp, mana, armure):
        super().__init__(pseudo, hp, mana, armure)
        self.poison = 0     #compteur de tour restant au poison
        self.invisible = False  #Vérifie si l'assassin est en état de camouflage
        #cooldwon des différentes actions
        self.poison_cooldown = 0
        self.double_cooldown = 0
        self.camouflage_cooldown = 0
        self.soin_cooldown = 0
    def lame_sonique(self, cible):
        self.mana -= 0
        dgt = randint(10, 14)
        if self.invisible == True:
            dgt = 14
            self.invisible = False
        if dgt == 14:
            print("Coup critique !💥")
        print(f"{self.pseudo} attaque {cible.pseudo} ! lame sonique!")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self,dgt)
        return dgt,self.invisible
    #attaque à double
    def attaque_double(self, cible):
        self.mana -= 15
        dgt_1= randint(7, 10)
        dgt_2 = randint(3,8)
        if self.invisible == True:
            dgt_1 = 10
            self.invisible = False
        if dgt_1 >= 10:
            print("Coup critique !💥")
        dgt = dgt_1 + dgt_2
        print(f"{self.pseudo} attaque {cible.pseudo} ! compétence spéciale : attaque double ⚔")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        self.double_cooldown += 2
        return dgt,self.invisible,self.mana,self.double_cooldown
    #applique du poison à la cible
    def lame_toxique(self, cible):
        self.mana -= 10
        print(f"{self.pseudo} utilise lame toxique et empoisonne {cible.pseudo} !")
        dgt = randint(10, 13)
        if self.invisible == True :
            dgt = 13
            self.invisible = False
        if dgt == 13:
            print("Coup critique ! ☠")
        print(f"{self.pseudo} attaque {cible.pseudo} ! Attaque ultime")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        cible.poison = 3
        self.poison_cooldown += 4
        return dgt,self.invisible,self.mana,self.poison_cooldown
    #Entre en état de camouflage et devient invisible, le prochain coup suivant le camouflage est garanti de crit.
    #Le camouflage se désactive dès le premier coup après son activation.
    def camouflage(self):
        self.mana -= 20
        self.invisible = True
        print(f"{self.pseudo} entre en mode camouflage !")
        self.camouflage_cooldown += 3
        return self.invisible,self.mana,self.camouflage_cooldown
    def soin(self):
        self.mana -= 25
        soin = int((25*95)/100)
        self.hp += soin
        print(f"{self.pseudo} utilise soin ! Pv récupéré : {soin}")
        self.soin_cooldown += 3
        return self.hp,self.mana,self.soin_cooldown
    def subir_degats(self,attaquant,dgt):
        if dgt <= 0:
            super().subir_degats(attaquant,dgt)
            return None
        if self.invisible == True:
            print("L'assassin est intouchable ! L'attaque à échoué !")
            super().subir_degats(attaquant,0)
        else:
            super().subir_degats(attaquant,dgt)
        return self.hp,self.armure
    def regen_assassin(self):
        self.mana += int((self.mana * 15)/100)
        print("début du tour : +15% de mana")
        return self.mana
    #une fonction qui met à jour le cooldown de chaque action au début du tour
    def reset_assassin(self):
        print("---- Temps de recharge des compétences----")
        if self.double_cooldown > 0:
            self.double_cooldown -= 1
        if self.double_cooldown == 0:
            print("\nAttaque double : disponible")
        else:
            print(f"\nAttaque double : en recharge, {self.double_cooldown} tours restants")
        if self.poison_cooldown > 0:
            self.poison_cooldown -= 1
        if self.poison_cooldown == 0:
            print("Lame toxique : disponible")
        else:
            print(f"Lame toxique : en recharge, {self.poison_cooldown} tours restants")
        if self.camouflage_cooldown > 0:
            self.camouflage_cooldown -= 1
        if self.camouflage_cooldown == 0:
            print("Camouflage : disponible")
        else:
            print(f"Camouflage : en recharge, {self.camouflage_cooldown} tours restants")
        if self.soin_cooldown > 0:
            self.soin_cooldown -= 1
        if self.soin_cooldown == 0:
            print("Soin : disponible")
        else:
            print(f"Soin : en recharge, {self.soin_cooldown} tours restants")
        return self.double_cooldown,self.poison_cooldown,self.camouflage_cooldown,self.soin_cooldown

def menu_assassin():
    print("\n--- Menu d'action de l'Assassin ---")
    print("1_ Lame sonique : inflige des dégâts légers. cout : 0 de mana")
    print("2_ Double frappe : effectue 2 attaques puissantes. cout : 15 de mana; temps de recharge : 2 tours")
    print("3_ Lame toxique : dégâts moyens + applique [Poison] (3 tours). cout : 10 de mana; tdr : 3 tours")
    print("4_ Camouflage : devient intouchable + prochaine attaque = critique.Cout : 20 de mana; tdr : 3 tours")
    print("5_ Soin : récupère une partie de ses PV. cout : 25 de mana; tdr : 3 tours")
    print("--- Capacité passive ---")
    print("Poison : inflige -4 à -6 PV par tour.")
