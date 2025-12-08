from algos import *


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
