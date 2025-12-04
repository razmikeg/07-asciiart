"""
Module de gestion de l'encodage ASCII art.

Ce module contient deux fonctions pour encoder une chaîne de caractères
en une liste de tuples (caractère, nombre d'occurrences).
"""

#### Imports et définition des variables globales

import sys

# Augmente la limite de récursion pour traiter de grandes chaînes
sys.setrecursionlimit(2000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    caracteres = [s[0]]
    occurrences = [1]
    # On parcourt la chaîne à partir du 2ème caractère
    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            occurrences[-1] += 1
        else:
            caracteres.append(s[k])
            occurrences.append(1)
    return list(zip(caracteres, occurrences))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    char_courant = s[0]
    count = 1
    # On compte tant que l'on ne dépasse pas la taille et que le caractère est identique
    while count < len(s) and s[count] == char_courant:
        count += 1
    return [(char_courant, count)] + artcode_r(s[count:])
#### Fonction principale


def main():
    """
    Fonction principale du programme.
    
    Elle permet de vérifier le bon fonctionnement des fonctions 
    d'encodage itérative et récursive via des affichages dans la console.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
