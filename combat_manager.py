from assassin import *
from barbare import *
from chevalier import *
from mage import *
from random import *
from player import *


def menu_de_classe():
    print("\n---Classe de combattant disponible---")
    print("1_classe Assassin : faible dégats, joue sur la durée, poison, double frappe et camouflage.")
    print("2_classe Barbare : dégats élevés, défense faible, rage et défense naturelle.")
    print("3_classe Chevalier : faible dégats, joue sur la durée, bouclier, soin et contre attaque.")
    print("4_classe Mage : équilibré, mana élevé, soin, vol de mana, dégats élémentaires et armure temporaire.")


pseudo_p1 = input("\nplayer1 entrez votre pseudo : ")
menu_de_classe()
try:
    choix_p1 = int(input("player1 , choisissez votre classe (1-2-3-4) : "))
except ValueError:
    choix_p1 = int(input("Erreur, veuillez entrez le numéro de la classe (1-2-3-4) : "))

if choix_p1 == 1:
    player1 = Assassin(pseudo_p1, 95, 70, 0)
elif choix_p1 == 2:
    player1 = Barbare(pseudo_p1, 150, 40, 0)
elif choix_p1 == 3:
    player1 = Chevalier(pseudo_p1, 125, 50, 10)
elif choix_p1 == 4:
    player1 = Mage(pseudo_p1, 85, 120, 0)
else:
    print("Erreur")

pseudo_p2 = input("\nplayer2 entrez votre pseudo : ")
menu_de_classe()
try:
    choix_p2 = int(input("player2 , choisissez votre classe (1-2-3-4) : "))
except ValueError:
    choix_p2 = int(input("Erreur, veuillez entrez le numéro de la classe (1-2-3-4) : "))

if choix_p2 == 1:
    player2 = Assassin(pseudo_p2, 95, 70, 0)
elif choix_p2 == 2:
    player2 = Barbare(pseudo_p2, 150, 40, 0)
elif choix_p2 == 3:
    player2 = Chevalier(pseudo_p2, 125, 50, 10)
elif choix_p2 == 4:
    player2 = Mage(pseudo_p2, 85, 120, 0)
else:
    print("Erreur")


