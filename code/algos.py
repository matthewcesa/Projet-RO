from fonctions_annexes import *



# Constant fait cet algo
def balas_hammer(matrice_provision, matrice_cout) :
    matrice_complete = matrice_provision
    return matrice_complete



# Matthew fait cet algo
def nord_ouest() :
    return 0 # Modifier la valeur de retour par celle à vraiment retourner (s'il faut retourner une valeur)


#
# Steve fait cet algo
#
def marche_pied_potentiel() :
    # Affichage de la proposition de transport, ainsi que son coût de transport total
    # Test pour savoir si la proposition de transport est dégénérée
    
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