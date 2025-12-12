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
        
        

        # Choix entre ligne de la ligne si delta plus élevé 
        if max_delta_ligne > max_delta_colonne:

            # toutes les lignes avec le delta maximum 
            lignes_candidates = [i for i, d in delta_lignes.items() if d == max_delta_ligne]

            # Choisi la ligne dont le coût minimal est le plus faible
            ligne_choisie = min(
                lignes_candidates,
                key=lambda i: min(couts[i, list(colonnes_actives)])
            )

            # ensuite choisir la colonne au coût minimal pour cette ligne
            colonne_choisie = min(colonnes_actives, key=lambda c: couts[ligne_choisie, c])

            
        # Si le colonne a un delta plus élevé
        elif max_delta_ligne < max_delta_colonne :

            # Colonnes candidates (celle avec un delta max)
            colonnes_candidates = [j for j, d in delta_colonnes.items() if d == max_delta_colonne]

            # Choisi la colonne dont le coût minimal est le plus faible
            colonne_choisie = min(
                colonnes_candidates,
                key=lambda j: min(couts[list(lignes_actives), j])
            )
            # Ensuite choisir la meilleure ligne pour cette colonne
            ligne_choisie = min(lignes_actives, key=lambda r: couts[r, colonne_choisie])
            
        # Cas ou le delta maximum des lignes et colonne sont égaux
        else:
            # Lignes et colonnes dont le delta est maximum
            lignes_candidates = [i for i, d in delta_lignes.items() if d == max_delta_ligne]
            colonnes_candidates = [j for j, d in delta_colonnes.items() if d == max_delta_colonne]

            # meilleure ligne candidate (celle dont le min sur colonnes_actives est le plus petit)
            meilleure_ligne = min(
                lignes_candidates,
                key=lambda i: np.min(couts[i, list(colonnes_actives)])
            )
            min_meilleure_ligne = float(np.min(couts[meilleure_ligne, list(colonnes_actives)]))

            # meilleure colonne candidate (celle dont le min sur lignes_actives est le plus petit)
            meilleure_colonne = min(
                colonnes_candidates,
                key=lambda j: np.min(couts[list(lignes_actives), j])
            )
            min_meilleure_colonne = float(np.min(couts[list(lignes_actives), meilleure_colonne]))

            # Si la meilleure valeur minimale est une ligne on prend la ligne, sinon la colonne
            if min_meilleure_ligne <= min_meilleure_colonne:
                # on privilégie la ligne en cas d'égalité des minima
                ligne_choisie = meilleure_ligne
                colonne_choisie = min(colonnes_actives, key=lambda c: couts[ligne_choisie, c])
            else:
                colonne_choisie = meilleure_colonne
                ligne_choisie = min(lignes_actives, key=lambda r: couts[r, colonne_choisie])




        
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