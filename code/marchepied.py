from fonctions_annexes import *
from collections import deque
from graphes import *
# from degenere import *


# Sert à trouver le sommet de commande le plus connecté
# C'est la colonne de la matrice de transport avec le plus de valeurs non nulles
def get_sommet_plus_connecte(proposition_transport) :
    i = 0
    j = 0

    nb_valeurs_non_nulles = [0] * len(proposition_transport[0])

    # Compte le nombre de connexions pour chaque colonne
    for j in range (len(proposition_transport[0]) - 1) : 
        for i in range (len(proposition_transport) - 1) : 
            if(proposition_transport[i][j] != 0) :
                nb_valeurs_non_nulles[j] += 1
        
    # Trouve la colonne avec le maximum de connexions
    max_connexions = 0
    sommet_connecte = 0
    for i in range (0, len(nb_valeurs_non_nulles)) :
        if(nb_valeurs_non_nulles[i] > max_connexions) :
            max_connexions = nb_valeurs_non_nulles[i]
            sommet_connecte = i

    print(f"Le sommet le plus connecté est C{sommet_connecte}")
    return sommet_connecte


# Calcul des potentiels
def calcul_potentiels(couts, proposition_transport):
    # Initialisation des potentiels pour les boucles
    n = len(couts)
    m = len(couts[0])

    # u pour les sommets S, v pour les sommets C (lignes et colonnes)
    u = [None]*n    
    v = [None]*m

    # On fixe une valeur pour initialiser
    u[0] = 0 

    # Boucle jusqu'à ce qu'il n'y ait plus de changements
    change = True
    while change:
        change = False
        # parcours chaque ligne
        for i in range(n):
            #  Parcours chaque colonne
            for j in range(m):
                # Si une valeur de transport existe (donc pas nulle ou epsilon qu'on veut pas))
                if proposition_transport[i][j] > 1e-7:
                    #  si v[j] est pas connu mais u[i] oui
                    if u[i] is not None and v[j] is None:
                        # Calcul de v[j]
                        v[j] = couts[i][j] - u[i]
                        change = True
                    # Sinon, si v[j] est connu mais pas u[i]
                    elif u[i] is None and v[j] is not None:
                        u[i] = couts[i][j] - v[j]
                        change = True

    # Création d'une table avec que des None qu'on rempli avec les potentiels
    couts_pot = [[None]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if u[i] is not None and v[j] is not None:
                couts_pot[i][j] = u[i] + v[j]

    return couts_pot




# Indique si une proposition de transport est optimale
# True si les coûts marginaux sont > 0
# False sinon
def est_optimale(couts_marginaux) :
    i = 0
    j = 0
    for i in range (len(couts_marginaux)) :
        for j in range (len(couts_marginaux[0])) :
            if (couts_marginaux[i][j] is not None and couts_marginaux[i][j] < 0) :
                return False
    return True



# Permet de calculer le coût total de transport d'une proposition de transport
def calcul_cout_transport(couts, proposition_transport) :
    i = 0
    j = 0
    cout_transport = 0

    for i in range (len(couts)) :
        for j in range (len(couts[0])) :
            cout_transport += couts[i][j]*proposition_transport[i][j]

    return cout_transport


# Vérifie si une arête existe entre deux sommets (donc si pas 0 et pas epsilon)
def chemin_existe(proposition_transport, i, j):
    return proposition_transport[i][j] > 1e-6


# Calcul des coûts marginaux 
def calcul_couts_marginaux(couts, couts_potentiels):
    n = len(couts)
    m = len(couts[0])

    # On crée une matrice des coûts marginaux avec que des 0 qu'on remplit
    marg = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if couts_potentiels[i][j] is not None:
                marg[i][j] = couts[i][j] - couts_potentiels[i][j]
            else:
                marg[i][j] = 0
    return marg


# Vérifie si la proposition contient un cycle
def est_cyclique(proposition_transport):
    
    n = len(proposition_transport)-1     
    m = len(proposition_transport[0])-1  

    nb_sommets = n + m
    adj = [[] for _ in range(nb_sommets)]

    
    for i in range(n):
        for j in range(m):
            if proposition_transport[i][j] > 0:
                s = i         
                c = n + j    
                adj[s].append(c)
                adj[c].append(s)

    # BFS pour détecter un cycle 
    visited = [False] * nb_sommets
    parent  = [-1] * nb_sommets

    # Parcours de tout les sommets
    for start in range(nb_sommets):
        if not adj[start]:  # sommet isolé
            continue
        if visited[start]:
            continue

        queue = deque([start])
        visited[start] = True

        while queue:
            u = queue.popleft()

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)

                elif parent[u] != v:
                    # Cycle détecté
                    cycle = reconstruire_cycle(parent, u, v, n)
                    # renvoie le cycle et true si il y en a un
                    return True, cycle

    print("Aucun cycle détecté.")
    return False, None




