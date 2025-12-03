class lecture_fichiers : 
    
    listes_matrices_stockes = []

    @classmethod
    def lecture_simple_fichier(cls, nom_fichier) : # deux boucles non imbriqués donc compelxité = O(2n)
        with open (nom_fichier, 'r') as f:
            lignes = [l.strip() for l in f.readlines()] 
        
        premiere_ligne = [int(x) for x in lignes[0].split()]
        C = premiere_ligne[0] # nombre de de lignes => provisions
        P = premiere_ligne[1] # nombre de colonnes => commandes

        matrice_entiere = [] # représente la matrice entière sans C et P => que les valeurs
        for ligne in lignes[1:] : # on commence a partir de la ligne 1 et on va jusqu'à la fin 
            ligne_int = [int(valeur) for valeur in ligne.split()] # on découpe les valeurs et on les ajotue
            matrice_entiere.append(ligne_int)
        
        provisions = [] 
        commandes = [] 
        couts = [] # provisions x commandes

        for i in range (P) : # on extraits les couts et les provisions 
            ligne = matrice_entiere[i]

            couts.append(ligne[:C])
            # Le coût est donné par les C premières colonnes

            provisions.append(lignes[C])
            # La provision est la dernière valeur de la ligne (indice C)

        ligne_commandes = matrice_entiere[P]
        commandes.extend(ligne_commandes[:C]) # On prend seulement les C premières valeurs


        
# il faut tester la focntion pour voir si elle marche vraiment 
# il manque la mémorisation des novuelles matrices créé
# il manque l'affichage des matrices aussi 

    
            
