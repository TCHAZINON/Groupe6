import os


def choix_ville(patrimoines, city):
    return [p
            for p in patrimoines
            if p["ville"].lower() == city.lower()]

def calcul_centre_ville(patrimoines, city):
    latitudes = [p["lat"] for p in patrimoines]
    longitudes = [p["lon"] for p in patrimoines]

    if not latitudes or not longitudes:
        return None

    return {
        "nom": f"Centre de {city}",
        "lat": sum(latitudes) / len(latitudes),
        "lon": sum(longitudes) / len(longitudes),
        "ville": city,
        "type": "centre"
    }



def build_gpx_content(patrimoines, city):
    content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    content += '<gpx version="1.1" creator="Groupe6">\n'

    # 🔹 Centre de la ville (toujours)
    centre = calcul_centre_ville(patrimoines, city)
    if centre:
        content += f'  <wpt lat="{centre["lat"]}" lon="{centre["lon"]}">\n'
        content += f'    <name>{centre["nom"]}</name>\n'
        content += '    <sym>Star</sym>\n'
        content += '    <type>CentreVille</type>\n'
        content += '  </wpt>\n'

    # 🔹 Monuments (s’ils existent)
    for p in patrimoines:
        content += f'  <wpt lat="{p["lat"]}" lon="{p["lon"]}">\n'
        content += f'    <name>{p["nom"]}</name>\n'
        content += '    <sym>Historic</sym>\n'
        content += '    <type>Monument</type>\n'
        content += '  </wpt>\n'

    content += '</gpx>'
    return content



def save_gpx(filename, content):
    # Dossier de sortie dans le même dossier que le script
    output_dir = os.path.join(os.path.dirname(__file__), "exports")

    # Créer le dossier si nécessaire
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Chemin complet du fichier
    full_path = os.path.join(output_dir, filename)

    # Écriture du fichier
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    return full_path
