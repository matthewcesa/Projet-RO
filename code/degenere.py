# graphe.py
from collections import deque

def construire_graphe(solution):
    """
    Construit une liste d'adjacence bipartie à partir de la matrice solution.
    Les n fournisseurs sont 0..(n-1)
    Les m clients deviennent n..(n+m-1)
    """
    n = len(solution)
    m = len(solution[0])

    N = n + m
    graph = [[] for _ in range(N)]

    for i in range(n):
        for j in range(m):
            if solution[i][j] > 0:   # arête existante
                graph[i].append(n+j)
                graph[n+j].append(i)

    return graph


# ----------------------------------------------------------------------
# Détection de cycle par BFS
# ----------------------------------------------------------------------

def detect_cycle(graph):
    """
    Retourne :
    - True, cycle (liste de nœuds)   si un cycle est trouvé
    - False, None                    sinon
    """

    N = len(graph)
    visited = [False]*N
    parent = [-1]*N

    for start in range(N):
        if not visited[start]:
            queue = deque([start])
            visited[start] = True
            parent[start] = -1
            
            #BFS
            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        queue.append(v)

                    elif parent[u] != v:
                        # Cycle trouvé : reconstruire le cycle
                        return True, reconstruire_cycle(parent, u, v)

    return False, None


def reconstruire_cycle(parent, u, v):
    """
    Reconstruit le cycle BFS à partir de deux nœuds u et v
    tels que v est un voisin déjà visité mais pas parent.
    """

    chemin_u = []
    chemin_v = []

    # remonter depuis u
    x = u
    while x != -1:
        chemin_u.append(x)
        x = parent[x]

    # remonter depuis v
    y = v
    while y != -1:
        chemin_v.append(y)
        y = parent[y]

    # trouver le premier ancêtre commun
    ancêtres_u = set(chemin_u)

    lca = None
    for node in chemin_v:
        if node in ancêtres_u:
            lca = node
            break

    cycle = []

    # partie de u → ancêtre commun
    for node in chemin_u:
        cycle.append(node)
        if node == lca:
            break

    # partie de v → ancêtre commun (à l’envers)
    path_v_to_lca = []
    for node in chemin_v:
        if node == lca:
            break
        path_v_to_lca.append(node)

    cycle.extend(path_v_to_lca)

    return cycle


# ----------------------------------------------------------------------
# Vérifier la connexité
# ----------------------------------------------------------------------

def est_connexe(graph):
    """
    Vérifie si tout le graphe est connexe via BFS.
    """
    N = len(graph)
    visited = [False]*N
    queue = deque([0])
    visited[0] = True

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    # Si un sommet n'est jamais visité → non connexe
    return all(visited)


def composants_connexes(graph):
    """
    Renvoie une liste de composantes connexes (listes de sommets).
    Exemple : [[0,1,5], [2,3,4]]
    """
    N = len(graph)
    visited = [False]*N
    comps = []

    for start in range(N):
        if not visited[start]:
            queue = deque([start])
            visited[start] = True
            comp = [start]

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                        comp.append(v)
            comps.append(comp)

    return comps


# ----------------------------------------------------------------------
# Correction d’un graphe non connexe
# ----------------------------------------------------------------------

def corriger_connexite(solution):
    """
    Rend la proposition de transport connexe en ajoutant des arêtes minimales.
    On ajoute une arête (i,j) de coût minimal entre composantes.
    """

    graph = construire_graphe(solution)
    comps = composants_connexes(graph)

    if len(comps) == 1:
        return solution  # déjà connexe

    # Il y a plusieurs composantes : on les connecte
    n = len(solution)
    m = len(solution[0])

    # On relie chaque composante à la première
    comp0 = comps[0]

    for comp in comps[1:]:
        # choisir une arête i-fournisseur dans comp0 et j-client dans comp
        best_i = None
        best_j = None
        found = False

        for u in comp0:
            if u < n:  # fournisseur
                i = u
                for v in comp:
                    if v >= n:  # client
                        j = v - n
                        best_i, best_j = i, j
                        found = True
                        break
            if found:
                break

        # Ajouter l'arête choisie avec un epsilon
        if best_i is not None:
            solution[best_i][best_j] += 0.00001  # très petite valeur pour "connecter"

    return solution