#### Imports et définition des variables globales
import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Retourne le contenu du fichier <filename> sous forme de liste de listes d'entiers.

    Args:
        filename (str): Nom du fichier à lire

    Returns:
        list: Le contenu du fichier (1 liste par ligne)
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    return [list(map(int, line.strip().replace(';', ',').split(','))) for line in lines]

def get_list_k(data, k):
    """Retourne la k-ième liste de data.

    Args:
        data (list): Liste de listes
        k (int): Indice de la liste à retourner

    Returns:
        list: La k-ième liste
    """
    return data[k] if 0 <= k < len(data) else []

def get_first(l):
    """Retourne le premier élément de la liste.

    Args:
        l (list): Liste d'entiers

    Returns:
        int: Premier élément de la liste
    """
    return l[0] if l else None

def get_last(l):
    """Retourne le dernier élément de la liste.

    Args:
        l (list): Liste d'entiers

    Returns:
        int: Dernier élément de la liste
    """
    return l[-1] if l else None

def get_max(l):
    """Retourne le maximum de la liste.

    Args:
        l (list): Liste d'entiers

    Returns:
        int: Maximum de la liste
    """
    return max(l) if l else None

def get_min(l):
    """Retourne le minimum de la liste.

    Args:
        l (list): Liste d'entiers

    Returns:
        int: Minimum de la liste
    """
    return min(l) if l else None

def get_sum(l):
    """Retourne la somme des éléments de la liste.

    Args:
        l (list): Liste d'entiers

    Returns:
        int: Somme des éléments de la liste
    """
    return sum(l) if l else 0

#### Fonction principale

def main():
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(f"Liste {i}: {l}")

    k = 1  # Exemple d'indice
    print(f"Liste à l'indice {k}: {get_list_k(data, k)}")

    if data:
        example_list = data[0]  # On prend la première liste comme exemple
        print(f"Première liste: {example_list}")
        print(f"Premier élément: {get_first(example_list)}")
        print(f"Dernier élément: {get_last(example_list)}")
        print(f"Maximum: {get_max(example_list)}")
        print(f"Minimum: {get_min(example_list)}")
        print(f"Somme: {get_sum(example_list)}")

if __name__ == "__main__":
    main()
