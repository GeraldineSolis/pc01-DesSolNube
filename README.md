# Sistema de Verificación de Miembros de Mesa - Dockerizado 🗳️

Este proyecto consiste en una aplicación Python que utiliza **Selenium** y **Chromium** para procesar datos de ciudadanos y filtrar a los Miembros de Mesa. Está diseñado para ejecutarse en entornos de nube (AWS) mediante contenedores optimizados.

## 🚀 Características
- **Web Scraping Ready**: Equipado con Selenium y Google Chromium Headless.
- **Optimización de Imágenes**: Tres versiones de Dockerfile para comparar eficiencia.
- **Persistencia de Datos**: Uso de Volúmenes para exportar resultados al host.
- **Seguridad**: Implementación de usuarios no-root en versiones optimizadas.

## 🛠️ Instalación y Construcción

Para construir la imagen más eficiente (Multi-stage), ejecute:
```bash
docker build -t reniec-app:final -f Dockerfile.multistage .
```

## 📋 Ejecución

Para procesar el archivo datos.csv y obtener el reporte resultados.csv en su carpeta local, use el siguiente comando:
```bash
docker run --rm -v $(pwd):/app reniec-app:final
```
