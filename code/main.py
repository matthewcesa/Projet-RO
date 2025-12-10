from marchepied import *
from nord_ouest import *
from balas_np import *
from graphes import *


if __name__ == "__main__" :
    probleme = demander_pb_a_traiter()
    print(f"Probleme : {probleme}")
    while (probleme != 0) :
        graphes.lecture_fichier_txt(f"../matrices/matrice_{probleme}.txt")


        # Lire le tableau dans le fichier correspondant
        couts = graphes.matrice_couts

        print("Matrice des coûts :")
        graphes.print_matrice_constante(graphes.matrice_couts)
        # afficher_matrice(graphes.matrice_couts, len(graphes.matrice_couts), len(graphes.matrice_couts[0]))

        proposition_transport = graphes.matrice_provisions_x_commandes

        proposition_transport[len(proposition_transport)-1].append(calculer_somme_transport(proposition_transport))

        print("Proposition de transport :")
        afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))

        print()
        choix_algo = demander_algo()
        print()

        if(choix_algo == 1) :
            # Nord-Ouest
            print("Vous avez choisi Nord-Ouest")
            matrice = algorithme_nord_ouest(proposition_transport)
            copier_tableau(matrice,proposition_transport) # La fonction de Matthew était implémentée un peu différemment, donc il a fallu faire un rapide ajustement
            print("Proposition de transport avec Nord-Ouest :")
            afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))

        else : # Si choix_algo = 2
            print("Vous avez choisi Balas-Hammer")
            proposition_transport = balas_hammer(proposition_transport, couts)
            print("Proposition de transport avec Balas-Hammer :")
            afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))


        marche_pied_potentiel(couts, proposition_transport)

        


        probleme = demander_pb_a_traiter()
        print(f"Probleme : {probleme}")
    
    print("Vous ne souhaitez plus tester de nouveaux problèmes.")