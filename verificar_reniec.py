import csv

def procesar_reniec():
    print("--- Iniciando consulta de Miembro de Mesa ---")
    with open('datos.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(f"DNI: {row['dni']} | Nombre: {row['nombres']}")
            print(f"¿Es Miembro?: {row['miembro_de_mesa']} | Ubicación: {row['ubicacion']}")
            print(f"Dirección Local: {row['direccion']}")
            print("-" * 40)

if __name__ == "__main__":
    procesar_reniec()
