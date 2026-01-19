from random import *
from player import *
# classe Mage : équilibré, mana élevé, soin, vol de mana et armure temporaire.
class Mage(Player):
    def __init__(self,pseudo,hp,mana,armure):
        super().__init__(pseudo, hp, mana, armure)
        self.magic_armor = False
        self.magic_aff = 0
        self.froid = 0
        self.feu_countdown = 0
        self.glace_countdown = 0
        self.tonnerre_countdown = 0
        self.armor_countdown = 0
        self.drain_countdown = 0
        self.soin_countdown = 0
    def atk_basique(self,cible):
        dgt = randint(8,12)
        if dgt >= 11:
            print("coup critique !")
        print(f"{self.pseudo} lance un sort de base .")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        return dgt
    def boule_de_feu(self, cible):
        self.mana -= 15
        dgt = randint(14, 20) + self.magic_aff
        if self.magic_aff <5:
            self.magic_aff += 1
        if dgt >= 19:
            print("Coup critique !💥")
        print(f"{self.pseudo} attaque {cible.pseudo} ! boule de feu lancé !.")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        cible.brulure = 2
        self.feu_countdown += 1
        return dgt,self.magic_aff,cible.brulure,self.mana,self.feu_countdown
    def rayon_de_glace(self, cible):
        self.mana -=20
        dgt = randint(10, 15) + self.magic_aff
        cible.froid = 1
        if self.magic_aff <5:
            self.magic_aff += 1
        if dgt >= 14:
            print("Coup critique !💥")
        print(f"{self.pseudo} attaque {cible.pseudo} ! rayon de glace !")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        self.glace_countdown += 2
        return dgt,self.magic_aff,cible.froid,self.mana,self.glace_countdown
    def tonnerre(self, cible):
        self.mana -= 50
        dgt = 34 + self.magic_aff
        if self.magic_aff <5:
            self.magic_aff += 1
        print("Coup critique ! ☠")
        print(f"{self.pseudo} attaque {cible.pseudo} ! Attaque ultime")
        print(f"Dégats infligés : {dgt}")
        cible.subir_degats(self, dgt)
        self.tonnerre_countdown += 4
        return dgt,self.magic_aff,self.mana,self.tonnerre_countdown
    def bouclier_magique(self):
        self.mana -= 25
        self.magic_armor = True
        self.armure += 6
        print(f"{self.pseudo} active son armure magique temporaire !")
        self.armor_countdown += 3
        return self.mana,self.magic_armor,self.armor_countdown
    def drain(self,cible):
        self.mana -= 20
        vol = 15
        cible.mana -= vol
        self.mana += vol
        self.hp += 2
        print(f"{self.pseudo} utilise drain et vol {vol} de mana à {cible.pseudo} !")
        print(f"mana volé : {vol} , pv récupéré : 2")
        self.drain_countdown += 2
        return self.mana,cible.mana,self.mana
    def soin(self):
        self.mana -= 35
        soin = int((25*85)/100)
        self.hp += soin
        print(f"{self.pseudo} utilise soin ! Pv récupéré : {soin}")
        self.soin_countdown += 3
        return self.hp,self.mana
    def subir_degats(self,attaquant,dgt):
        if dgt <= 0:
            super().subir_degats(attaquant,dgt)
            return None
        if self.magic_armor == True:
            if attaquant.froid > 0:
                dgt -= int((dgt * 20) / 100)
                print(f"{attaquant.pseudo} est sous emprise de froid ! Ses dégats sont réduits de 20%.")
                print("dégats : ", dgt)
                super().subir_degats(attaquant, dgt)
                attaquant.froid -= 1
                self.magic_armor = False
                self.armure = 0
            else:
                super().subir_degats(attaquant, dgt)
                self.magic_armor = False
                self.armure = 0
            return attaquant.froid, self.hp, self.armure,self.magic_armor
        else:
            if attaquant.froid > 0:
                dgt -= int((dgt * 20) / 100)
                print(f"{attaquant.pseudo} est sous emprise de froid ! Ses dégats sont réduits de 20%.")
                print("dégats : ", dgt)
                super().subir_degats(attaquant, dgt)
                attaquant.froid -= 1
            else:
                super().subir_degats(attaquant, dgt)
                return self.froid, self.hp, self.armure,attaquant.froid
    def regen_mage(self):
        self.mana += int((120*25)/100)
        print("début du tour : +25% de mana")
        return self.mana
    def reset_mage(self):
        print("---- Temps de recharge des compétences----")
        if self.feu_countdown > 0:
            self.feu_countdown -= 1
        if self.feu_countdown == 0:
            print("\nBoule de feu : disponible")
        else:
            print(f"\nBoule de feu : en recharge, {self.feu_countdown} tours restants")
        if self.glace_countdown > 0:
            self.glace_countdown  -= 1
        if self.glace_countdown  == 0:
            print("Rayon de glace : disponible")
        else:
            print(f"Rayon de glace : en recharge, {self.glace_countdown} tours restants")
        if self.tonnerre_countdown > 0:
            self.tonnerre_countdown -= 1
        if self.tonnerre_countdown == 0:
            print("Coup de tonnerre : disponible")
        else:
            print(f"Coup de tonnerre : en recharge, {self.tonnerre_countdown} tours restants")
        if self.armor_countdown > 0:
            self.armor_countdown -= 1
        if self.armor_countdown == 0:
            print("Armure magique : disponible")
        else:
            print(f"Armure magique : en recharge, {self.armor_countdown} tours restants")
        if self.drain_countdown > 0:
            self.drain_countdown -= 1
        if self.drain_countdown == 0:
            print("Drain : disponible")
        else:
            print(f"Drain : en recharge, {self.drain_countdown} tours restants")
        if self.soin_countdown > 0:
            self.soin_countdown -= 1
        if self.soin_countdown == 0:
            print("Soin : disponible")
        else:
            print(f"Soin : en recharge, {self.soin_countdown} tours restants")
        return self.feu_countdown, self.glace_countdown, self.tonnerre_countdown, self.soin_countdown,self.drain_countdown,self.armor_countdown

def menu_mage():
    print("\n--- Menu d'action du Mage ---")
    print("1_ Sort offensif de base : lance une petite attaque magique.cout : 0 de mana")
    print("2_ Boule de feu : inflige des dégâts et applique [Brûlure].Cout : 15 de mana; tdr : 1 tour")
    print("3_ Rayon de glace : inflige de petits dégâts et applique [Froid].Cout : 20 de mana; tdr : 2 tours")
    print("4_ Coup de tonnerre : attaque électrique massive avec critique garanti.Cout : 50 de mana; tdr : 4 tours")
    print("5_ Bouclier magique : crée un bouclier qui disparaît après un coup.Cout : 25 de mana; tdr : 3 tours")
    print("6_ Drain : vole du mana à l’adversaire.Cout : 20 de mana; tdr : 2 tours")
    print("7_ Soin : récupère une partie de ses PV.Cout : 35 de mana; tdr : 3 tours")
    print("--- Capacité passive ---")
    print("Affinité magique : +1 puissance par sort lancé (max 5).")
    print("froid : -20% dégâts ennemis.")
    print("brûlure : -3pv par tour (2 tours).")