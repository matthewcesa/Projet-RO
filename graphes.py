import math
class graphes : 

    matrice_provisions_x_commandes = []
    matrice_couts = []
    matrice_couts_potentiel = []
    matrice_couts_marginaux = [] # couts marginaux = couts - couts potentiels
    
    @classmethod
    def lecture_fichier_txt(cls, nom_fichier) : 
        with open (nom_fichier, 'r') as f:
            lignes = [l.strip() for l in f.readlines()] 
        
        premiere_ligne = [int(x) for x in lignes[0].split()]
        P = premiere_ligne[0] # nombre de de lignes => provisions
        C = premiere_ligne[1] # nombre de colonnes => commandes
        
        longueur_ligne = len(lignes) - 1      # utiliser pour la matrice des provisions x commandes
        longueur_colonne = len(lignes[1].split()) # utiliser pour la matrice des provisions x commandes

        # la matrice des couts 
        cls.matrice_cout = []
        for ligne in lignes[1:][:-1] : 
            ligne_int = [int (valeur) for valeur in ligne.split()]  # on convertit en entier et on découpe les valeurs
            ligne_sans_derniere_colonne = ligne_int[:-1] # on enleve la derniere colonne
            cls.matrice_cout.append(ligne_sans_derniere_colonne) # on ajoute a la matrice de cout

        # la matrice des provisions x commandes
        cls.matrice_provisions_x_commandes = [[math.inf for _ in range(longueur_colonne)] for _ in range(longueur_ligne)] # on intialise la matrice avec que des infinis
    
        for i, ligne in enumerate(lignes[1:]): # pour chauque ligne sans la première ligne
            ligne_int = [int (valeur) for valeur in ligne.split()]  #on transformer en etier et on découpe les valeurs
            if i == longueur_ligne-1:   # si c'est la derniere ligne
                cls.matrice_provisions_x_commandes[i] = ligne_int # on l'ajoute en totalité
            cls.matrice_provisions_x_commandes[i][-1] = ligne_int[-1] # sinon on ajoute juste le dernire terme de la ligne
                
                
    
    @classmethod
    def print_matrice(cls, matrice):
        for ligne in matrice:
            print(" ".join(str(valeur) for valeur in ligne))
    
    # --- TEST ---
graphes.lecture_fichier_txt("matrices/matrice_11.txt")

print("Matrice des coûts (sans dernière colonne) :")
graphes.print_matrice(graphes.matrice_cout)

print("\nMatrice des provisions x commandes (dernière ligne + dernière colonne) :")
graphes.print_matrice(graphes.matrice_provisions_x_commandes)

    