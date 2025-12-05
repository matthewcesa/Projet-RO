class graphes : 

    matrice_stock = []
    matrice_couts = []
    matrice_couts_potentiel = []
    matrice_couts_marginaux = [] # couts marginaux = couts - couts potentiels
    
    
    @classmethod
    def __init__(self, P, C, couts) : 
        self.P = P 
        self.C = C 
        self.couts = couts
        
    @classmethod
    def lecture_fichier_txt(cls, nom_fichier) : 
        with open (nom_fichier, 'r') as f:
            lignes = [l.strip() for l in f.readlines()] 
        
        premiere_ligne = [int(x) for x in lignes[0].split()]
        P = premiere_ligne[0] # nombre de de lignes => provisions
        C = premiere_ligne[1] # nombre de colonnes => commandes
    
        # matrice_entiere = [] # représente la matrice entière sans C et P => que les valeurs
        # for ligne in lignes[1:] : # on commence a partir de la ligne 1 et on va jusqu'à la fin 
        #     ligne_int = [int(valeur) for valeur in ligne.split()] # on découpe les valeurs et on les ajotue
        #     matrice_entiere.append(ligne_int)
        
        # Faire la matrice des couts
        # Faire la matrice commande x provisions