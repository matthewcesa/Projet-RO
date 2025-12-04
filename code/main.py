from algos import *
from Probleme import *


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
    p = Probleme(3,3)
    afficher_matrice(p.couts)
    # pb_a_traiter = demander_pb_a_traiter()
    # while(pb_a_traiter != 0) :
        # boucle_principale()

        # pb_a_traiter = demander_pb_a_traiter()