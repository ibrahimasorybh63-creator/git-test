from random import *
from player import *
#classe Barbare : dégats élevés, inversement proportionnel aux pv mais défense faible.
class Barbare(Player):
    def __init__(self,pseudo, hp, mana, armure):
        super().__init__(pseudo, hp, mana, armure)
        # état de rage
        self.rage = False
        # compteur , a chaque 10 pv perdu ajoute +1 aux dgt
        self.sup = (150-self.hp)//10
        #lorsque cet état est actif, réduit les dgt subits
        self.choc = False
        #countdown des différentes action
        self.brutal_countdown = 0
        self.choc_countdown = 0
        self.carnage_countdown = 0
        self.rage_countdown = 0
        self.soin_countdown = 0
    def coup_brutal(self, cible):
        dgt = randint(12, 16) + self.sup
        if self.rage == True:
            dgt += int((dgt * 50) / 100)
            self.rage = False
        if dgt >= 15:
            print("Coup critique !💥")
        print(f"{self.pseudo} attaque {cible.pseudo} ! coup brutal.")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        return dgt,self.rage
    def choc_tellurique(self,cible):
        self.mana -= 10
        dgt = randint(8,12)
        if self.rage == True:
            dgt += int((dgt * 50) / 100)
            self.rage = False
        if dgt >= 12:
            print("Coup critique !💥")
        print(f"{self.pseudo} attaque {cible.pseudo} ! Choc tellurique.")
        print(f"Dégats infligés : {dgt}")
        self.choc = True
        cible.subir_degats(self, dgt)
        self.choc_countdown += 3
        return dgt,self.rage,self.choc,self.choc_countdown

    def mode_rage(self):
        self.mana -= 5
        print(f"{self.pseudo} active le mode rage !")
        self.rage = True
        self.rage_countdown += 4
        return self.rage,self.mana,self.rage_countdown
    def carnage(self, cible):
        self.mana -= 40
        dgt = randint(32,42) + self.sup
        if self.rage == True:
            dgt += int((dgt * 50) / 100)
            self.rage = False
        if dgt >= 40:
            print("Coup critique ! ☠")
        print(f"{self.pseudo} attaque {cible.pseudo} ! Attaque ultime, carnage !")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        self.carnage_countdown += 4
        return dgt,self.rage,self.mana,self.carnage_countdown
    def soin(self):
        self.mana -= 30
        soin = int((25 * 150)/ 100)
        self.hp += soin
        print(f"{self.pseudo} utilise soin ! Pv récupéré : {soin}")
        self.soin_countdown += 3
        return self.hp,self.mana,self.soin_countdown
    def subir_degats(self,attaquant,dgt):
        if dgt <= 0:
            super().subir_degats(attaquant,dgt)
            return None
        # compétence passive peau endurcie réduit les dgt
        dgt -= randint(1, 2)
        #plus la réduction de choc si elle est active
        if self.choc == True:
            dgt -= int((dgt*25)/100)
            self.choc = False
        super().subir_degats(attaquant, dgt)
        self.sup = (100 - self.hp) // 10
        return self.sup,self.choc
    #
    def regen_barbare(self):
        self.mana += int((40 * 8)/100)
        print("début du tour : +8% de mana")
        return self.mana
    def reset_barbare(self):
        print("---- Temps de recharge des compétences----")
        if self.choc_countdown > 0:
            self.choc_countdown -= 1
        if self.choc_countdown == 0:
            print("\nChoc Tellurique : disponible")
        else:
            print(f"\nChoc Tellurique : en recharge, {self.choc_countdown} tours restants")
        if self.carnage_countdown > 0:
            self.carnage_countdown -= 1
        if self.carnage_countdown == 0:
            print("Carnage : disponible")
        else:
            print(f"Carnage : en recharge, {self.carnage_countdown} tours restants")
        if self.rage_countdown > 0:
            self.rage_countdown -= 1
        if self.rage_countdown == 0:
            print("Rage : disponible")
        else:
            print(f"Rage : en recharge, {self.rage_countdown} tours restants")
        if self.soin_countdown > 0:
            self.soin_countdown -= 1
        if self.soin_countdown == 0:
            print("Soin : disponible")
        else:
            print(f"Soin : en recharge, {self.soin_countdown} tours restants")
        return self.choc_countdown,self.carnage_countdown,self.rage_countdown,self.soin_countdown

def menu_barbare():
    print("\n--- Menu d'action du Barbare ---")
    print("1_ Coup brutal : inflige de gros dégâts.cout : 0 de mana")
    print("2_ Choc Tellurique : inflige des dgt et affaiblit l'ennemi pendant un tour.Cout : 10 de mana; tdr : 3 tours")
    print("3_ Carnage : inflige des dégâts extrêmement élevés.Cout : 40 de mana; tdr : 4 tours")
    print("4_ Rage : +50% dégâts au prochain tour.Cout : 5 de mana; tdr : 4 tours")
    print("5_ Soin : récupère une partie de ses PV.Cout : 30 de mana; tdr : 3 tours")
    print("--- Capacité passive ---")
    print("Peau endurcie : réduit les dégâts reçus de 1 à 2 points.")
    print("Esprit combatif : à chaque 10 pv perdu, obtient +1 de dgt infligés")