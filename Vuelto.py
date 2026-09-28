monto = 179.45
centavos = round(monto * 100)

billetes_y_monedas = {
    "Billete de 200": 20000,
    "Billete de 100": 10000,
    "Billete de 50": 5000,
    "Billete de 20": 2000,
    "Billete de 10": 1000,
    "Moneda de 5": 500,
    "Moneda de 2": 200,
    "Moneda de 1": 100,
    "Moneda de 0.50": 50,
    "Moneda de 0.20": 20,
    "Moneda de 0.10": 10,
    "Moneda de 0.05": 5,
}

print(f"Desglose para {monto}:")
for nombre, valor in billetes_y_monedas.items():
    cantidad = centavos // valor  
    if cantidad > 0:
        print(f"{cantidad} x {nombre}")
        centavos %= valor
    


