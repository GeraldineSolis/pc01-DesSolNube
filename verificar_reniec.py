import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def scraping_reniec():
    print("--- Iniciando Proceso de Scraping (Simulado para PC1) ---")
    
    # Configuración de Chrome para Docker/Alpine
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Ruta del driver en Alpine
    service = Service(executable_path="/usr/bin/chromedriver")
    
    resultados = []
    
    try:
        # Intentar iniciar el driver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Leer datos.csv
        with open('datos.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                dni = row['dni']
                # Filtrar: Solo procesar si tiene un cargo asignado
                if row['miembro_de_mesa'].lower() != "no es miembro":
                    print(f"DNI {dni}: Procesado como {row['miembro_de_mesa']}")
                    resultados.append(row)
                else:
                    print(f"DNI {dni}: Descartado (No es miembro)")
        
        driver.quit()

        # Guardar resultados.csv
        if resultados:
            keys = resultados[0].keys()
            with open('resultados.csv', 'w', newline='', encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys, delimiter=';')
                dict_writer.writeheader()
                dict_writer.writerows(resultados)
            print("--- Archivo 'resultados.csv' generado con éxito ---")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    scraping_reniec()
