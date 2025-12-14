import math
class graphes : 

    #constantes de classe
    matrice_provisions_x_commandes = []
    matrice_couts = []
    matrice_couts_potentiel = []
    matrice_couts_marginaux = [] # couts marginaux = couts - couts potentiels
    P = 0 #nombres de lignes -> provisions
    C = 0 #nombres de colonnes -> commandes
    
    
    
    
    #méthode qui lit le fichier txt et mémorise les données pour en faire des matrices
    @classmethod
    @classmethod
    def lecture_fichier_txt(cls, nom_fichier) : 
        # réinitialisation des matrices et variables de classe
        # i.e. si on appelle plusieurs fois cette méthode, on ne garde pas les anciennes valeurs.
        cls.matrice_provisions_x_commandes = []
        cls.matrice_couts = []
        cls.matrice_couts_potentiel = []
        cls.matrice_couts_marginaux = []
        cls.P = 0
        cls.C = 0

        with open (nom_fichier, 'r') as f:
            lignes = [l.strip() for l in f.readlines()] 
        
        premiere_ligne = [int(x) for x in lignes[0].split()]
        cls.P = premiere_ligne[0] # nombre de de lignes => provisions
        cls.C = premiere_ligne[1] # nombre de colonnes => commandes
        
        longueur_ligne = len(lignes) - 1            # utiliser pour la matrice des provisions x commandes
        longueur_colonne = len(lignes[1].split())   # utiliser pour la matrice des provisions x commandes

        
        for ligne in lignes[1:][:-1] : 
            ligne_int = [int (valeur) for valeur in ligne.split()]  # on convertit en entier et on découpe les valeurs
            ligne_sans_derniere_colonne = ligne_int[:-1] # on enleve la derniere colonne
            cls.matrice_couts.append(ligne_sans_derniere_colonne) # on ajoute a la matrice de cout

        # on intialise la matrice provisions x commandes avec que des infinis
        cls.matrice_provisions_x_commandes = [[math.inf for _ in range(longueur_colonne)] for _ in range(longueur_ligne)] 

        # pour chaque ligne sans la première ligne -> 
        for i, ligne in enumerate(lignes[1:]): 
            ligne_int = [int (valeur) for valeur in ligne.split()]  #on transformer en entier et on découpe les valeurs
            
            # si c'est la derniere ligne
            # on l'ajoute en totalité
            # sinon on ajoute juste le dernire terme de la ligne
            if i == longueur_ligne-1:  
                cls.matrice_provisions_x_commandes[i] = ligne_int 
            cls.matrice_provisions_x_commandes[i][-1] = ligne_int[-1]           
            
            
            
            
            
    # méthode affichage pour les contantes tableaux (matrice_cout, matrice_provisions_x_commandes, etc )
    @classmethod
    def print_matrice_constante(cls, matrice) : 
        
        lenP = len(matrice) 
        lenC = len(matrice[0]) 
        
        #constatnte de méthode qui représente la largeur de chaque colonne
        COL_WIDTH = 8 
        
        for i in range(lenP):
            
            ligne_actuelle = ""
            for val in matrice[i]: # affichage des coûts (au centre de chaque colonne)
                ligne_actuelle += str(val).center(COL_WIDTH)
            print(ligne_actuelle)
            
        ligne_actuelle = ""
        dernière_ligne_matrice = matrice[lenP-1] 
        for val in dernière_ligne_matrice[:lenC]:
            ligne_actuelle += str(val).center(COL_WIDTH)  
        
        
    # méthode pour afficher la matrice de transport sous forme de tableau
    @classmethod 
    def afficher_matrice_transport(cls):

        #constatnte de méthode qui représente la largeur de chaque colonne
        COL_WIDTH = 8
        
        # Longueur totale de la ligne de séparation 
        TOTAL_WIDTH = COL_WIDTH * (cls.C + 2)  
        print("-" * TOTAL_WIDTH) 
        
        # entete de colonne 
        ligne_du_haut = "".ljust(COL_WIDTH)   # pour faire en sorte qu'il y ait une "case" vide en haut à gauche 
                                            # la fonction ljust permet d'aligner le texte à gauche dans un espace de largeur         COL_WIDTH
                                      
        # affichage des noms de colonnes : Cj      
        for j in range(cls.C):
            ligne_du_haut += f"C{j+1}".center(COL_WIDTH)
        
        ligne_du_haut += "Provisions".center(COL_WIDTH) # dernire colonne "Provisions"
        
        print(ligne_du_haut)
        print("-" * TOTAL_WIDTH)

        # lignes intérieurs du tableau/lignes des fournisseurs sous forme ( P1, P2, ... Coûts et Provision)
        for i in range(cls.P):
            nom_colonne = f"S{i+1}" 
            donnees_colonne = cls.matrice_provisions_x_commandes[i]
            
            # affichage des noms de colonnes : Pj 
            ligne_actuelle = nom_colonne.ljust(COL_WIDTH+1)
            
            # affichage des couts (au centre de chaque colonne)
            donnes_couts = donnees_colonne[:cls.C]
            for val in donnes_couts:
                ligne_actuelle += str(val).center(COL_WIDTH)
            
            # affichage de la Provision (au centre de la dernière colonne)
            provision = donnees_colonne[cls.C]
            ligne_actuelle += str(provision).center(COL_WIDTH)
            
            print(ligne_actuelle)

        # Ligne de Séparation
        print("-" * TOTAL_WIDTH)
        
        # dernière ligne/ ligne des commandes
        demand_label = "Commandes"
        ligne_donnees_colonne = cls.matrice_provisions_x_commandes[cls.P]
        
        # affichage du label "Commandes" (aligné à gauche)
        derniere_ligne = demand_label.ljust(COL_WIDTH)
        
        # Affichage des valeurs de Commandes (au centre)
        for val in ligne_donnees_colonne[:cls.C]:
            derniere_ligne += str(val).center(COL_WIDTH)
        print(derniere_ligne)
        
        
        print("-" * TOTAL_WIDTH)





# Test de la lecture de fichier et affichage des matrices
# graphes.lecture_fichier_txt("matrices/matrice_12.txt")

# print("Matrice des coûts (sans dernière colonne) :")
# graphes.print_matrice_constante(graphes.matrice_couts)

# print("\nMatrice des provisions x commandes (dernière ligne + dernière colonne) :")
# graphes.print_matrice_constante(graphes.matrice_provisions_x_commandes)
# graphes.afficher_matrice_transport()

    