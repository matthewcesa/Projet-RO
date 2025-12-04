# Fonction basique pour afficher les matrices
def afficher_matrice(matrice, nb_lignes, nb_colonnes) :
    i = 0
    j = 0

    for i in range(nb_lignes-1) :
        for j in range (nb_colonnes-1) :
            # Pour afficher chaque case avec un écart de 8 caractères à droite, sans retour à la ligne
            print(f"{matrice[i][j]:<8}", end="")
        print()

# Pour demander quel problème on souhaite traiter
def demander_pb_a_traiter() :
    pb_a_traiter = int(input("Choisissez le numéro du problème à traiter (0 pour sortir): "))
    
    while((pb_a_traiter < 0) or (pb_a_traiter > 13)) :
        print("Erreur : saisissez une valeur entre 1 et 13 inclus (0 pour sortir).")
        pb_a_traiter = int(input("Choisissez le numéro du problème à traiter (0 pour sortir): "))
    
    return pb_a_traiter


def demander_algo() :
    print("Choisissez l'algorithme à utiliser :")
    print("1 : Nord-Ouest")
    print("2 : Balas-Hammer")
    choix_algo = int(input("Votre choix : "))

    while((choix_algo != 1) and (choix_algo != 2)) :
        print("Choisissez l'algorithme à utiliser :")
        print("1 : Nord-Ouest")
        print("2 : Balas-Hammer")
        choix_algo = int(input("Votre choix : "))
    
    return choix_algo