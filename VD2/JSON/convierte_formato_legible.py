import json

# Explora la estuctura de datos.
nombreFichero = './VD2/JSON/datos/eq_data_1_day_m1.json'
with open(nombreFichero) as f:
    todos_los_datos = json.load(f)

fichero_legible = './VD2/JSON/datos/datos_terremotos_legible.json'
with open(fichero_legible, 'w') as f:
          json.dump(todos_los_datos,f,indent=4)

