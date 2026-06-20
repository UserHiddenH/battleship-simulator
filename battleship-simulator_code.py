TAILLE = 10
NOMBRE_BATEAUX = 5
LETTRE_COORDONNE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
TAILLES_BATEAUX = [5, 4, 3, 3, 2]  # Tailles des bateaux disponibles
import random


def creer_grille(): 
    '''
    none --> grille 
    Permet de creer une grille de taille 10x10
    '''
    grille = []
    for i in range(TAILLE):
        grille.append([''] * TAILLE)
    return grille



def afficher_grille(grille):
    '''
    grille --> none
    Permet d'afficher avec tous les éléments qui la compose 
    la grille de taille 10x10
    '''
    print("  ", end="")
    for i in range(TAILLE):
        print(i + 1, end=' ')
    print()
    for i in range(TAILLE):
        print(LETTRE_COORDONNE[i], end=' ')
        for j in range(TAILLE):
            print(grille[i][j] or '.', end=' ')  # Affiche '.' pour les cases vides
        print()



def convertir_coordonne():
    '''
    none --> tuple (int, int)
    Permet de convertir les coordonnées transmises par l'utilisateur 
    '''
    chiffres_valides = '0,1,2,3,4,5,6,7,8,9'

    while True:
        coord = input('Entrer une coordonnée (ex: A1, C5, E2...) : ').upper()  # Permet de ne pas avoir d'erreur de syntaxe

        # Vérifie que la coordonnée a 2 caractères, que le premier est une lettre valide et le deuxième un chiffre valide
        if len(coord) == 2 and coord[0] in LETTRE_COORDONNE and coord[1] in chiffres_valides:
            ligne = LETTRE_COORDONNE.index(coord[0])
            colonne = int(coord[1]) - 1
            return ligne, colonne
        if len(coord) == 3 and coord[0] in LETTRE_COORDONNE and coord[1] in chiffres_valides and coord[2] in chiffres_valides:
            ligne = LETTRE_COORDONNE.index(coord[0])
            colonne = int(10) - 1
            return ligne, colonne   
        print('Coordonnée invalide veuillez réessayer...')



def est_adjacent(ligne, col, grille):
    '''
    int x int x grille --> bool
    Permet de vérifier si un bateau est adjacent à un autre
    '''
    directions = [(-1, -1), (-1, 0), (-1, 1),  # Diagonales et haut
                  (0, -1),          (0, 1),   # Gauche et droite
                  (1, -1),  (1, 0), (1, 1)]   # Diagonales et bas
    for dx, dy in directions:
        nx, ny = ligne + dx, col + dy
        if 0 <= nx < TAILLE and 0 <= ny < TAILLE and grille[nx][ny] == 'B': # Vérification que les coordonnées sont dans la grille
            return True  # Un bateau adjacent a été trouvé 
    return False # Aucun bateau adjacent trouvé 



def peut_placer_bateau(ligne, col, direction, taille, grille):
    '''
    int x int x str x int x grille --> bool
    Vérifie si un bateau peut être placé dans une direction donnée
    '''
    dx, dy = 0, 0
    if direction == 'Z':  # Haut
        dx, dy = -1, 0
    elif direction == 'S':  # Bas
        dx, dy = 1, 0
    elif direction == 'Q':  # Gauche
        dx, dy = 0, -1
    elif direction == 'D':  # Droite
        dx, dy = 0, 1

    for i in range(taille):
        x = ligne + i * dx  # Calcul de la position de la case en x
        y = col + i * dy    # Calcul de la position de la case en y
        if not (0 <= x < TAILLE and 0 <= y < TAILLE) or grille[x][y] == 'B' or est_adjacent(x, y, grille): # Vérification que la case est dans les limites de la grille, qu'il n'y a pas déjà un bateau sur cette case et qu'il n'y a pas de bateau adjacent
            return False
    return True



def direction_bateau(ligne, col, direction, taille, grille):
    '''
    int x int x str x int x grille --> none
    Place un bateau sur la grille
    '''
    dx, dy = 0, 0
    if direction == 'Z':  # Haut
        dx, dy = -1, 0
    elif direction == 'S':  # Bas
        dx, dy = 1, 0
    elif direction == 'Q':  # Gauche
        dx, dy = 0, -1
    elif direction == 'D':  # Droite
        dx, dy = 0, 1

    for i in range(taille):
        x = ligne + i * dx # Calcul de la position de la case en x
        y = col + i * dy   # Calcul de la position de la case en y
        grille[x][y] = 'B' 