# Reconstruit le cycle complet entre deux sommets u et v
def reconstruire_cycle(parent, u, v, n):

    chemin_u, chemin_v = [], []
    
    # Remonte jusqu'à la racine depuis u
    cur = u
    while cur != -1:
        chemin_u.append(cur)
        cur = parent[cur]

    # Remonte depuis v jusqu'à la racine
    cur = v
    while cur != -1:
        chemin_v.append(cur)
        cur = parent[cur]

    # Trouver le premier en commun
    set_u = set(chemin_u)
    for noeud in chemin_v:
        if noeud in set_u:
            lca = noeud
            break

    # Construire le cycle
    cycle_u = []
    cur = u
    while cur != lca:
        cycle_u.append(cur)
        cur = parent[cur]
    cycle_u.append(lca)

    cycle_v = []
    cur = v
    while cur != lca:
        cycle_v.append(cur)
        cur = parent[cur]

    cycle_v.reverse()

    cycle = cycle_u + cycle_v

    #   Convertir les indices en noms S_i et C_j
    cycle_nomme = []
    for s in cycle:
        if s < n:
            cycle_nomme.append(f"S{s}")
        else:
            cycle_nomme.append(f"C{s-n}")

    return cycle_nomme

# Vérifie si la proposition est connexe
def est_connexe(proposition_transport):
    n = len(proposition_transport)      # lignes -> sommets S
    m = len(proposition_transport[0])   # colonnes -> sommets C

    # ----- Construction du graphe biparti -----
    nb_sommets = n + m
    adj = [[] for _ in range(nb_sommets)]

    # Création des arêtes
    for i in range(n):
        for j in range(m):
            if proposition_transport[i][j] != 0:
                s = i          # sommet S_i
                c = n + j      # sommet C_j
                adj[s].append(c)
                adj[c].append(s)

    # BFS pour trouver les composantes connexes
    visited = [False] * nb_sommets
    composantes = []

    for start in range(nb_sommets):
        if visited[start]:
            continue
        if not adj[start]:  # sommet isolé (aucune arête)
            visited[start] = True
            composantes.append([start])   # composante de taille 1
            continue

        # BFS 
        queue = deque([start])
        visited[start] = True
        composante = [start]

        while queue:
            u = queue.popleft()

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    composante.append(v)
                    queue.append(v)

        composantes.append(composante)

    # Filtrer les composantes réellement "actives" (celles qui touchent au transport)
    composantes_significatives = [
        comp for comp in composantes
        if len(comp) > 1 or any(adj[s] for s in comp)
    ]

    if len(composantes_significatives) == 1:
        # print("La proposition est connexe.")
        # print("Sous-graphe connexe :", afficher_composante(composantes_significatives[0], n))
        return True

    else:
        # print("La proposition est NON connexe.")
        print("Sous-graphes connexes :")
        for comp in composantes_significatives:
            print("-", afficher_composante(comp, n))
        return False



# Convertit une composante en noms S_i / C_j
def afficher_composante(composante, n):
    noms = []
    for s in composante:
        if s < n:
            noms.append(f"S{s}")
        else:
            noms.append(f"C{s-n}")
    return noms


# Trouve une arête à ajouter pour améliorer la solution
def arete_a_ajouter(couts_marginaux):
    for i in range(len(couts_marginaux)):
        for j in range(len(couts_marginaux[0])):
            if couts_marginaux[i][j] < 0:
                return (i, j)
    return None



