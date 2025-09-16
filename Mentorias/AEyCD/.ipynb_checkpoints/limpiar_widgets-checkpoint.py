import json
import glob

# Busca todos los notebooks en la carpeta actual
for notebook_file in glob.glob("*.ipynb"):
    with open(notebook_file, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    # Si existe metadata de widgets, la borramos
    if "widgets" in nb.get("metadata", {}):
        del nb["metadata"]["widgets"]
        print(f"Se limpió widgets en: {notebook_file}")
    
    # Guardamos el notebook limpio
    with open(notebook_file, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
