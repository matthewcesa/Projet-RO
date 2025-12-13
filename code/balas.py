from fonctions_annexes import *
import numpy as np
import math

def delta_deux_plus_petites(valeurs):
    """Calcule le delta entre les deux plus petites valeurs d'une liste"""
    if len(valeurs) < 2:
        return -math.inf  # Si une seule valeur, on retourne inf car delta pas calculable
    # prend les deux plus petites valeurs, partition avec le 1 permet de trier le tableau et le [:2] de prendre que les 2 première valeurs
    deux_plus_petites = np.partition(valeurs, 1)[:2]  
    return deux_plus_petites[1] - deux_plus_petites[0]


# Constant fait cet algo
def balas_hammer(matrice_provisions, matrice_couts):

    # Convertir en tableau numpy car plus simple à utiliser
    couts = np.array(matrice_couts, dtype=float)
    provisions = np.array(matrice_provisions, dtype=float)

    # permet de donner le nbr de ligne et de colonne dans le tableau
    n_lignes, n_colonnes = couts.shape

    # On garde les valeurs de la dernière colonne et dernière ligne qui sont les totaux 
    total_lignes_restantes = provisions[:n_lignes, -1].copy()
    total_colonne_restantes = provisions[-1, :n_colonnes].copy()

    # Matrice résultat que je retuorne à la fin
    resultat = provisions.copy()  # on ne touche pas aux dernières lignes/colonnes

    # Lignes et colonnes actives (celles qui sont pas remplises) 
    lignes_actives = set(range(n_lignes))
    colonnes_actives = set(range(n_colonnes))

    compteur = 0

    # Boucle tant que toute les lignes et colonnes sont pas remplises
    while lignes_actives and colonnes_actives:

        compteur +=1
        # Calcul des deltas pour chaque ligne et colonne active
        delta_lignes = {i: delta_deux_plus_petites(couts[i, list(colonnes_actives)]) 
                        for i in lignes_actives}
        delta_colonnes = {j: delta_deux_plus_petites(couts[list(lignes_actives), j]) 
                          for j in colonnes_actives}

        # Trouver le delta maximum pour ligne et colonne
        max_delta_ligne = max(delta_lignes.values())
        max_delta_colonne = max(delta_colonnes.values())
        
        print("\nItération :", compteur)     
        print("Max colonnes :", delta_colonnes)
        

        # Choix entre ligne et colonne selon delta maximum
        if max_delta_ligne >= max_delta_colonne:
            # La ligne a le delta le plus élevé
            ligne_choisie = max(delta_lignes.items(), key=lambda x: x[1])[0]
            print("\n C'est quoi çaaaaaaaaaaa : ", max(delta_lignes.items(), key=lambda x: x[1]))
            # On prend la colonne avec le coût minimal (si il y a 2 delta le meme, on prend celle avec le plus petit)
            colonne_choisie = min(colonnes_actives, key=lambda c: couts[ligne_choisie, c])
            print("\n C'est quoi çaaaaaaaaaaaaaa V2: ", min(colonnes_actives, key=lambda c: couts[ligne_choisie, c]))
            
            
        else:
            # La colonne a le delta le plus élevé
            colonne_choisie = max(delta_colonnes.items(), key=lambda x: x[1])[0]
            print("\n C'est quoi ça : ", max(delta_colonnes.items(), key=lambda x: x[1]))

            
            # On prend la ligne avec le coût minimal (si il y a 2 delta le meme, on prend celle avec le plus petit)
            ligne_choisie = min(lignes_actives, key=lambda r: couts[r, colonne_choisie])
            print("\n C'est quoi ça V2: ", min(lignes_actives, key=lambda r: couts[r, colonne_choisie]))

        print("colonnes :", colonne_choisie)
        
        # Calcul de la quantité maximale à mettre dans la case choisie
        quantite = min(total_lignes_restantes[ligne_choisie], total_colonne_restantes[colonne_choisie])
        resultat[ligne_choisie, colonne_choisie] = quantite

        # Mise à jour des totaux de colonne et ligne
        total_lignes_restantes[ligne_choisie] -= quantite
        total_colonne_restantes[colonne_choisie] -= quantite

        # Si lo total est atteind pour la ligne on rempli le reste de zéro
        if total_lignes_restantes[ligne_choisie] == 0:
            for col in colonnes_actives:
                if col != colonne_choisie:
                    resultat[ligne_choisie, col] = 0
            lignes_actives.remove(ligne_choisie)

        # Si le total est atteint pour la colonne on rempli le reste de zéro
        if total_colonne_restantes[colonne_choisie] == 0:
            for lig in lignes_actives:
                if lig != ligne_choisie:
                    resultat[lig, colonne_choisie] = 0
            colonnes_actives.remove(colonne_choisie)

    #Renvoie la matrice finale
    return resultat.astype(int).tolist()