def afficher_bateaux_restants(bateaux_restants): #Fonction qui se met à jour au fur et à mesure que les joueurs placent leur bateaux
    '''
    list --> none
    Affiche les bateaux restants à placer
    '''
    print("\nBateaux restants à placer :")
    for taille in bateaux_restants:
        print(f"- Bateau de taille {taille}")




def placer_bateaux(grille): #Fonction placer_bateaux pour les joueurs humains
    '''
    grille --> none
    Permet de remplir notre grille avec des bateaux de tailles différentes
    tout en respectant les conditions
    '''
    print("\n--- Placement des bateaux ---")
    bateaux_restants = TAILLES_BATEAUX[:] 
    afficher_grille(grille)
    afficher_bateaux_restants(bateaux_restants) 

    while bateaux_restants: # Tant que tous les bateaux ne sont pas placés 
        taille = bateaux_restants[0]
        print(f"\nPlacez un bateau de taille {taille}")
        ligne, colonne = convertir_coordonne()

        print('Quel sera la direction de votre bateau (Z: haut, Q: gauche, S: bas, D: droite) ? ', end='')
        direction = input().upper()
        while direction not in ['Z', 'Q', 'S', 'D']:
            print('Veuillez saisir une direction valide.', end='')
            direction = input().upper()

        if peut_placer_bateau(ligne, colonne, direction, taille, grille):
            direction_bateau(ligne, colonne, direction, taille, grille)
            bateaux_restants.pop(0)
            afficher_grille(grille)
            afficher_bateaux_restants(bateaux_restants)
        else:
            print("Impossible de placer le bateau ici. Veuillez réessayer.")




def placer_bateaux_IA(grille_IA):
    '''
    grille --> none
    Permet à l'IA de placer des bateaux de tailles différentes
    tout en respectant les règles du jeu
    '''
    bateaux_restants = TAILLES_BATEAUX[:]  
    while bateaux_restants:
        taille = bateaux_restants[0]
        direction = random.choice(['Z', 'Q', 'S', 'D'])
        ligne, colonne = random.randint(0, TAILLE - 1), random.randint(0, TAILLE - 1)

        if peut_placer_bateau(ligne, colonne, direction, taille, grille_IA):
            direction_bateau(ligne, colonne, direction, taille, grille_IA)
            bateaux_restants.pop(0)
            


def verifier_bateau_coule(grille, ligne, colonne):
    '''
    grille x int x int --> bool
    Vérifie si le bateau auquel appartient la case (ligne, colonne) est entièrement coulé
    '''
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, Bas, Gauche, Droite
    
    # Vérifie dans toutes les directions pour trouver toutes les cases du bateau
    for dx, dy in directions:
        x, y = ligne, colonne
        while 0 <= x < TAILLE and 0 <= y < TAILLE and grille[x][y] != '':
            if grille[x][y] == 'B':  # Si on trouve une case intacte du bateau il n'est pas coulé
                return False
            x += dx
            y += dy

    return True  # Si toutes les cases du bateau sont touchées il est coulé



def tirer(grille_joueur, grille_affichage): #Fonction tirer pour les joueurs humains
    '''
    grille x grille --> none
    Permet de remplir la grille du joueur 
    en fonction de ses tirs
    '''
    print("\n--- Phase de tir ---")
    afficher_grille(grille_affichage)

    tir_valide = False
    while not tir_valide:
        print('Où voulez-vous tirer ? ')
        ligne, colonne = convertir_coordonne()

        if grille_affichage[ligne][colonne] != 'X' and grille_affichage[ligne][colonne] != 'O':
            if grille_joueur[ligne][colonne] == 'B':
                grille_joueur[ligne][colonne] = 'X'
                grille_affichage[ligne][colonne] = 'X'
                if verifier_bateau_coule(grille_joueur, ligne, colonne):
                    print("Touché-coulé !")
                else:
                    print("Touché !")
            else:
                print("Manqué !")
                grille_affichage[ligne][colonne] = 'O'
            tir_valide = True
        else:
            print('Vous avez déjà tiré ici ! Veuillez essayer une autre case...')




