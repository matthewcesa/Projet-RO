from fonctions_annexes import *
import math

def calcul_delta_lignes(matrice_couts, colonnes_actives, num_ligne):

    valeurs = [matrice_couts[num_ligne][j] for j in colonnes_actives]

    if len(valeurs) < 2:
        return -math.inf

    valeurs = sorted(valeurs)
    return valeurs[1] - valeurs[0]


def calcul_delta_colonnes(matrice_couts, lignes_actives, num_colonne):
    valeurs = [matrice_couts[i][num_colonne] for i in lignes_actives]

    if len(valeurs) < 2:
        return -math.inf

    valeurs = sorted(valeurs)
    return valeurs[1] - valeurs[0]

def balas_hammer(matrice_provision, matrice_cout):

    nb_lignes = len(matrice_cout)
    nb_colonnes = len(matrice_cout[0])

    # Sont toutes vides donc actives au début
    lignes_actives = set(range(nb_lignes))
    colonnes_actives = set(range(nb_colonnes))

    compteur = 0

    # Boucle sur ligne et colonne qui ne sont pas remplises
    while lignes_actives and colonnes_actives:

        print("\nACTIVEES à itération : ", compteur)    
        print("\nLignes actives : ", lignes_actives)
        print("Colonnes actives : ", colonnes_actives)

        
        deltas_lignes = {}
        for i in lignes_actives:
            deltas_lignes[i] = calcul_delta_lignes(matrice_cout, colonnes_actives, i)

        deltas_colonnes = {}
        for j in colonnes_actives:
            deltas_colonnes[j] = calcul_delta_colonnes(matrice_cout, lignes_actives, j)

        

        # Trouve meilleure ligne en calculant le delta
        premiere_ligne = next(iter(deltas_lignes))
        max_delta_ligne = deltas_lignes[premiere_ligne]
        meilleure_ligne = [premiere_ligne, max_delta_ligne]
        for ligne, delta in deltas_lignes.items():
            if delta > max_delta_ligne:
                max_delta_ligne = delta
                meilleure_ligne = [ligne, delta]


        # Trouve meilleure colonneen calculant le delta
        premiere_colonne = next(iter(deltas_colonnes))
        max_delta_colonne = deltas_colonnes[premiere_colonne]
        meilleure_colonne = [premiere_colonne, max_delta_colonne]
        for colonne, delta in deltas_colonnes.items():
            if delta > max_delta_colonne:
                max_delta_colonne = delta
                meilleure_colonne = [colonne, delta]



        # Vérifie si le delta le plus faible est ligne ou colonne
        if max_delta_ligne >= max_delta_colonne:
            # on traite la ligne sélectionnee
            i = meilleure_ligne[0]
            
            cout_min = math.inf
            for j in colonnes_actives:
                c = matrice_cout[i][j]
                if c < cout_min:
                    cout_min = c
                    index_col_choisie = j

            offre = matrice_provision[i][-1]
            demande = matrice_provision[-1][index_col_choisie]

            # la quantite max qu'on peut mettre dans la case minimale du delta le plus élevé (ca va pas chiant comme phrase)
            quantite = min(offre, demande)

            # On met la valeur dans la bonne case
            matrice_provision[i][index_col_choisie] = quantite

            # On met les autre cases de la colone à 0 
            for ligne_idx in range(len(matrice_provision) - 1):
                if ligne_idx != i:
                    matrice_provision[ligne_idx][index_col_choisie] = 0

            # La ligne n'est plus prise en compte
            lignes_actives.remove(i)
            
        # Ca me parait être redondant vu qu'on fait la meme chose mais version ligne et colonne... je sais pas si c'est très opti....
        # En tout cas ça fonctionne je pense que je vais regarder pour améliorer car la j'en bouffe de l'énergie... 
        #Ttout mon algo me parait long pour rien. C'est une version 1.0 à voir si j'arrive à l'améliorer ou si vous trouvez des trus mieux
        else:
            j = meilleure_colonne[0]
            # trouver la ligne active de coût minimal dans la colonne j
            cout_min = math.inf
            for k in lignes_actives:
                c = matrice_cout[k][j]
                if c < cout_min:
                    cout_min = c
                    index_ligne_choisie = k

            offre = matrice_provision[index_ligne_choisie][-1]
            demande = matrice_provision[-1][j]

            # Comme pour colonne mais version ligne
            quantite = min(offre, demande)

            # Comme pour la colonne
            matrice_provision[index_ligne_choisie][j] = quantite


            for col_idx in range(len(matrice_provision[0]) -1):
                if col_idx != j:
                    matrice_provision[index_ligne_choisie][col_idx] = 0
                
            colonnes_actives.remove(j)

            
        matrice_cout_active = []
        for i in lignes_actives:
            ligne_active = [matrice_cout[i][j] for j in colonnes_actives]
            matrice_cout_active.append(ligne_active)

        # print("\nMatrice provision à itération :", compteur)
        # for ligne in matrice_provision:
        #     print(ligne)
    # print("\nMatrice coûts")
    # for ligne in matrice_cout_active:
    #     print(ligne)



        compteur += 1

    return matrice_provision








#--------------------------------------------------
def delta_ligne(matrice_couts, i):
    ligne = matrice_couts[i]
    deux_min = sorted(ligne)
    return deux_min[1] - deux_min[0]


def delta_colonne(matrice_couts, j):

    colonne = [ligne[j] for ligne in matrice_couts]
    deux_min = sorted(colonne)
    return deux_min[1] - deux_min[0]