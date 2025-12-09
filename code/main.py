from marchepied import *


if __name__ == "__main__" :
    probleme = demander_pb_a_traiter()
    while (probleme != 0) :
        # Lire le tableau dans le fichier correspondant
        couts = [
            [11,12,10,10],
            [17,16,15,18],
            [19,21,20,22]
        ]
        print("Matrice des coûts :")
        afficher_matrice(couts, len(couts), len(couts[0]))

        proposition_transport = [
            [50,10,0,0,60],
            [0,30,0,0,30],
            [0,35,30,25,90],
            [50,75,30,25]
        ]

        proposition_transport[len(proposition_transport)-1].append(calculer_somme_transport(proposition_transport))

        print("Proposition de transport :")
        afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))

        choix_algo = demander_algo()
        if(choix_algo == 1) :
            # Nord-Ouest
            print("Vous avez choisi Nord-Ouest")
        else : # Si choix_algo = 2
            print("Vous avez choisi Balas-Hammer")

        marche_pied_potentiel(couts, proposition_transport)