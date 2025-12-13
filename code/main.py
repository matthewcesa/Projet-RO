import math
from algos import *
import numpy as np

if __name__ == "__main__" :
    while True:

        matrice_couts = [
        [30, 10, 10],   # ligne 0
        [50, 50, 30],   # ligne 1
        [50, 20, 30]    # ligne 2
    ]


        print("\n MATRICE INITIALE COUT")
        for ligne in matrice_couts:
            print(ligne)

        matrice_provisions = [
            [math.inf, math.inf, math.inf, 450], 
            [math.inf, math.inf, math.inf, 600], 
            [math.inf, math.inf, math.inf, 350],   
            [500,      600,       300,    1400]  
        ]

    

        print("\n MATRICE INITIALE PROIVISONS")
        for ligne in matrice_provisions:
            print(ligne)

        resultat = balas_hammer(matrice_provisions, matrice_couts)
        print("\nRÉSULTAT MATRICE PROVISIONS")
        for ligne in resultat:
            print(ligne)
        break
        # numProblem = choisir_Num_Probleme()

        # #Lecture et stockage de la matrice des coûts associée au numéro de problème choisi.
        # graphes.lecture_fichier_txt(f"matrices/matrice_{numProblem}.txt")
        
        # # Affichage de la matrice des coûts & Provisions x commandes.
        # graphes.afficher_matrice_constante(graphes.matrice_cout)
        # graphes.afficher_matrice_constante(graphes.matrice_provisions_x_commandes)
        
        # # Demander à l'utilisateur de choisir l'algorithme pour fixer la proposition initiale et l'exécuter.
        # choix_Algo = choisir_Algo()

        # # Exécution de l'algorithme choisi pour obtenir une proposition de transport.
        # graphes.matrice_cout, graphes.matrice_provisions_x_commandes = appliquer_Algo(choix_Algo, graphes.matrice_cout, graphes.matrice_provisions_x_commandes)
        
        # # Afficher les matrices de PROVISION et de COÛTS CALCULÉES.
        # afficher_Matrices(graphes.matrice_cout, graphes.matrice_provisions_x_commandes)
        
        # solution_courante = graphes.matrice_cout, graphes.matrice_provisions_x_commandes
        # est_Optimale = False

        # # Dérouler la méthode du marche-pied avec potentiel :
        # while not est_Optimale:
        #     # Exécution d'une itération de la méthode du marche-pied avec potentiel.
        #     solution_courante, est_Optimale = appliquer_MPP(solution_courante)

        # solution_Optimale = solution_courante
        # # Afficher la proposition de transport optimale, ainsi que son coût.
        # print("\n--- RÉSULTAT FINAL ---")
        # print(f"Proposition de transport optimale : {solution_Optimale['proposition']}")
        # print(f"Coût total optimal : {solution_Optimale['cout_total']}")
        
        # # Proposer à l'utilisateur de changer de problème de transport (Fin tant que)
        # if not rester_Sur_Meme_Probleme():
        #     break