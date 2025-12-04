def choisir_Nb_Probleme():
    # Demande un entier à l'utilisateur et assure qu'il est compris entre 0 et 14 inclus.
    while True:
        try:
            # input() récupère la saisie de l'utilisateur.
            # int() converti cette saisie en entier.
            userInput = int(input("Veuillez choisir un problème à résoudre (1 à 12) :\n"))
            
            # Vérifie que l'entrée soit comprise entre 1 et 12.
            if userInput >= 1 and userInput <= 12:
                # Si les conditions sont remplies, retourner le nombre choisi.
                return userInput
            
            # Si les conditions ne sont PAS remplies :
            else:
                # Test si l'entier est négatif ou null.
                if userInput <= 0:
                    print("Erreur : L'entier doit être positif.")
                else: # i.e. nombre > 12.
                    print("Erreur : Les entiers supérieurs à 12 sont exclus.")
        
        except ValueError:
            # Si l'utilisateur n'a pas saisie un entier :
            print("Erreur : Ce n'est pas un entier valide. Veuillez réessayer.")

def choisir_Algo():
    # Demande un entier à l'utilisateur et assure qu'il est compris entre 0 et 14 inclus.
    while True:
        # input() récupère la saisie de l'utilisateur.
        # int() converti cette saisie en entier.
        userInput = input("Veuillez entrer le nom de l'algorithme à appliquer\n")

        # On convertit la saisie en majuscules pour faciliter la comparaison.
        userInput = userInput.upper()

        match userInput:
            case "NORD-OUEST" | "NORD OUEST" | "NO" :
                print("Vous avez choisi l'Algorithme Nord-Ouest.")
                return "NO"
            case "BALAS-HAMMER" | "BH" :
                print("Vous avez choisi l'Algorithme de Balas-Hammer.")
                return "BH"
            case _:
                print("Erreur : Veuillez choisir un algorithme parmi les suivants :" \
                    "Nord-Ouest, Balas-Hammer, Marche-Pied avec Potentiel.")

def rester_Sur_Meme_Probleme():
    # Demande une confirmation à l'utilisateur en lui demandant de saisir 'o' ou 'n'.
    # Retourne True si l'utilisateur saisit 'o' (oui), et False s'il saisit 'n' (non).
    while True:
        reponse = input("Voulez-vous résoudre un autre problème de transport ? (o/n) : ").strip().lower()
        if reponse == 'o':
            return True
        elif reponse == 'n':
            return False
        else:
            print("Erreur : Veuillez répondre par 'o' pour oui ou 'n' pour non.")