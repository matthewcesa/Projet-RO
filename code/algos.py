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

# Détermine et applique l'algorithme choisi par l'utilisateur pour obtenir une proposition de transport initiale.
def appliquer_Algo(choix_Algo, solution_Initiale):
    match choix_Algo:
        case "NO":
            solution_Initiale = nord_ouest(solution_Initiale)
        case "BH":
            solution_Initiale = balas_hammer(solution_Initiale)
    return solution_Initiale

# Exécute une seule itération complète de la méthode du marche-pied avec potentiel (MODI).
# Args:
#     solution_courante (dict): Représente l'état actuel de la solution (matrice de provisions, coûts, etc.).
# Returns:
#     tuple: (nouvelle_solution, est_optimale)
#            - nouvelle_solution (dict): La solution après l'itération ou la solution courante si optimale.
#            - est_optimale (bool): True si la solution est optimale, False sinon.
def appliquer_MPP(solution_courante):
    # Affichage de la proposition de transport courante, ainsi que son coût total.
    afficher_Solution(solution_courante)
    
    # Calcule et affichage des coûts totaux.
    couts_total = calculer_Couts_Total(solution_courante)
    afficher_Couts_Total(couts_total)

    # Test pour savoir si la proposition de transport est dégénérée.
    if est_Degeneree(solution_courante):
        # Convertir la solution dégénérée en arbre.
        solution_courante = from_graph_to_tree(solution_courante)
        
    # Calcul et affichage des potentiels
    sommet_potentiel = calculer_Potentiels(solution_courante)
    afficher_Potentiels(sommet_potentiel)
    
    # Affichage des matrices de coûts potentiels et de coûts marginaux
    couts_potentiels = calculer_Couts_Potentiels(solution_courante, sommet_potentiel)
    couts_marginaux = calculer_Couts_Marginaux(solution_courante, sommet_potentiel)
    afficher_Matrices(couts_potentiels, couts_marginaux)
    
    # Vérifie si la solution est optimale.
    if test_Optimale(couts_marginaux):
        return solution_courante, True # L'itération est terminée.
    else:
        # Si elle n'est pas optimale:
        # Trouver la case hors-base avec le coût marginal le plus négatif.
        arete_Ajoutee = trouver_Arete_A_Ajouter(couts_marginaux)
        # Affichage de l'arête à ajouter.
        afficher_arrete_ajoutee(arete_Ajoutee)
        
        # Identifier le cycle formé par l'arête ajoutée et les cases de base.
        cycle = identifier_Cycle(solution_courante, arete_Ajoutee)
        
        # Maximisation du transport sur le cycle formé et nouvelle itération.
        nouvelle_solution = appliquer_Maximisation(solution_courante, cycle)
        
        return nouvelle_solution, False # L'itération n'est pas terminée, continuer la boucle.