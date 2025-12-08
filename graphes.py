import math
class graphes : 

    #constantes de classe
    matrice_provisions_x_commandes = []
    matrice_couts = []
    matrice_couts_potentiel = []
    matrice_couts_marginaux = [] # couts marginaux = couts - couts potentiels
    P = 0
    C =0
    
    @classmethod
    def lecture_fichier_txt(cls, nom_fichier) : 
        with open (nom_fichier, 'r') as f:
            lignes = [l.strip() for l in f.readlines()] 
        
        premiere_ligne = [int(x) for x in lignes[0].split()]
        cls.P = premiere_ligne[0] # nombre de de lignes => provisions
        cls.C = premiere_ligne[1] # nombre de colonnes => commandes
        
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
            
            
    # méthode affichage pour les contantes tableaux (matrice_cout, matrice_provisions_x_commandes, etc )
    @classmethod
    def print_matrice_constante(cls, matrice) : 
        
        lenP = len(matrice) 
        lenC = len(matrice[0]) 
        
        COL_WIDTH = 8 #constatnte de méthode qui représente la largeur de chaque colonne
        
        for i in range(lenP):
            
            current_line = ""
            for val in matrice[i]: # affichage des Coûts (au centre de chaque colonne)
                current_line += str(val).center(COL_WIDTH)
            print(current_line)
            
        current_line = ""
        dernière_ligne_matrice = matrice[lenP-1] 
        for val in dernière_ligne_matrice[:lenC]:
            current_line += str(val).center(COL_WIDTH)
            
        
    # méthode pour afficher la matrice de transport sous forme de tableau
    @classmethod 
    def afficher_matrice_transport(cls):

        COL_WIDTH = 8
        
        TOTAL_WIDTH = COL_WIDTH * (cls.C + 2) # Longueur totale de la ligne de séparation
        print("-" * TOTAL_WIDTH) # --- Ligne de Séparation Supérieure ---
        
        # entete de colonne
        header_line = "".ljust(COL_WIDTH)   # pour faire en sorte qu'il y ait une "case" vide en haut à gauche 
                                            # la fonctiosn ljust permet d'aligner le texte à gauche dans un espace de largeur   COL_WIDTH
                                      
         # noms des colonnes Cj      
        for j in range(cls.C):
            header_line += f"C{j+1}".center(COL_WIDTH)
        
        header_line += "Provisions".center(COL_WIDTH) # dernire colonne "Provisions"
        
        print(header_line)
        print("-" * TOTAL_WIDTH)

        # lignes intérieurs du tableau/lignes des fournisseurs sous forme ( P1, P2, ... Coûts et Provision)
        for i in range(cls.P):
            P_label = f"S{i+1}" 
            row_data = cls.matrice_provisions_x_commandes[i]
            
            # affichage du label P1, P2, (aligné à gauche)
            current_line = P_label.ljust(COL_WIDTH+1)
            
            # affichage des Coûts (au centre de chaque colonne)
            cost_data = row_data[:cls.C]
            for val in cost_data:
                current_line += str(val).center(COL_WIDTH)
            
            # affichage de la Provision (au centre de la dernière colonne)
            provision = row_data[cls.C]
            current_line += str(provision).center(COL_WIDTH)
            
            print(current_line)

        # Ligne de Séparation
        print("-" * TOTAL_WIDTH)
        
        # dernière ligne/ ligne des commandes
        demand_label = "Commandes"
        demand_row_data = cls.matrice_provisions_x_commandes[cls.P]
        
        # affichage du label "Commandes" (aligné à gauche)
        demand_line = demand_label.ljust(COL_WIDTH)
        
        # Affichage des valeurs de Commandes (au centre)
        for val in demand_row_data[:cls.C]:
            demand_line += str(val).center(COL_WIDTH)
        print(demand_line)
        
        
        print("-" * TOTAL_WIDTH)


# Test de la lecture de fichier et affichage des matrices
graphes.lecture_fichier_txt("matrices/matrice_12.txt")

print("Matrice des coûts (sans dernière colonne) :")
graphes.print_matrice_constante(graphes.matrice_cout)

print("\nMatrice des provisions x commandes (dernière ligne + dernière colonne) :")
graphes.print_matrice_constante(graphes.matrice_provisions_x_commandes)
graphes.afficher_matrice_transport()

    