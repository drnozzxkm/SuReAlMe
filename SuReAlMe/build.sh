#!/bin/bash
# Este script instala dependencias y recopila archivos estáticos

pip install -r requirements.txt
python manage.py collectstatic --noinput
