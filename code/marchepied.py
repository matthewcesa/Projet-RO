from fonctions_annexes import *
from collections import deque
from graphes import *
# from degenere import *

# Fait par Steve
# Sert à trouver le sommet de commande le plus connecté
# => c'est simplement la colonne de la matrice de stocks qui a le moins de 0
def get_sommet_plus_connecte(proposition_transport) :
    i = 0
    j = 0

    nb_valeurs_non_nulles = [0] * len(proposition_transport[0])


    for j in range (len(proposition_transport[0]) - 1) : # il faut mettre -1 je crois
        for i in range (len(proposition_transport) - 1) : # pareil
            if(proposition_transport[i][j] != 0) :
                nb_valeurs_non_nulles[j] += 1
        # print(f"La colonne {j} contient {nb_valeurs_non_nulles[j]} connexions")
    
    max_connexions = 0
    sommet_connecte = 0
    for i in range (0, len(nb_valeurs_non_nulles)) :
        if(nb_valeurs_non_nulles[i] > max_connexions) :
            max_connexions = nb_valeurs_non_nulles[i]
            sommet_connecte = i
            # print(f"Le sommet connecté devient {i}")
    
    print(f"Le sommet le plus connecté est C{sommet_connecte}") # DEBUG
    return sommet_connecte


# def arc_existe(arcs,i,j) :
#     for arc in arcs :
#         if (i,j) == arc :
#             return True
#     return False

def calcul_potentiels(couts, proposition_transport) :
    couts_potentiels = [
        [None] * len(couts[0]) 
        for _ in range(len(couts))
    ]

    sommet_plus_connecte = get_sommet_plus_connecte(proposition_transport)
    # print(f"Le sommet le plus connecté est {sommet_plus_connecte}")

    E_S = [None] * len(couts)
    E_C = [None] * len(couts[0])

    E_C[sommet_plus_connecte] = 0

    
    # On s'infiltre dans l'arbre : d'abord, si un chemin existe entre un sommet de stock et un sommet de commande,
    # alors la case correspondante dans la matrice des coûts potentiels = le coût de transport
    for i in range (0, len(couts)) :
        for j in range (0, len(couts[0])) :
            if(chemin_existe(proposition_transport, i,j)) :
                        couts_potentiels[i][j] = couts[i][j]
                        if(j == sommet_plus_connecte) :
                            E_S[i] = couts[i][sommet_plus_connecte]
                            # print(f"E_S[{i}] = {E_S[i]}")
    
    print("Coûts pot SF :")
    afficher_matrice(couts_potentiels, len(couts_potentiels), len(couts_potentiels[0]))
    
    for i in range (0, len(couts)) :
        if(E_S[i] is not None) :
            for j in range (0, len(couts[0])) :
                if(chemin_existe(proposition_transport, i,j)) :
                        if(E_C[j] is None) :
                            E_C[j] = E_S[i] - couts[i][j]

    for j in range (0, len(couts[0])) :
        if(E_C[j] is not None) :
            for i in range (0, len(couts)) :
                if(chemin_existe(proposition_transport, i,j)) :
                        if(E_S[i] is None) :
                            E_S[i] = couts[i][j] + E_C[j]


    for i in range (0, len(couts)) :
        for j in range (0, len(couts[0])) :
            if((E_S[i] is not None) and (E_C[j] is None)) :
                E_C[j] = E_S[i] - couts[i][j]
                # print(f"Calcul : E_C[{j}] = E_S[{i}] - couts[{i}][{j}] = {E_S[i]} - {couts[i][j]} = {E_C[j]}")
            elif((E_S[i] is None) and (E_C[j] is not None)) :
                E_S[i] = couts[i][j] + E_C[j]
                # print(f"Calcul : E_S[{i}] = couts[{i}][{j}] + E_C[{j}] = {couts[i][j] + E_C[j]} = {E_S[i]}")

            couts_potentiels[i][j] = E_S[i] - E_C[j]
            # print(f"couts_potentiels[{i}][{j}] = {E_S[i]} - {E_C[j]} = {couts_potentiels[i][j]}")   
            

    # print(f"E_S : {E_S}")
    # print(f"E_C : {E_C}")

    return couts_potentiels


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

    # print(f"len(couts) : {len(couts)}")
    # print(f"len(couts[0]) : {len(couts[0])}")
    # print(f"len(pt) : {len(proposition_transport)}")
    # print(f"len(pt[0]) : {len(proposition_transport[0])}")

    for i in range (len(couts)) :
        for j in range (len(couts[0])) :
            cout_transport += couts[i][j]*proposition_transport[i][j]

    return cout_transport


# Indique si un chemin existe entre 2 sommets
# True si un sommet existe
# False sinon
def chemin_existe(proposition_transport, S, C) :
    if(proposition_transport[S][C] == 0) :
        return False
    return True

#
# Fait par Steve
# VÉRIFIER QUE C'EST CORRECT (je suis pas sûr que ce soit bon)
#
def calcul_couts_marginaux(couts, couts_potentiels) :
    i = 0
    j = 0

    couts_marginaux = []

    # print("CP :")
    # print(couts_potentiels)

    for i in range (len(couts)) :
        ligne = []
        for j in range (len(couts[0])) :
            if(couts_potentiels[i][j] is not None) :
                ligne.append(couts[i][j] - couts_potentiels[i][j])
            else :
                ligne.append(0)
        couts_marginaux.append(ligne)
    
    return couts_marginaux


