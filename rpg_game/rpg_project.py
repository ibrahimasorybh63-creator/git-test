from random import *


class Player:
    def init(self, pseudo, hp, mana, armure):
        self.pseudo = pseudo
        self.hp = hp
        self.mana = mana
        self.armure = armure


class Assassin(Player):
    def atk_simple(self, cible):
        dgt = randint(2, 3)
        if dgt == 3:
            print("Coup critique !💥")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! attaque basique.")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure

    def competence_spe(self, cible):
        dgt = randint(7, 10)
        if dgt >= 9:
            print("Coup critique !💥")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! compétence spéciale")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure

    def atk_ultime(self, cible):
        dgt = randint(13, 15)
        if dgt == 15:
            print("Coup critique ! ☠")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! Attaque ultime")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure


class Chevalier(Player):
    def atk_simple(self, cible):
        dgt = randint(1, 2)
        if dgt == 2:
            print("Coup critique !💥")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! attaque basique.")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure

    def competence_spe(self, cible):
        dgt = randint(5, 8)
        if dgt >= 7:
            print("Coup critique !💥")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! compétence spéciale")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure

    def atk_ultime(self, cible):
        dgt = randint(10, 13)
        if dgt == 13:
            print("Coup critique ! ☠")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! Attaque ultime")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure

    def restauration(self):
        res = 10
        self.armure += res
        return self.armure


class Barbare(Player):
    def atk_simple(self, cible):
        dgt = randint(4, 5)
        if dgt == 5:
            print("Coup critique !💥")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! attaque basique.")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure

    def competence_spe(self, cible):
        dgt = randint(10, 15)
        if dgt >= 14:
            print("Coup critique !💥")
        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! compétence spéciale")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure

    def atk_ultime(self, cible):
        dgt = 20
        print("Coup critique ! ☠")

        if dgt <= self.armure:
            cible.armure -= dgt
        else:
            cible.hp -= dgt
        print(f"{self.pseudo} attaque {cible.pseudo} ! Attaque ultime")
        print(f"Dégats infligés : {dgt}")
        return cible.hp, cible.armure


class Mage(Player):
