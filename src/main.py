from rune import *
from interface import *
import os

def stop(entree):
    if entree == "q":
        quit(0)


def decoupage(entree):
    """Découpe l'entrée et retourne une liste contenant les différents paramètres à prendre en compte lors du calcul"""
    termes = entree.split(", ")
    elements = []
    for elem in termes:
        elements.append(elem.split(" ", 1))
    return elements


def pesee(carac, tableau_rune):
    """Retourne le poid de base d'une rune dont la caractéristique est passée en entrée"""
    resultat = 0
    for rune in tableau_rune:
        if carac == rune.getCarac():
            resultat = rune.getPoids()
    return resultat


def poid_terme(terme, tableau_rune):
    """Retourne le poid effectif d'une perte ou d'un gain d'un terme suite à l'application d'une rune"""
    """Exemple : ["+10", "Sagesse"], poid effectif : 10*3=30"""
    if "%" in terme[0]:
        coefficient = float(terme[0].replace("%", ""))  # On retire le caractère % si présent
    else:
        coefficient = float(terme[0])
    poids = pesee(terme[1], tableau_rune)
    return int(coefficient * poids)


def reliquat(saisie, tableau_rune):
    """Retourne le reliquat généré par la forge"""
    resultat = 0
    decoupe = decoupage(saisie)
    for terme in decoupe[:-1]:
        resultat += -poid_terme(terme, tableau_rune)
    return resultat


def calcul_over(caracteristique, reli, tableau_rune):
    """Calcule le nombre de runes nécessaires pour over un item en optimisant au maximum le reliquat"""
    poid = pesee(caracteristique, tableau_rune)
    if poid < 1:
        poid = 1
    resultat = reli / poid
    reste = reli % poid
    print("[+] Vous pouvez inscrire", int(resultat), "runes simples", caracteristique, "\n[!] Il vous restera alors",
          int(reste), "de reliquat")


# Initialisation du tableau de runes
pui = 0
tableau = init_rune_tab()
# assert (reliquat("+10 Sagesse, -5 Dommages critiques, -1 Portée, +reliquat", tableau) == 46)
# assert (reliquat("-91 Vitalité, -1 PA, 10 Sagesse, +reliquat", tableau) == 88)

banniere()
print("""[*] Tapez "q" pour sortir du programme""")
historique = input("[~] Copiez-collez la ligne de votre historique de forgemagie : ")
stop(historique)
pui += reliquat(historique, tableau)
print("""[+] Votre reliquat est désormais de""", pui)
code = input("(Press any key)")
stop(code)
while True:
    print(
        "[*] Que souhaitez-vous faire ?"
        "\n\n     1. Calcul d'optimisation du reliquat"
        "\n     2. Mise à jour du reliquat"
        "\n     3. Reset")
    code = input("\n[~] Entrez le numéro correspondant : ")
    stop(code)
    # os.system("clear")
    # banniere()
    if code == '1':
        carac = input("[~] Caractéristique à augmenter : ")
        stop(carac)
        calcul_over(carac, pui, tableau)
    elif code == '2':
        historique = input("[~] Copiez-collez la ligne de votre historique de forgemagie : ")
        stop(historique)
        pui += reliquat(historique, tableau)
        print("""[+] Votre reliquat est désormais de""", pui)
    elif code == '3':
        pui = 0
        print("""[+] Votre reliquat a été réinitialisé""")
        print("""[+] Votre reliquat est désormais de""", pui)
    code = input("(Press any key)")
    stop(code)
