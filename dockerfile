# Imagen base oficial
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia archivos de dependencias
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

RUN python manage.py migrate 

# Expone el puerto por defecto de Django
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
