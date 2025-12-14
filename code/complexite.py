from math import *
import random
import matplotlib.pyplot as plt
import time

from fonctions_annexes import *
from graphes import *

import nord_ouest
import balas_np
import marchepied



def generer_probleme_aleatoire(n) :
    i = 0
    j = 0
    
    couts = []
    probleme_transport = []

    for i in range (n) :
        ligne_couts = [0] * n
        ligne_probleme_transport = [0] * n
        for j in range (n) :
            ligne_couts[j] = random.randint(1,100)
            ligne_probleme_transport[j] = random.randint(1,100)
        couts.append(ligne_couts)
        probleme_transport.append(ligne_probleme_transport)
    
    somme_ligne_probleme_transport(probleme_transport)
    somme_colonne_probleme_transport(probleme_transport)
    graphes.matrice_couts = couts
    graphes.matrice_provisions_x_commandes = probleme_transport

    # Ajouter la somme des marchandises circulant en fin de ligne et de colonne

    # print("Coûts :")
    # afficher_matrice(couts, len(couts), len(couts[0]))
    
    # print("Problème de transport :")
    # afficher_matrice(probleme_transport, len(probleme_transport), len(probleme_transport[0]))

    return couts, probleme_transport


tailles_n_a_tester = [10, 40, 100, 400, 1000, 4000] # 10000 aussi
tailles_n_a_tester = [1000]


def tests() :
    tailles_testees = []
    numero_probleme = [i for i in range (100)]

    theta_NO = []
    theta_BH = []

    theta_MP_NO = []
    theta_MP_BH = []
    
    for taille_probleme in tailles_n_a_tester :
        theta_NO = []
        theta_BH = []

        theta_MP_NO = []
        theta_MP_BH = []

        print(f"n = {taille_probleme}")
        i = 0
        debut_n = time.process_time()
        for i in range (0, 100) :
            couts_A, probleme_transport_A = generer_probleme_aleatoire(taille_probleme)
            couts_B = [ligne[:] for ligne in couts_A]
            probleme_transport_B = [ligne[:] for ligne in probleme_transport_A]


            debut_A = time.process_time()
            nord_ouest.algorithme_nord_ouest(probleme_transport_A)
            fin_A = time.process_time()
            difference_temps_A = fin_A - debut_A
            print(f"Problème {i} - Temps CPU utilisé pour N-O : {difference_temps_A} secondes")
            theta_NO.append(difference_temps_A)

            debut_A = time.process_time()
            couts_potentiels_A = marchepied.marche_pied_potentiel(couts_A, probleme_transport_A)
            fin_A = time.process_time()
            difference_temps_A = fin_A - debut_A
            print(f"Problème {i} - Temps CPU utilisé pour marche-pied après N-O : {difference_temps_A} secondes")
            theta_MP_NO.append(difference_temps_A)



            debut_B = time.process_time()
            balas_np.balas_hammer(probleme_transport_B,couts_B)
            fin_B = time.process_time()
            difference_temps_B = fin_B - debut_B
            print(f"Problème {i} - Temps CPU utilisé pour Balas-Hammer : {difference_temps_B} secondes")
            theta_BH.append(difference_temps_B)

            debut_B = time.process_time()
            couts_potentiels_B = marchepied.marche_pied_potentiel(couts_B, probleme_transport_B)
            fin_B = time.process_time()
            difference_temps_B = fin_B - debut_B
            print(f"Problème {i} - Temps CPU utilisé pour marche-pied après Balas-Hammer : {difference_temps_B} secondes")
            theta_MP_BH.append(difference_temps_B)

            
            tailles_testees.append(taille_probleme)

        fin_n = time.process_time()
        diff_n = fin_n - debut_n
        print(f"Pour n = {taille_probleme}, temps d'exécution total de {diff_n} secondes.")
        

        plt.scatter(numero_probleme, theta_NO)
        plt.xlabel("Taille n")
        plt.ylabel("Temps (secondes)")
        plt.title("Theta Nord-Ouest")
        plt.grid(True)
        plt.savefig(f"../nuages_points/nuage_points_NO_{taille_probleme}.png", dpi=300, bbox_inches="tight")
        # plt.show()
        plt.figure()

        plt.scatter(numero_probleme, theta_BH)
        plt.xlabel("Taille n")
        plt.ylabel("Temps (secondes)")
        plt.title("Theta Balas-Hammer")
        plt.grid(True)
        plt.savefig(f"../nuages_points/nuage_points_BH_{taille_probleme}.png", dpi=300, bbox_inches="tight")
        # plt.show()
        plt.figure()

        plt.scatter(numero_probleme, theta_MP_NO)
        plt.xlabel("Taille n")
        plt.ylabel("Temps (secondes)")
        plt.title("Theta marchepied après Nord-Ouest")
        plt.grid(True)
        plt.savefig(f"../nuages_points/nuage_points_MP_NO_{taille_probleme}.png", dpi=300, bbox_inches="tight")
        # plt.show()
        plt.figure()

        plt.scatter(numero_probleme, theta_MP_BH)
        plt.xlabel("Taille n")
        plt.ylabel("Temps (secondes)")
        plt.title("Theta marchepied après Balas-Hammer")
        plt.grid(True)
        plt.savefig(f"../nuages_points/nuage_points_MP_BH_{taille_probleme}.png", dpi=300, bbox_inches="tight")
        # plt.show()
        plt.figure()

        print("")


if __name__ == "__main__" :
    # tests_nord_ouest()
    # tests_balas_hammer()
    tests()