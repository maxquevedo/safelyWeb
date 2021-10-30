# safely
> Repositorio de prueba personal para proyecto de portafolio 

# Configuración de compilación
## Crear entorno virtual fuera de la carpeta safely
``` bash
# 1-) crear entorno virtual ("env" es el nombre este puede ser reemplazado por cualquiera)
python -m venv env

# 2-)Activar el entorno para trabajar
env\Scripts\activate

# Instalar requerimientos 
pip install -r requirements.txt
```

# Comandos utiles 

## Iniciar api
python manage.py runserver

## crear superuser
python manage.py createsuperuser

## Migraciones 
python manage.py makemigrations

python manage.py migrate

## Para saber que esta instalado
pip freeze --local

## Inspecciona la base de datos y coloca las tablas en models.py
``` bash
# No utilizar esto comando nuevamente, ya que puede causar errores
```
python manage.py inspectdb > .\app\models.py

## Crear app
python manage.py startapp "nombre"
