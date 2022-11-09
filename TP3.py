"""
Antoine Patino Conde
405
combat des monstres
"""
import random
print("Vous vous trouvez dans un dongeon plein de monstres! pour survivre , vous devait battre au moins 3 monstres et un boss pour gagner !")


"""
    La fonction qui define le deroulement du combat

"""
    counter = 0
    chef = 0
    pointsdevie = 20
    choice = 0
    force_adversaire = 0
    victoires_cons = 0

    def combat():
        dice = random.randint(1, 5)
        print(f"Vous attaquez le monstre à {force_adversaire} points de vie avec une force de...")
        print("...")
        print(f"{dice} !!!")
        if dice > force_adversaire:
            print("Reussite!")
            counter = counter + 1
            chef = chef + 1
            victoires_cons = victoires_cons + 1
            pointsdevie = pointsdevie + force_adversaire
            print(f"Vous avez maintenant {pointsdevie} points de vie ")
            print(f"Vous avez {victoires_cons} victoires consecutives")

        else:
            print("Defaite..")
            pointsdevie = pointsdevie - force_adversaire
            print(f"Vous avez maintenant {pointsdevie} points de vie ")
            victoires_cons = 0
    def jeu():
        while pointsdevie > 0:
            if boss == 3:
                choice = -1
                force_boss = random.randint(3, 5)
                print(f"Vous confrontez un chef des monstres  ! sa force est de {force_boss} HP    Il vous reste {pointdevie} pints de vie .")
                boss_choice = int(input("Que voulez vous faire ? \n"
                                        "5- Combattre le chef des monstres"))
                if boss_choice == 5:
                    dice = random.randint(1, 5)
                    print(f"Vous attaquez le BOSS à {force_boss} HP avec une force de...")
                    print("...")
                    print(f"{dice} !!!")
                    if dice > force_boss:
                        print("Reussite!")
                        counter = counter + 1
                        victoires_cons = victoires_cons + 1
                        boss = 0
                        pointsdevie = pointsdevie + force_boss
                        print(f"Vous avez maintenant {pointsdevie} HP")
                        print(f"Vous avez {victoires_cons} victoires consecutives")



                    else:
                        print("Le BOSS vous abat..")
                        pointsdevie = pointsdevie - force_boss
                        print(f"Vous avez maintenant {pointsdevie} HP")
            else:
                force_adversaire = random.randint(1, 5)
                print(f"Vous tombez face a face avec un monstre! sa force est de {force_adversaire} HP    Il vous reste {hp} HP")
                print("Que voulez - vous faire ?")
                print("1 - Combattre cet adversaire")
                print("2 - Contourner cet adversaire et aller ouvrir une autre porte (-1 HP)")
                print("3 - Afficher les regles du jeu")
                print("4 - Quitter la partie")
                choice = int(input(" "))

            if choice == 1:
                combat()

            elif choice == 2:
                pointsdevie -= 1
                # hud()
                # return {hp}
            elif choice == 3:
                print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
                      " Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. ")
                print("Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n"
                      "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

            elif choice == 4:
                print("Au revoir...")
                exit()




        if pointsdevie <= 0:
            print("VOUS ETES MORT")
            print(f"Vous avez battu {counter} monstres")
            exit()











jeu()
