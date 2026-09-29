class Paquetes:
    def __init__(self, precio, peso):
        self.precio = precio
        self.peso = peso

cantidad_Paquetes = 8
lis_precio = [3, 1.8, 3, 2, 3, 4, 2, 1]
lis_peso = [3, 2, 4, 3, 7, 10, 5, 3]
lis_paquetes = []

for carga in range(cantidad_Paquetes):
    precio = lis_precio[carga]
    peso = lis_peso[carga]
    paquete = Paquetes(precio, peso)
    lis_paquetes.append(paquete)

Peso_Mochila = int(input("Ingrese el peso de la mochila: "))

lis_porcentaje = []
for porcentaje in range(cantidad_Paquetes):
    lis_porcentaje.append(float(lis_paquetes[porcentaje].precio) / lis_paquetes[porcentaje].peso)

Monto_Total = 0
indice = 0
for peso in range(cantidad_Paquetes):
    if(Peso_Mochila >= lis_paquetes[peso].peso):
        Peso_Mochila -= lis_paquetes[peso].peso
        Monto_Total += lis_paquetes[peso].precio
        indice = peso
    else:
        break
        
if Peso_Mochila > 0:
  siguiente_indice = indice + 1
  if siguiente_indice < cantidad_Paquetes:
    Monto_Total += lis_porcentaje[siguiente_indice] * Peso_Mochila

print("Monto Total obtenido:", Monto_Total.__round__(2))
        