def tirer_IA(grille_joueur, grille_affichage):
    '''
    grille x grille --> none
    Permet de remplir la grille de l'IA 
    en fonction de ses tirs
    '''    
    
    print("\n-- Phase de tir IA --")

    # Vérifier s'il y a un bateau touché non coulé pour cibler autour
    for ligne in range(TAILLE):
        for colonne in range(TAILLE):
            if grille_affichage[ligne][colonne] == 'X':
                # Directions possibles (haut, bas, gauche, droite)
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    x, y = ligne + dx, colonne + dy
                    # Vérifie si la case est valide et non explorée
                    if (0 <= x < TAILLE and 0 <= y < TAILLE and grille_affichage[x][y] not in ['X', 'O']):
                        # Tir sur cette case
                        if grille_joueur[x][y] == 'B':
                            grille_joueur[x][y] = 'X'
                            grille_affichage[x][y] = 'X'
                            if verifier_bateau_coule(grille_joueur, x, y):
                                print("Touché-coulé !")
                                # Marquer les cases autour comme inutiles 
                                for dx2, dy2 in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                                    nx, ny = x + dx2, y + dy2
                                    if 0 <= nx < TAILLE and 0 <= ny < TAILLE and grille_affichage[nx][ny] not in ['X', 'O']:
                                        grille_affichage[nx][ny] = 'O'
                            else:
                                print("Touché !")
                        else:
                            print("Manqué !")
                            grille_affichage[x][y] = 'O'
                        return  # Sort une fois le tir effectuer
                    
    # Si aucun bateau touché à proximité, tir aléatoire
    tir_valide = False
    while not tir_valide:
        ligne, colonne = random.randint(0, TAILLE - 1), random.randint(0, TAILLE - 1)
        if grille_affichage[ligne][colonne] not in ['X', 'O']:
            if grille_joueur[ligne][colonne] == 'B':
                grille_joueur[ligne][colonne] = 'X'
                grille_affichage[ligne][colonne] = 'X'
                if verifier_bateau_coule(grille_joueur, ligne, colonne):
                    print("Touché-coulé !")
                    # Marquer les cases autour comme inutiles
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                        nx, ny = ligne + dx, colonne + dy
                        if 0 <= nx < TAILLE and 0 <= ny < TAILLE and grille_affichage[nx][ny] not in ['X', 'O']:
                            grille_affichage[nx][ny] = 'O'
                else:
                    print("Touché !")
            else:
                print("Manqué !")
                grille_affichage[ligne][colonne] = 'O'
            tir_valide = True



