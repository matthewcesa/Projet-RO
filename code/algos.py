from fonctions_annexes import *



# Constant fait cet algo
def balas_hammer() :
    return 0



# Matthew fait cet algo
def nord_ouest() :
    return 0 # Modifier la valeur de retour par celle à vraiment retourner (s'il faut retourner une valeur)


def get_sommet_plus_connecte(matrice_stocks) :
    i = 0
    j = 0

    nb_valeurs_non_nulles = [0] * len(matrice_stocks[0])


    for j in range (len(matrice_stocks[0])) : # il faut mettre -1 je crois
        for i in range (len(matrice_stocks)) : # pareil
            if(matrice_stocks[i][j] != 0) :
                nb_valeurs_non_nulles[j] += 1
        # print(f"La colonne {j} contient {nb_valeurs_non_nulles[j]} connexions")
    
    max_connexions = 0
    sommet_connecte = 0
    for i in range (0, len(nb_valeurs_non_nulles)) :
        if(nb_valeurs_non_nulles[i] > max_connexions) :
            max_connexions = nb_valeurs_non_nulles[i]
            sommet_connecte = i
            # print(f"Le sommet connecté devient {i}")
    
    print(f"Le sommet le plus connecté est C{sommet_connecte}") # DEBUG
    return sommet_connecte
            

#
# Steve fait cet algo
#
def marche_pied_potentiel() :
    # Affichage de la proposition de transport, ainsi que son coût de transport total
    # Test pour savoir si la proposition de transport est dégénérée
    #if(est_cyclique(matrice_stocks)) :
        # Faire les trucs pour réajuster le graphe
    #    return 0
    #else :
        # Trouver le sommet Cj le plus connecté : la colonne avec le plus
        # grand nombre de valeurs non nulles

    
    # Modifications du graphe de transport pour obtenir un arbre, dans les cas cyclique ou non connexe.
    
    # Calcul et affichage des potentiels
    
    return 0


#
# Fait par Steve
# VÉRIFIER QUE C'EST CORRECT (je suis pas sûr que ce soit bon)
#
def calcul_couts_marginaux(matrice_couts, matrice_couts_potentiels) :
    i = 0
    j = 0

    couts_marginaux = []

    for i in range (len(matrice_couts)) :
        ligne = []
        for j in range (len(matrice_couts_potentiels)) :
            ligne.append(matrice_couts[i][j] - matrice_couts_potentiels[i][j])
        couts_marginaux.append(ligne)
    
    
    return couts_marginaux


matrice = [
    [150,0,20],
    [0,150,20],
    [0,100,200]
]


get_sommet_plus_connecte(matrice)