def est_cyclique(proposition_transport):
    n = len(proposition_transport)-1     # nombre de lignes S_i
    m = len(proposition_transport[0])-1  # nombre de colonnes C_j

    # ---------- Construction du graphe biparti ----------
    # Sommets = S0..Sn-1   et   C0..Cm-1  (indexés comme C_j -> n+j)
    nb_sommets = n + m
    adj = [[] for _ in range(nb_sommets)]

    for i in range(n):
        for j in range(m):
            if proposition_transport[i][j] > 0:
                s = i          # sommet S_i
                c = n + j      # sommet C_j
                adj[s].append(c)
                adj[c].append(s)

    # ---------- BFS pour détecter un cycle ----------
    visited = [False] * nb_sommets
    parent  = [-1] * nb_sommets

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
                    # --- Cycle détecté ---
                    cycle = reconstruire_cycle(parent, u, v, n)
                    print("Cycle détecté :", cycle)
                    return True

    print("Aucun cycle détecté.")
    return False


# ---------- Reconstruit le cycle complet entre u et v ----------
def reconstruire_cycle(parent, u, v, n):
    # Remonte depuis u jusqu'à la racine
    chemin_u = []
    cur = u
    while cur != -1:
        chemin_u.append(cur)
        cur = parent[cur]

    # Remonte depuis v jusqu'à la racine
    chemin_v = []
    cur = v
    while cur != -1:
        chemin_v.append(cur)
        cur = parent[cur]

    # Trouver le premier ancêtre commun
    set_u = set(chemin_u)
    for noeud in chemin_v:
        if noeud in set_u:
            lca = noeud
            break

    # Construire chemin u → LCA
    cycle_u = []
    cur = u
    while cur != lca:
        cycle_u.append(cur)
        cur = parent[cur]
    cycle_u.append(lca)

    # Construire chemin v → LCA (en sens inverse)
    cycle_v = []
    cur = v
    while cur != lca:
        cycle_v.append(cur)
        cur = parent[cur]

    cycle_v.reverse()

    cycle = cycle_u + cycle_v

    # convertir les index internes en noms S_i / C_j
    cycle_nomme = []
    for s in cycle:
        if s < n:
            cycle_nomme.append(f"S{s}")
        else:
            cycle_nomme.append(f"C{s-n}")

    return cycle_nomme


def est_connexe(proposition_transport):
    n = len(proposition_transport)      # lignes -> sommets S
    m = len(proposition_transport[0])   # colonnes -> sommets C

    # ----- Construction du graphe biparti -----
    nb_sommets = n + m
    adj = [[] for _ in range(nb_sommets)]

    for i in range(n):
        for j in range(m):
            if proposition_transport[i][j] > 0:
                s = i          # sommet S_i
                c = n + j      # sommet C_j
                adj[s].append(c)
                adj[c].append(s)

    # ----- BFS pour trouver toutes les composantes -----
    visited = [False] * nb_sommets
    composantes = []

    for start in range(nb_sommets):
        if visited[start]:
            continue
        if not adj[start]:  # sommet isolé (aucune arête)
            visited[start] = True
            composantes.append([start])   # composante de taille 1
            continue

        # BFS normal
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

    # ----- Analyse du résultat -----

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


# ----- Utilitaire pour afficher les sommets S_i et C_j -----
def afficher_composante(composante, n):
    noms = []
    for s in composante:
        if s < n:
            noms.append(f"S{s}")
        else:
            noms.append(f"C{s-n}")
    return noms


def arete_a_ajouter(couts_potentiels) :
    i = 0
    j = 0

    for i in range (len(couts_potentiels)) :
        for j in range (len(couts_potentiels[0])) :
            if(couts_potentiels[i][j] < 0) :
                return (i,j)
    return None


#   
# Steve fait cet algo
#
def marche_pied_potentiel(graphes, couts, proposition_transport) :
    iteration = 0
    while True :        
        iteration += 1
        print(f"Itération n°{iteration}")


        # print("Matrice des coûts :")
        # afficher_matrice(couts, len(couts), len(couts[0]))

        # Affichage de la proposition de transport
        print("Proposition de transport :")
        afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))
        print()

        cout_transport = calcul_cout_transport(couts, proposition_transport)
        print(f"Coût total de transport : {cout_transport}")
        print()
        
        if(est_cyclique(proposition_transport) == True) :
            print("La proposition est cyclique.")
            break # Retirer
        print("La proposition de transport est acyclique.")

        if(not est_connexe(proposition_transport)) :
            print("La proposition n'est pas connexe.")
            break # Retirer
        
        print("La proposition est connexe.")

        
        couts_potentiels = calcul_potentiels(couts, proposition_transport)
        
        
        print("Coûts potentiels :")
        afficher_matrice(couts_potentiels, len(couts_potentiels), len(couts_potentiels[0]))
        print()

        # Ce qu'il faut faire maintenant :
        # On part d'un sommet S avec potentiel (i.e ceux reliés au sommet très connecté), et on remplit les sommets C
        # Après cela, on traite les sommets S qui n'ont pas encore de potentiel

        couts_marginaux = calcul_couts_marginaux(couts, couts_potentiels)
        
        print("Coûts marginaux :")
        afficher_matrice(couts_marginaux, len(couts_marginaux), len(couts_marginaux[0]))
        print()

        # Modifier ici, pour sortir de la boucle while si on a une proposition optimale
        if(not est_optimale(couts_marginaux)) :
            print("La proposition n'est pas optimale")
            arete = arete_a_ajouter(couts_marginaux)
            print(f"Arête : {arete}")
            
        else :
            break # Sort de la boucle

    # Après qu'on soit sorti de la boucle...
    
    print("La proposition est optimale.")
    afficher_matrice(proposition_transport, len(proposition_transport), len(proposition_transport[0]))
    print()

    cout_transport = calcul_cout_transport(couts, proposition_transport)
    print(f"Coût total de transport : {cout_transport}")

    return couts_potentiels