def partie():
    '''
    none --> none
    Fonction principale qui lance la partie
    '''
    print("Choisissez votre mode de jeu, tapez 1 pour jouer humain contre humain, tapez 2 pour jouer contre l'IA, tapez 3 pour le mode IA contre IA et obtenir les statistiques de victoire et défaites sur 100 parties : ", end='')  # Choix du mode
    choix_mode = int(input())
    while choix_mode != 1 and choix_mode != 2 and choix_mode != 3:
        print('Erreur de saisie, veuillez choisir un mode existant. Tapez 1, 2 où 3 : ', end='')
        choix_mode = int(input())
    else:


        if choix_mode == 1:
            # MODE HUMAIN VS HUMAIN
            print("===  Bataille Navale  ===")

            # Création des grilles des joueurs
            grille_joueur_1 = creer_grille()
            grille_joueur_2 = creer_grille()
            grille_affichage_1 = creer_grille()
            grille_affichage_2 = creer_grille()

            # Placement des bateaux
            print("\n Joueur 1, placez vos bateaux :")
            placer_bateaux(grille_joueur_1)

            print("\n Joueur 2, placez vos bateaux :")
            placer_bateaux(grille_joueur_2)

            # Tour par tour
            joueur_1_gagne = False
            joueur_2_gagne = False

            while not joueur_1_gagne and not joueur_2_gagne:
                print("\n--- Tour du Joueur 1 ---")
                tirer(grille_joueur_2, grille_affichage_1)

                # Vérifier si le Joueur 1 a gagné
                joueur_1_gagne = True
                for ligne in grille_joueur_2:
                    if 'B' in ligne:
                        joueur_1_gagne = False
                        break

                if joueur_1_gagne:
                    print("Joueur 1 a gagné ! ")
                    break

                print("\n--- Tour du Joueur 2 ---")
                tirer(grille_joueur_1, grille_affichage_2)

                # Vérifier si le Joueur 2 a gagné
                joueur_2_gagne = True
                for ligne in grille_joueur_1:
                    if 'B' in ligne:
                        joueur_2_gagne = False
                        break

                if joueur_2_gagne:
                    print("Joueur 2 a gagné ! ")




        elif choix_mode == 2:
            # MODE HUMAIN VS IA
            print("===  Bataille Navale  ===")

            # Création des grilles des joueurs
            grille_joueur_humain = creer_grille()
            grille_joueur_IA = creer_grille()
            grille_affichage_humain = creer_grille()
            grille_affichage_IA = creer_grille()

            # Placement des bateaux
            print("\n Joueur 1, placez vos bateaux :")
            placer_bateaux(grille_joueur_humain)

            print("\nL'IA place ses bateaux...")
            placer_bateaux_IA(grille_joueur_IA)

            # Tour par tour
            joueur_humain_gagne = False
            joueur_IA_gagne = False

            while not joueur_humain_gagne and not joueur_IA_gagne:
                print("\n--- Tour de l'Humain ---")
                tirer(grille_joueur_IA, grille_affichage_humain)

                # Vérifier si le Joueur 1 a gagné
                joueur_humain_gagne = True
                for ligne in grille_joueur_IA:
                    if 'B' in ligne:
                        joueur_humain_gagne = False
                        break

                if joueur_humain_gagne:
                    print("Bravo vous avez battu l'IA ! ")
                    break

                print("\n--- Tour de l'IA ---")
                tirer_IA(grille_joueur_humain, grille_affichage_IA)

                # Vérifier si l'IA a gagné
                joueur_IA_gagne = True
                for ligne in grille_joueur_humain:
                    if 'B' in ligne:
                        joueur_IA_gagne = False
                        break

                if joueur_IA_gagne:
                    print("Dommage vous avez perdu contre l'IA ! ")
                    
                    
        elif choix_mode == 3:
            import sys
            import os
            # MODE IA VS IA
            compteur = 0
            # On initialise des variables pour calculer le nombre de victoire des deux IA 
            nbr_victoire_IA_1 = 0 
            nbr_victoire_IA_2 = 0 
                
            while compteur < 100:  # Pour obtenir des statistiques sur 100 parties    
                    sys.stdout = open(os.devnull, 'w')  # Pour ne pas afficher les messages durant la partie
                    
                    # Création des grilles des joueurs
                    grille_joueur_IA_1 = creer_grille()
                    grille_joueur_IA_2 = creer_grille()
                    grille_affichage_IA_1 = creer_grille()
                    grille_affichage_IA_2 = creer_grille()

                    # Placement des bateaux
                    placer_bateaux_IA(grille_joueur_IA_1)
                    placer_bateaux_IA(grille_joueur_IA_2)

                    # Tour par tour
                    joueur_IA_1_gagne = False
                    joueur_IA_2_gagne = False

                    while not joueur_IA_1_gagne and not joueur_IA_2_gagne:
                            # Tour de l'IA 1
                            tirer_IA(grille_joueur_IA_2, grille_affichage_IA_1)
                                
                            # Vérifier si L'IA_1 a gagné
                            joueur_IA_1_gagne = True
                            for ligne in grille_joueur_IA_2:
                                    if 'B' in ligne:
                                            joueur_IA_1_gagne = False
                                            break

                            if joueur_IA_1_gagne:
                                    nbr_victoire_IA_1 += 1 
                                    break

                            # Tour de l'IA 2
                            tirer_IA(grille_joueur_IA_1, grille_affichage_IA_2)

                            # Vérifier si l'IA_2 a gagné
                            joueur_IA_2_gagne = True
                            for ligne in grille_joueur_IA_1:
                                    if 'B' in ligne:
                                            joueur_IA_2_gagne = False
                                            break
                            if joueur_IA_2_gagne:
                                    nbr_victoire_IA_2 += 1
                        
                    compteur += 1
                    sys.stdout.close()  # Fermer le redirection d'output
                    sys.stdout = sys.__stdout__  # Pour réactiver l'affichage 
                
            if compteur > 0:  # Pour éviter la division par zéro 
                    taux_IA1 = (nbr_victoire_IA_1 / compteur) * 100
                    taux_IA2 = (nbr_victoire_IA_2 / compteur) * 100
                    print("Le taux de victoire de l'IA_1 est de",round(taux_IA1),'%')  # Résultats arrondi 
                    print("Le taux de victoire de l'IA_2 est de",round(taux_IA2),'%')
                    if taux_IA1 > taux_IA2 :
                        print('Il y a donc plus de chance de gagner en commençant la partie')
                    elif taux_IA2 > taux_IA1 :
                        print('Il y a donc plus de chance de gagner en commençant en deuxième')
                    else :
                        print("Il y a autant de chance de gagner peux importe l'ordre")      

# Lancer la partie
partie()