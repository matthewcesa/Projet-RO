# Fonction basique pour afficher les matrices
def afficher_matrice(matrice, nb_lignes, nb_colonnes) :
    i = 0
    j = 0

    for i in range(nb_lignes) :
        for j in range (nb_colonnes) :
            # Pour afficher chaque case avec un écart de 8 caractères à droite, sans retour à la ligne
            if matrice[i][j] is None:
                print(f"{'None':<10}", end="")
            else:
                print(f"{matrice[i][j]:<10}", end="")
        print()


def copier_tableau(matrice, proposition_transport) :
    i = 0
    j = 0

    for i in range (len(matrice)) :
        for j in range(len(matrice[0])) :
            proposition_transport[i][j] = matrice [i][j]

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

# Pour calculer la somme des marchandises transportables dans le circuit
def calculer_somme_transport(proposition_transport) :
    i = len(proposition_transport)-1
    j = 0

    somme = 0

    for j in range (len(proposition_transport[0])-1) :
        somme += proposition_transport[i][j]
        # print(f"Somme += {proposition_transport[i][j]}")
    
    # print(f"Somme coûts : {somme}")
    return somme