from math import *
import random
from fonctions_annexes import *
from graphes import *


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

    print("Coûts :")
    afficher_matrice(couts, len(couts), len(couts[0]))
    
    print("Problème de transport :")
    afficher_matrice(probleme_transport, len(probleme_transport), len(probleme_transport[0]))

    return couts, probleme_transport

generer_probleme_aleatoire(10)