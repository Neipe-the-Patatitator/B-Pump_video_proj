import json

with open("./data/workouts.json", "r") as read_file:
    data = json.load(read_file)

def fetchSugar(exercice):
    """
    Récupère le titre associé au sugar d'un exo

    :param exercice: Le nom de l'exercice
    :return: Le titre de l'exo
    """
    parsed = data['workouts'][exercice]
    return parsed['sugar']['title']

def fetchPosition(exercice):
    """
    Récupère les positions des points à afficher sur le graphique

    :param exercice: Le nom de l'exercice
    :return: Les positions des points à afficher
    """
    parsed = data['workouts'][exercice]['position']
    positions = [(point['milieu_x'], point['milieu_y']) for point in parsed]
    return positions