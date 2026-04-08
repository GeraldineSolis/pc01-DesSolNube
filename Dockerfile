FROM python:3.11-slim
WORKDIR /app
COPY datos.csv .
COPY verificar_reniec.py .
CMD ["python", "verificar_reniec.py"]
