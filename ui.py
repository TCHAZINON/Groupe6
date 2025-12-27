import tkinter as tk
from tkinter import messagebox
from gpx_generator import choix_ville, build_gpx_content, save_gpx

patrimoines = []

def ajouter_patrimoine():
    ville = entry_ville.get().strip()
    nom = entry_nom.get().strip()
    lat = entry_lat.get().strip()
    lon = entry_lon.get().strip()

    if not ville or not nom or not lat or not lon:
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
        return

    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        messagebox.showerror("Erreur", "Latitude et longitude invalides")
        return

    patrimoines.append({
        "ville": ville,
        "nom": nom,
        "lat": lat,
        "lon": lon
    })

    messagebox.showinfo("Ajout", f"{nom} ajouté à {ville}")

    entry_nom.delete(0, tk.END)
    entry_lat.delete(0, tk.END)
    entry_lon.delete(0, tk.END)


def generate():
    city = entry_ville.get().strip()
    results = choix_ville(patrimoines, city)

    if not results:
        messagebox.showinfo("GPX", "Aucun patrimoine pour cette ville.")
        return

    content = build_gpx_content(results, city)
    filename = f"{city}_patrimoines.gpx"
    path = save_gpx(filename, content)

    messagebox.showinfo("GPX", f"Fichier généré :\n{path}")


# ================= UI =================
app = tk.Tk()
app.title("Générateur GPX – Groupe 6")
app.geometry("350x350")

tk.Label(app, text="Ville").pack()
entry_ville = tk.Entry(app)
entry_ville.pack()

tk.Label(app, text="Nom du patrimoine").pack()
entry_nom = tk.Entry(app)
entry_nom.pack()

tk.Label(app, text="Latitude").pack()
entry_lat = tk.Entry(app)
entry_lat.pack()

tk.Label(app, text="Longitude").pack()
entry_lon = tk.Entry(app)
entry_lon.pack()

tk.Button(app, text="Ajouter le patrimoine", command=ajouter_patrimoine).pack(pady=5)
tk.Button(app, text="Générer GPX", command=generate).pack(pady=5)

app.mainloop()
