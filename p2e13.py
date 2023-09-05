import numpy as np

filename = "mafalda.RAW"
with open(filename, 'rb') as f:
    line = f.readline()
    line = f.readline()
    cantidadPixeles = 256*256
    colores = [0, 0, 0, 0, 0, 0, 0, 0]  # Inicializa la lista con 8 elementos, todos en 0

    for line in f:
        line = f.readline()
        colores[int(line.strip())] += 1
        
f.close()
probabilidades =  [0, 0, 0, 0, 0, 0, 0, 0] 
cantidadInformacion = [0, 0, 0, 0, 0, 0, 0, 0]
entropia = 0
for i in range(8):
    probabilidades[i] = float(colores[i]) / cantidadPixeles
    cantidadInformacion[i] = (-1) * (probabilidades[i]) * (np.log(probabilidades[i])/np.log(2))
    entropia = entropia + cantidadInformacion[i]

print(entropia)


