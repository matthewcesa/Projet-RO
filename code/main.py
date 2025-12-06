from algos import *


def boucle_principale() :
    # Lire le tableau et stocker en mémoire (à faire par Matthew)
    
    matrice_1 = [ # Matrice de test
        [30,20,100],
        [10,50,100],
        [100,100]
    ]
    

    choix_algo = demander_algo()

    if(choix_algo == 1) :
        # Nord-Ouest
        print("Vous avez choisi Nord-Ouest")
    else : # choix_algo = 2
        print("Vous avez choisi Balas-Hammer")


if __name__ == "__main__" :
    matrice_couts = [
        [30, 20, 20],   # ligne 0
        [10, 50, 20],   # ligne 1
        [50, 40, 30]    # ligne 2
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
