"""
Antoine Patino Conde
405
combat des monstres
"""
import random

print(
    "Vous vous trouvez dans un dongeon plein de monstres! pour survivre , vous devait battre au moins 3 monstres et un boss pour gagner !")


counter = 0
chef = 0
points_de_vie = 20
victoires_consecutifs = 0
force_adversaire = 0


def regles():
    """

    fonction qui affiche les regles du jeu
    """
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.")
    print("Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n")
    print(" Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. ")
    print("Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
    print("La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n")
    print("L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")


def combat():
    """
    La fonction qui define le deroulement du combat
    """
    global chef, counter, points_de_vie, victoires_consecutifs,force_adversaire
    choice = 0
    dice = random.randint(1, 5)
    print(f"Vous attaquez le monstre à {force_adversaire} points de vie avec une force de...")
    print(f"{dice} !!!")
    if dice > force_adversaire:
        print("Reussite!")
        counter = counter + 1
        chef = chef + 1
        victoires_consecutifs = victoires_consecutifs + 1
        points_de_vie = points_de_vie + force_adversaire
        print(f"Vous avez maintenant {points_de_vie} points de vie ")
        print(f"Vous avez {victoires_consecutifs} victoires consecutives")

    else:
        print("Defaite..")
        points_de_vie = points_de_vie - force_adversaire
        print(f"Vous avez maintenant {points_de_vie} points de vie ")
        victoires_cons = 0


def jeu():
    """

    fonction qui define le jeu et le deroulement du programme dependant des choix faits
    """
    global chef, points_de_vie, counter, victoires_consecutifs,force_adversaire

    choice = 0
    while points_de_vie > 0:

        if chef == 3:
            force_chef = random.randint(3, 5)
            print(
                f"Vous confrontez un chef des monstres  ! sa force est de {force_chef} HP    Il vous reste {points_de_vie} points de vie .")
            choice = int(input("Que voulez vous faire ? \n"
                                     "5- Combattre le chef des monstres"))
            if choice == 5:
                dice = random.randint(1, 5)
                print(
                    f"Vous attaquez le chef des monstres qui a une force de {force_chef} point de vie avec une force de...")
                print(f"{dice} !!!")
                if dice > force_chef:
                    print("Reussite!")
                    counter = counter+ 1
                    victoires_consecutifs = victoires_consecutifs + 1
                    boss = 0
                    points_de_vie = points_de_vie + force_chef
                    print(f"Vous avez maintenant {points_de_vie} points de vie ")
                    print(f"Vous avez {victoires_consecutifs} victoires consecutives")
                else:
                    print("Le BOSS vous abat..")
                    points_de_vie = points_de_vie - force_chef
                    print(f"Vous avez maintenant {points_de_vie} HP")
        else:
            force_adversaire = random.randint(1, 5)
            print(f"Vous tombez face a face avec un monstre! sa force est de {force_adversaire} points de vie . ")
            print(f"Il vous reste {points_de_vie} points de vie.")
            print("Que voulez - vous faire ?")
            print("1 - Combattre l'adversaire")
            print("2 - Contourner l'adversaire et aller a une autre porte (-1 HP)")
            print("3 - Afficher les regles du jeu")
            print("4 - Quitter la partie")
            choice = int(input(" "))

        if choice == 1:
            combat()
        elif choice == 2:
            points_de_vie = points_de_vie - 1
        elif choice == 3:
            regles()
        elif choice == 4:
            print("Au revoir")
            exit()


    print("VOUS ETES MORT")
    print(f"Vous avez battu {counter} adversaires")
    exit()


jeu()
