#!/bin/bash
# Esto le dice a Linux que use bash para ejecutar

# Instalar dependencias
pip install -r requirements.txt

# Recoger archivos estáticos
python manage.py collectstatic --noinput

# Aplicar migraciones
python manage.py migrate
