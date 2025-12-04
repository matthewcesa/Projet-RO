from ihm import choisir_Nb_Probleme, choisir_Algo, rester_Sur_Meme_Probleme
from algos import appliquer_Algo, appliquer_MPP

while True:
    numProblem = choisir_Nb_Probleme()

    # PARTIE DE MATTHEW :
    #Lecture, création et affichage de la matrice des coûts associée au problème choisi.
    solution_Initiale = charger_Matrice(numProblem) #Solution initiale = matrice de provision et de coûts.
    afficher_Matrices(solution_Initiale)
    
    # Demander à l'utilisateur de choisir l'algorithme pour fixer la proposition initiale et l'exécuter.
    choix_Algo = choisir_Algo()

    # Exécution de l'algorithme choisi pour obtenir une proposition de transport.
    solution_Initiale = appliquer_Algo(choix_Algo, solution_Initiale)
    
    # Afficher les matrices de PROVISION et de COÛTS CALCULÉES.
    afficher_Matrices(solution_Initiale)
    
    solution_courante = solution_Initiale
    est_Optimale = False

    # Dérouler la méthode du marche-pied avec potentiel :
    while not est_Optimale:
        # Exécution d'une itération de la méthode du marche-pied avec potentiel.
        solution_courante, est_Optimale = appliquer_MPP(solution_courante)

    solution_Optimale = solution_courante
    # Afficher la proposition de transport optimale, ainsi que son coût.
    print("\n--- RÉSULTAT FINAL ---")
    print(f"Proposition de transport optimale : {solution_Optimale['proposition']}")
    print(f"Coût total optimal : {solution_Optimale['cout_total']}")
    
    # Proposer à l'utilisateur de changer de problème de transport (Fin tant que)
    if not rester_Sur_Meme_Probleme():
        break