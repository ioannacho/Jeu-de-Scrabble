from random import randint

# 1ère fonction :
def generer_lettres(difficulte):
    mots_facile = ["nez", "sel", "ami","os","aile","aide"]
    mots_moyen = ["bras", "marrakech", "cinq","bleu","paris","berlin"]
    mots_difficile = ["inconditionnellement", "anticonstitutionnellement", "Apopathodiaphulatophobie","catastrophe"]

    if difficulte == "facile":
        return mots_facile
    elif difficulte == "moyen":
        return mots_moyen
    elif difficulte == "difficile":
        return mots_difficile
    else:
        return []

# 2ème fonction :
def choisir_trois_mots(liste_mots):
    mots_choisis = []
    i = 0
    while i < 3:
        mot = liste_mots[randint(0, len(liste_mots) - 1)]
        if mot not in mots_choisis:
            mots_choisis.append(mot)
            i += 1
    return mots_choisis

# 3ème fonction :
def mots_melangees(liste_mots):
    lettres_combinees = ""
    i = 0
    while i < len(liste_mots):
        mot = liste_mots[i]
        j = 0
        while j < len(mot):
            lettres_combinees += mot[j]
            j += 1
        i += 1
    return lettres_combinees

# 4ème fonction : `
def delete_double(chaine):
    liste_unique = []
    i = 0
    while i < len(chaine):
        lettre = chaine[i]
        if lettre not in liste_unique:
            liste_unique.append(lettre)
        i += 1

    resultat = ""
    j = 0
    while j < len(liste_unique):
        resultat += liste_unique[j]
        j += 1
    return resultat

# 5ème fonction :
def choisir_mots_et_generer_lettres(difficulte):
    mots_disponibles = generer_lettres(difficulte)
    mots_choisis = choisir_trois_mots(mots_disponibles)
    lettres_melangees = mots_melangees(mots_choisis)
    lettres_uniques = delete_double(lettres_melangees)
    return mots_choisis, lettres_uniques

# 6ème fonction :
def jouer_manche(difficulte):
    mots_cibles, lettres = choisir_mots_et_generer_lettres(difficulte)

    print("Lettres mélangées : ", lettres)

    points = 0
    mots_trouves = []
    tentative = 0

    while tentative < 3:
        mot = input("Trouvez un mot (ou tapez 'Quit' pour passer) : ")

        if mot == "quit":
            tentative = 3
        elif mot in mots_cibles and mot not in mots_trouves:
            print("Bravo, mot trouvé !")
            mots_trouves.append(mot)
            points += 1
        else:
            print("Mot incorrect ou déjà trouvé.")

        tentative += 1

    print("Mots à trouver : ", end="")
    i = 0
    while i < len(mots_cibles):
        if i == len(mots_cibles) - 1:
            print(mots_cibles[i])
        else:
            print(mots_cibles[i] + ", ", end="")
        i += 1

    print("\nVous avez gagné ", points, " point(s) pour cette manche.")#\n pour sauter la ligne
    return points

# 7ème fonction :

def jouer_partie():
    niveaux_difficulte = ["facile", "moyen", "difficile"]
    total_points = 0

    i = 0
    while i < len(niveaux_difficulte):
        print("\n--- Manche", i + 1, "(Difficulté :", niveaux_difficulte[i].capitalize(), ") ---")#capitalize pour transformer la première lettre en Majuscule
        points = jouer_manche(niveaux_difficulte[i])
        total_points += points
        i += 1

    print("\nPartie terminée ! Vous avez gagné un total de", total_points, "point(s).")


jouer_partie()
