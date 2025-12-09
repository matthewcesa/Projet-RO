import math

def algorithme_nord_ouest(matrice_provisions_et_commandes) : 

# implémentation de l' alogorithme nord ouest avec en parametre deux matrice : provisions et commandes
# on commence au corner en haut a droite pour finir au corner en bas à gauche   
# on souhaite retourner une novelle matrice avec les résultats trouvés de l'algorithme 

    # on sépare les valeurs de provisions et de commande dans des listes
    provisions = [ligne[-1] for ligne in matrice_provisions_et_commandes[:-1]]
                # prend l'élèment de droite dans chaque ligne (donc toute la colonne à gauche)
                # prend tous sauf la dernière ligne

    commandes = matrice_provisions_et_commandes[-1][:-1]
                # prend la dernière ligne de la matrice

    c = len(provisions) # longueur de la liste commandes
    p = len(commandes) # longueur de la liste provisions

    # on rempli la matrice de 0
    matrice_final = [[0 for _ in range(p)] for _ in range(c)]

    i = 0
    j = 0

    # Tant qu'on est pas au corner en bas a gauche du tableau
    while i != c and j != p:

        # on prend le minimum entre la valeur de commande et de provision puis on l'alloue a la case coresspondante
        allocation = min(provisions[i], commandes[j])
        matrice_final[i][j] = allocation

        # maj des quantité restatnes
        provisions[i] -= allocation
        commandes[j] -= allocation

        # on change de case en fonction de l'allocation 
        if provisions[i] == 0 and commandes[j] == 0 : 
            if j+1 < c :  # si on peut encore avancer à droite
                j+=1 # si on peut aller a droite, on décale vers la case de droite
            else : 
                i+=1 # sinon on décale vers la case du bas 
        elif provisions[i] == 0 : 
            i+=1 # on décale vers la case du bas 
        elif commandes[j] == 0 : 
            j+=1 # on décale vers la case de droite
    return matrice_final



matrice = [
    [math.inf, math.inf, math.inf,  450],
    [math.inf, math.inf, math.inf,  250],
    [math.inf, math.inf, math.inf,  250],
    [math.inf, math.inf, math.inf, 450],
    [500,       600,    300,        1400]
]

# Exécution de l'algorithme
resultat = algorithme_nord_ouest(matrice)

# Affichage
print("Matrice des allocations :")
for ligne in resultat:
    print(ligne)