class CombatManager:
    def __init__(self, player1, player2):
        # initialisation du combat
        self.liste_joueur = [player1, player2]
        self.joueur_actif = choice(self.liste_joueur)
        self.compteur = 1
        self.action_valide = False
        if self.joueur_actif == player1:
            self.joueur_passif = player2
        else:
            self.joueur_passif = player1
        self.combat_termine = False
        if player1.hp <= 0 or player2.hp <= 0:
            self.combat_termine = True

    def tour_de_jeu(self):
        while True:
            if self.combat_termine == True:
                break
            print(f"\n---Tour {self.compteur}---")
            # applique les effets négatifs au joueur au début du tour, s'il y en a.
            self.joueur_actif.subir_degats(self.joueur_passif, 0)
            # tour du joueur 1
            if self.joueur_actif == player1:
                player1.etat(player2)
                print(f"\ntour de {player1.pseudo}")
                # si p1 est un assassin
                if choix_p1 == 1:
                    menu_assassin()
                    player1.regen_assassin()
                    player1.reset_assassin()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:  # lame sonique
                        player1.lame_sonique(player2)
                    elif action == 2:  # double attaque
                        if player1.mana < 15 or player1.double_cooldown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.attaque_double(player2)
                    elif action == 3:  # lame toxique
                        if player1.mana < 10 or player1.poison_cooldown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.lame_toxique(player2)
                            self.action_valide = True
                    elif action == 4:  # camouflage
                        if player1.mana < 20 or player1.camouflage_cooldown > 0:
                            print("impossible d'utiliser cette compétence pour le moment !")
                            continue
                        else:
                            player1.camouflage()
                    elif action == 5:  # soin
                        if player1.mana < 25 or player1.soin_cooldown > 0:
                            print("impossible d'utiliser cette compétence pour le moment !")
                            continue
                        else:
                            player1.soin()
                elif choix_p1 == 2:
                    # si p1 est un barbare
                    menu_barbare()
                    player1.regen_barbare()
                    player1.reset_barbare()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:
                        player1.coup_brutal(player2)
                    elif action == 2:
                        if player1.mana < 10 or player1.choc_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.choc_tellurique(player2)
                    elif action == 3:
                        if player1.mana < 40 or player1.carnage_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.carnage(player2)
                    elif action == 4:
                        if player1.mana < 5 or player1.rage_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player1.mode_rage()
                    elif action == 5:
                        if player1.mana < 30 or player1.soin_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player1.soin()
                elif choix_p1 == 3:
                    # si p1 est un chevalier
                    menu_chevalier()
                    player1.regen_chevalier()
                    player1.reset_chevalier()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:
                        player1.escrime_de_camelot(player2)
                    elif action == 2:
                        if player1.mana < 15 or player1.provocation_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player1.provocation()
                    elif action == 3:
                        if player1.mana < 30 or player1.charge_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.charge(player2)
                    elif action == 4:
                        if player1.mana < 15 or player1.res_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player1.restauration()
                    elif action == 5:
                        if player1.mana < 25 or player1.soin_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player1.soin()
                elif choix_p1 == 4:
                    # si p1 est un mage
                    menu_mage()
                    player1.regen_mage()
                    player1.reset_mage()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:
                        player1.atk_basique(player2)
                    elif action == 2:
                        if player1.mana < 15 or player1.feu_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.boule_de_feu(player2)
                    elif action == 3:
                        if player1.mana < 20 or player1.glace_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.rayon_de_glace(player2)
                    elif action == 4:
                        if player1.mana < 50 or player1.tonnerre_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.tonnerre(player2)
                    elif action == 5:
                        if player1.mana < 25 or player1.armor_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player1.bouclier_magique()
                    elif action == 6:
                        if player1.mana < 20 or player1.drain_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player1.drain(player2)
                    elif action == 7:
                        if player1.mana < 35 or player1.soin_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player1.soin()
                self.joueur_actif = player2
            else:
                player2.etat(player1)
                print(f"\ntour de {player2.pseudo} !")
                if choix_p2 == 1:
                    menu_assassin()
                    player2.regen_assassin()
                    player2.reset_assassin()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:  # lame sonique
                        player2.lame_sonique(player1)
                    elif action == 2:  # double attaque
                        if player2.mana < 15 or player2.double_cooldown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.attaque_double(player1)
                    elif action == 3:  # lame toxique
                        if player2.mana < 10 or player2.poison_cooldown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.lame_toxique(player1)
                    elif action == 4:  # camouflage
                        if player2.mana < 20 or player2.camouflage_cooldown > 0:
                            print("Impossible d'utiliser cette compétence pour le moment !")
                            continue
                        else:
                            player2.camouflage()
                    elif action == 5:
                        if player2.mana < 25 or player2.soin_cooldown > 0:
                            print("Impossible d'utiliser cette compétence pour le moment !")
                            continue
                        else:
                            player2.soin()
                elif choix_p2 == 2:
                    # si p2 est un barbare
                    menu_barbare()
                    player2.regen_barbare()
                    player2.reset_barbare()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:
                        player2.coup_brutal(player1)
                    elif action == 2:
                        if player2.mana < 10 or player2.choc_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.choc_tellurique(player1)
                    elif action == 3:
                        if player2.mana < 40 or player2.carnage_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.carnage(player1)
                    elif action == 4:
                        if player2.mana < 5 or player2.rage_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player2.mode_rage()
                    elif action == 5:
                        if player2.mana < 30 or player2.soin_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player2.soin()
                elif choix_p2 == 3:
                    # si p2 est un chevalier
                    menu_chevalier()
                    player2.regen_chevalier()
                    player2.reset_chevalier()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:
                        player2.escrime_de_camelot(player1)
                    elif action == 2:
                        if player2.mana < 15 or player2.provocation_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player2.provocation()
                    elif action == 3:
                        if player2.mana < 30 or player2.charge_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.charge(player1)
                    elif action == 4:
                        if player2.mana < 15 or player2.res_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player2.restauration()
                    elif action == 5:
                        if player2.mana < 25 or player2.soin_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player2.soin()
                elif choix_p2 == 4:
                    # si p2 est un mage
                    menu_mage()
                    player2.regen_mage()
                    player2.reset_mage()
                    action = int(input("\nchoisissez une action : "))
                    if action == 1:
                        player2.atk_basique(player1)
                    elif action == 2:
                        if player2.mana < 15 or player2.feu_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.boule_de_feu(player1)
                    elif action == 3:
                        if player2.mana < 20 or player2.glace_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.rayon_de_glace(player1)
                    elif action == 4:
                        if player2.mana < 50 or player2.tonnerre_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.tonnerre(player2)
                    elif action == 5:
                        if player2.mana < 25 or player2.armor_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player2.bouclier_magique()
                    elif action == 6:
                        if player2.mana < 20 or player2.drain_countdown > 0:
                            print("Impossible de lancer cette attaque pour le moment !")
                            continue
                        else:
                            player2.drain(player1)
                    elif action == 7:
                        if player2.mana < 35 or player2.soin_countdown > 0:
                            print("Impossible de lancer cette compétence pour le moment !")
                            continue
                        else:
                            player2.soin()
                self.joueur_actif = player1
            self.compteur += 1


combat = CombatManager(player1, player2)
combat.tour_de_jeu()
