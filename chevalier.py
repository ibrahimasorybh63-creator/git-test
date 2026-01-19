from random import *
from player import *
#classe Chevalier : faible dégats, joue sur la durée, bouclier et contre_attaque.
class Chevalier(Player):
    def __init__(self, pseudo, hp, mana, armure):
        super().__init__(pseudo, hp, mana, armure)
        self.contre_active = False
        self.dgt_reduit = 0
        #countdown des différentes action
        self.provocation_countdown = 0
        self.charge_countdown = 0
        self.res_countdown = 0
        self.soin_countdown = 0
    def escrime_de_camelot(self, cible):
        dgt = randint(9, 13)
        if dgt >= 12:
            print("Coup critique !💥")
        print(f"{self.pseudo} attaque {cible.pseudo} ! attaque basique.")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        return dgt
    def provocation(self):
        self.mana -= 15
        self.contre_active = True
        self.dgt_reduit += 2
        print(f"{self.pseudo} attire l'attention de l'ennemi et adopte une posture défensive ! 🛡"
              f" Il est prêt à contre-attaquer.")
        self.provocation_countdown += 3
        return self.contre_active,self.dgt_reduit,self.mana
    def charge(self, cible):
        self.mana -= 30
        dgt = randint(22, 30)
        if dgt >= 28:
            print("Coup critique ! ☠")
        print(f"{self.pseudo} attaque {cible.pseudo} ! charge de bouclier !")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        self.charge_countdown += 4
        return dgt,self.mana
    def restauration(self):
        self.mana -= 15
        res = 10
        self.armure += res
        self.res_countdown += 2
        return self.armure,self.mana
    def soin(self):
        self.mana -= 25
        soin = int((25*125)/100)
        self.hp += soin
        print(f"{self.pseudo} utilise soin ! Pv récupéré : {soin}")
        self.soin_countdown += 3
        return self.hp,self.mana
    def subir_degats(self,attaquant,dgt):
        if dgt <= 0:
            super().subir_degats(attaquant,dgt)
            return None
        if self.dgt_reduit > 0:
            self.dgt_reduit -= 1
            dgt -= int((dgt*30)/100)
            print(f"{attaquant.pseudo} est sous l'effet de provocation , ses dgt sont reduits !")
        if self.contre_active == True:
            dgt_recu = int(dgt/ 2)
            riposte = int(dgt_recu / 2)
            self.hp -= dgt_recu
            attaquant.hp -= riposte
            print(
            f"{self.pseudo} contre-attaque ! "
            f"Il ne subit que {dgt_recu} dégâts et renvoie {riposte} à {attaquant.pseudo} !")
            self.contre_active = False
        else:
            super().subir_degats(attaquant,dgt)
        return self.hp,self.armure,self.contre_active,self.dgt_reduit
    def regen_chevalier(self):
        self.mana += int((50*10)/100)
        print("début du tour : +10% de mana")
        return self.mana
    def reset_chevalier(self):
        print("---- Temps de recharge des compétences----")
        if self.provocation_countdown > 0:
            self.provocation_countdown -= 1
        if self.provocation_countdown == 0:
            print("\nProvocation : disponible")
        else:
            print(f"\nProvocation : en recharge, {self.provocation_countdown} tours restants")
        if self.charge_countdown > 0:
            self.charge_countdown  -= 1
        if self.charge_countdown  == 0:
            print("Charge : disponible")
        else:
            print(f"Charge : en recharge, {self.charge_countdown} tours restants")
        if self.res_countdown > 0:
            self.res_countdown -= 1
        if self.res_countdown == 0:
            print("Restauration : disponible")
        else:
            print(f"Restauration : en recharge, {self.res_countdown} tours restants")
        if self.soin_countdown > 0:
            self.soin_countdown -= 1
        if self.soin_countdown == 0:
            print("Soin : disponible")
        else:
            print(f"Soin : en recharge, {self.soin_countdown} tours restants")
        return self.provocation_countdown, self.charge_countdown, self.res_countdown, self.soin_countdown

def menu_chevalier():
    print("\n--- Menu d'action du Chevalier ---")
    print("1_ Escrime de Camelot : attaque à faibles dégâts.cout : 0 de mana")
    print("2_ Provocation : réduit les dégâts ennemis de 30% et prépare un contre.Cout : 15 de mana; tdr : 3 tours")
    print("3_ Charge : fonce sur l’ennemi et inflige de lourds dégâts.Cout : 30 de mana; tdr 4 tours")
    print("4_ Restauration : gagne +10 d’armure.Cout : 15 de mana; tdr : 2 tours")
    print("5_ Soin : récupère une partie de ses PV.Cout : 25 de mana; tdr 3 tours")
    print("--- Capacité passive ---")
    print("Contre : si provoqué, riposte automatiquement lorsqu’il est attaqué.")