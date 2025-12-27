def choix_ville(patrimoines, city):
    return [
        p for p in patrimoines
        if p["ville"].lower() == city.lower()
    ]


def calcul_centre_ville(patrimoines, city):
    lats = [p["lat"] for p in patrimoines]
    lons = [p["lon"] for p in patrimoines]

    if not lats:
        return None

    return {
        "nom": f"Centre de {city}",
        "lat": sum(lats) / len(lats),
        "lon": sum(lons) / len(lons),
        "ville": city
    }


def build_gpx_content(patrimoines, city):
    content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    content += '<gpx version="1.1" creator="Groupe6">\n'

    centre = calcul_centre_ville(patrimoines, city)
    if centre:
        content += f'''  <wpt lat="{centre["lat"]}" lon="{centre["lon"]}">
    <name>{centre["nom"]}</name>
    <sym>Star</sym>
    <type>CentreVille</type>
  </wpt>\n'''

    for p in patrimoines:
        content += f'''  <wpt lat="{p["lat"]}" lon="{p["lon"]}">
    <name>{p["nom"]}</name>
    <sym>Historic</sym>
    <type>Monument</type>
  </wpt>\n'''

    content += '</gpx>'
    return content


def save_gpx(filename, content):
    import os

    output_dir = os.path.join(os.path.dirname(__file__), "exports")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path