#   
# Steve fait cet algo
# Algorithme du marche-pied par potentiel
#
def marche_pied_potentiel(graphes, couts, proposition_transport) :
    # Vérifier si la proposition est dégénérée
    if est_degeneree(proposition_transport):
        print("\n=== Proposition dégénérée détectée ===")

        # Compléter la base
        proposition_transport = completer_base(proposition_transport)
        print("Proposition après complétion de la base :")
        print()

    # Boucle principale du marche-pied tant que la solution n'est pas optimale avec nombre d'itérations
    iteration = 0
    while True :
        # incrémente le nbr d'itérations        
        iteration += 1
        print(f"\n=== Itération n°{iteration} ===")
        # print("Matrice des coûts :")
        # afficher_matrice(couts, len(couts), len(couts[0]))

        # Affichage de la proposition de transport
        print("\nProposition de transport actuelle :")
        afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))
        print()

        # Calcul du coût total de transport en arrondissant pour pas prendre les epsilon en compte
        cout_transport = round(calcul_cout_transport(couts, proposition_transport))
        print(f"Coût total de transport : {cout_transport}\n")
        
        # Vérification de si il y a un cycle 
        est_cycle, cycle = est_cyclique(proposition_transport)
        # si ya un cycle, on sort de la boucle
        if est_cycle:
            print("La proposition est cyclique.")
            break # -> ici pas bon, ya un problème mais pas réussi à résoudre donc on sort pour éviter de planter normalement faudrait, code doublon avec la suite...
            
        # si pas de cycle, on vérifie si la proposition est connexe et si elle ne l'est pas, on sort de la boucle
        if(not est_connexe(proposition_transport)) :
            print("La proposition n'est pas connexe.")
            break 
        
        print("La proposition est connexe.")

        # Calcul des potentiels
        couts_potentiels = calcul_potentiels(couts, proposition_transport)
        
        # affichage des potentiels
        print("\n=== Coûts potentiels : === ")
        afficher_matrice(couts_potentiels, len(couts_potentiels), len(couts_potentiels[0]))
        print()

        # Calcul des coûts marginaux
        couts_marginaux = calcul_couts_marginaux(couts, couts_potentiels)
        # affichage des coûts marginaux
        print("Coûts marginaux :")
        afficher_matrice(couts_marginaux, len(couts_marginaux), len(couts_marginaux[0]))
        print()

        # Si la solution n'est pas optimale, ajouter une arête et corriger avec cycle
        if not est_optimale(couts_marginaux):
            print("La proposition n'est pas optimale")

            # Trouver l'arête à ajouter
            arete = arete_a_ajouter(couts_marginaux)
            # si y en a pas, on sort de la boucle
            if arete is None:
                break
            # affiche l'arrête qu'on a ajouté
            print(f"Arête améliorante ajoutée : {arete}")

            # Ajout de l'arête avec une valeur epsilon
            i, j = arete
            proposition_transport[i][j] = 1e-5

            # Recherche du cycle créé avec l'arrete
            est_cycle, cycle = est_cyclique(proposition_transport)
            if est_cycle:
                print("Cycle trouvé :", cycle)
                # Maximisation sur le cycle
                proposition_transport = maximiser_sur_cycle(proposition_transport, cycle, arete)

            else:
                print("Erreur : aucun cycle trouvé")

            continue  # nouvelle itération du marche-pied   

            
        else :
            break # Sort de la boucle
    
    # Nettoyage final de la solution (enlever les epsilons)
    proposition_transport = nettoyer_solution(proposition_transport)

    # Affichage final de la proposition bien selon nous
    print("La proposition est optimale.")
    afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))
    print()

    # calcul final des couts du transports (on arrondit encore pour pas prendre les epsilons dans les calculs en compte)
    cout_transport = round(calcul_cout_transport(couts, proposition_transport))

    print(f"Coût total de transport : {cout_transport}")


    return proposition_transport


# Ajuste maximiser la solution (fait avec IA car notre solution ne marchait pas)
def maximiser_sur_cycle(proposition_transport, cycle, arete_ajoutee):
    aretes = []
    for k in range(len(cycle)):
        a = cycle[k]
        b = cycle[(k+1) % len(cycle)]
        if a.startswith("S") and b.startswith("C"):
            i, j = int(a[1:]), int(b[1:])
        elif a.startswith("C") and b.startswith("S"):
            i, j = int(b[1:]), int(a[1:])
        else:
            continue
        aretes.append((i, j))

    if arete_ajoutee not in aretes:
        return proposition_transport

    idx = aretes.index(arete_ajoutee)

    aretes_plus = []
    aretes_moins = []

    for k, (i, j) in enumerate(aretes):
        if (k - idx) % 2 == 0:
            aretes_plus.append((i, j))
        else:
            aretes_moins.append((i, j))

    # delta = minimum STRICT des arêtes moins
    delta = min(proposition_transport[i][j] for (i, j) in aretes_moins)

    for (i, j) in aretes_plus:
        proposition_transport[i][j] += delta

    for (i, j) in aretes_moins:
        proposition_transport[i][j] -= delta
        if proposition_transport[i][j] < 1e-8:
            proposition_transport[i][j] = 0

    return proposition_transport











# Permet de vérifier si une proposition de transport est dégénérée
def est_degeneree(proposition_transport):
    n = len(proposition_transport)-1
    m = len(proposition_transport[0])-1
    nb = 0
    for i in range(n):
        for j in range(m):
            if proposition_transport[i][j] > 1e-5:
                nb += 1
    return nb < (n + m - 1)


# Permet de compléter une base dégénérée en ajoutant des epsilons
def completer_base(proposition_transport):
    n = len(proposition_transport) - 1
    m = len(proposition_transport[0]) - 1

    nb_requis = n + m - 1
    # Calcul du nombre d'arêtes actuelles
    nb_aretes = 0
    # On regarde les arretes existantes
    for i in range(n):
        for j in range(m):
            if proposition_transport[i][j] > 0:
                nb_aretes += 1

    epsilon = 1e-6
    # Ajout des epsilons jusqu'à atteindre le nombre d'arretes qui va bien  
    for i in range(n):
        for j in range(m):
            if proposition_transport[i][j] == 0 and nb_aretes < nb_requis:
                proposition_transport[i][j] = epsilon
                nb_aretes += 1
                print(f"Ajout de ε en position ({i},{j})")

    return proposition_transport


# permet d'enlever les epsilons de la solution finale et d'avoir un affichage beau
def nettoyer_solution(proposition_transport, epsilon=1e-5):
    n = len(proposition_transport)-1
    m = len(proposition_transport[0])-1

    for i in range(n):
        for j in range(m):
            if abs(proposition_transport[i][j]) < epsilon:
                proposition_transport[i][j] = 0
            else:
                # Arrondi final à l'entier
                proposition_transport[i][j] = int(round(proposition_transport[i][j]))

    return proposition_transport