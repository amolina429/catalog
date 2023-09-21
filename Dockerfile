# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app
COPY . .

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
