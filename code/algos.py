from fonctions_annexes import *


# Fait par Steve
# Sert à trouver le sommet de commande le plus connecté
# => c'est simplement la colonne de la matrice de stocks qui a le moins de 0
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


def calcul_potentiels(couts, proposition_transport) :
    couts_potentiels = [
        [None] * len(couts[0]) 
        for _ in range(len(couts))
    ]
    
    # On s'infiltre dans l'arbre : d'abord, si un chemin existe entre un sommet de stock et un sommet de commande,
    # alors la case correspondante dans la matrice des coûts potentiels = le coût de transport
    for i in range (0, len(couts)) :
        for j in range (0, len(couts[0])) :
            if(chemin_existe(proposition_transport, i,j)) :
                print(f"Il existe un arc entre S{i} et C{j}")
                couts_potentiels[i][j] = couts[i][j]
    return couts_potentiels

# Indique si une proposition de transport est optimale
# True si les coûts marginaux sont > 0
# False sinon
def est_optimale(couts_marginaux) :
    i = 0
    j = 0
    for i in range (len(couts_marginaux)) :
        for j in range (len(couts_marginaux[0])) :
            if (couts_marginaux[i][j] < 0) :
                return False
    return True


# Permet de calculer le coût total de transport d'une proposition de transport
def calcul_cout_transport(couts, proposition_transport) :
    i = 0
    j = 0
    cout_transport = 0

    for i in range (len(couts)) :
        for j in range (len(couts[0])) :
            cout_transport += couts[i][j]*proposition_transport[i][j]

    return cout_transport


#   
# Steve fait cet algo
#
def marche_pied_potentiel(couts, proposition_transport) :
    iteration = 0
    while True :        
        iteration += 1
        print(f"Itération n°{iteration}")


        print("Matrice des coûts :")
        afficher_matrice(couts, len(couts), len(couts[0]))

        
        print("Proposition de transport :")
        afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))

        E_S = [None] * len(couts[0])
        E_C = [None] * len(couts)
        
        
        couts_potentiels = calcul_potentiels(couts, proposition_transport)


        sommet_plus_connecte = get_sommet_plus_connecte(proposition_transport)
        E_C[sommet_plus_connecte] = 0
        i = 0
        

        print("Coûts potentiels :")
        afficher_matrice(couts_potentiels, len(couts_potentiels), len(couts_potentiels[0]))

        # Ce qu'il faut faire maintenant :
        # On part d'un sommet S avec potentiel (i.e ceux reliés au sommet très connecté), et on remplit les sommets C
        # Après cela, on traite les sommets S qui n'ont pas encore de potentiel
        

        couts_marginaux = calcul_couts_marginaux(couts, couts_potentiels)
        print("Coûts marginaux :")
        afficher_matrice(couts_marginaux, len(couts_marginaux), len(couts_marginaux[0]))

        # Modifier ici, pour sortir de la boucle while si on a une proposition optimale
        if(not est_optimale(couts_marginaux)) :
            return 0 # Modifier
        else :
            break


    print("La proposition est optimale.")
    afficher_matrice(couts)

    cout_transport = calcul_cout_transport(couts, proposition_transport)
    print(f"Le coût de transport est de {cout_transport}")


# Indique si un chemin existe entre 2 sommets
# True si un sommet existe
# False sinon
def chemin_existe(proposition_transport, S, C) :
    if(proposition_transport[S][C] == 0) :
        return False

    return True

#
# Fait par Steve
# VÉRIFIER QUE C'EST CORRECT (je suis pas sûr que ce soit bon)
#
def calcul_couts_marginaux(couts, couts_potentiels) :
    i = 0
    j = 0

    couts_marginaux = []

    for i in range (len(couts)) :
        ligne = []
        for j in range (len(couts_potentiels[0])) :
            ligne.append(couts[i][j] - couts_potentiels[i][j])
        couts_marginaux.append(ligne)
    
    return couts_marginaux