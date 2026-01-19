#création des différentes classes de joueur à choisir
import random


class Player:
    def __init__(self, pseudo, hp, mana, armure):
        self.pseudo = pseudo
        self.hp = hp
        self.mana = mana
        self.armure = armure
        self.poison = 0
        self.brulure = 0
        self.froid = 0
    def etat(self,compagnon):
        print("----Etat actuel des joueurs----")
        print(f"\n{self.pseudo}   |  {compagnon.pseudo}"
              f"\nPV: {self.hp}   |  PV: {compagnon.hp}"
              f"\nMana : {self.mana}   |  Mana: {compagnon.mana}"
              f"\nArmure : {self.armure}   |  Armure: {compagnon.armure}")
#une fonction qui fait subir les dégats retournés et vérifie si des états sont actifs pour les appliquer
    def subir_degats(self,attaquant,dgt):
        if self.poison > 0:
            print(f"{self.pseudo} souffre du poison ! -4 PV")
            self.hp -= random.randint(4,6)
            self.poison -= 1
        if self.brulure >0:
            print("pv perdu à cause de brulure : 3")
            self.hp -= 3
            self.brulure -= 1
        if dgt > self.armure:
            print(f"L'armure de {self.pseudo} se brise !")
        if self.armure >= dgt:
            self.armure -= dgt
            dgt = 0
        else:
            dgt -= self.armure
            self.armure = 0
            self.hp -= dgt
        return self.hp, self.armure