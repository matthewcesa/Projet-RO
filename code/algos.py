# Fonction basique pour afficher les matrices
def afficher_matrice(matrice, nb_lignes, nb_colonnes) :
    i = 0
    j = 0

    for i in range(nb_lignes-1) :
        for j in range (nb_colonnes-1) :
            print(f"{matrice[i][j]:<8}", end="")
        print()


# Steve fait cet algo
def balas_hammer() :

    return 0



# Matthew fait cet algo
def nord_ouest() :

    return 0 # Modifier la valeur de retour par celle à vraiment retourner (s'il faut retourner une valeur)



if __name__ == "__main__" :
    pb_a_traiter = int(input("Choisissez le numéro du problème à traiter :"))
    
    # Lire le tableau et stocker en mémoire
    
    matrice_1 = [
        [30,20,100],
        [10,50,100],
        [100,100]
    ]
    
