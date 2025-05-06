# 🗂️ Proyecto Django de Gestión de Tareas

Una aplicación web desarrollada con Django que permite la gestión de proyectos y tareas.  
Los usuarios pueden crear proyectos, añadir tareas a estos proyectos y gestionar su estado fácilmente.

---

## 📋 Requisitos previos

- Python 3.8 o superior  
- Django 5.2  
- Pip (gestor de paquetes de Python)

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crear un entorno virtual
```bash
python -m venv venv 
```

### 3. Activar el entorno virtual
En Windows
```bash
venv\Scripts\activate
```

En MacOS/Linux
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar la base de datos
```bash
python manage.py migrate
```

### 6. Crear un superusuario(opcional)
```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

---

Gracias por usar este proyecto de referencia. Si lo usas, por favor dar créditos.
