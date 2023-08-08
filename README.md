# Blog con Django, Bootstrap y HTMX


## Descripción

Este proyecto es un blog implementado utilizando Django en el backend y Bootstrap, CSS, JavaScript y HTMX en el frontend. La página principal del blog carga inicialmente 10 posts y, al hacer scroll, carga 10 posts más para mejorar el rendimiento. El proyecto está dockerizado para facilitar su despliegue en entornos de producción.


## Características

- Implementación de un blog utilizando Django como backend y Bootstrap, CSS, JavaScript y HTMX como frontend.
- Paginación infinita en la página principal para cargar más posts al hacer scroll.
- Diseño atractivo y responsivo gracias a Bootstrap y CSS personalizado.
- Dockerizado para facilitar el despliegue en diferentes entornos de producción.

## Requisitos

- Python 3.x
- Docker (para el despliegue en producción)

## Instalación y Uso

1. Clona este repositorio
2. Ve a la carpeta del proyecto: `cd tu-repositorio`
3. Crea y activa un entorno virtual (opcional pero recomendado).
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta las migraciones: `python manage.py migrate`
6. Carga los datos iniciales (si los tienes): `python manage.py loaddata initial_data.json`
7. Inicia el servidor de desarrollo: `python manage.py runserver`
8. Abre tu navegador y visita `http://localhost:8000` para ver el blog en acción.

## Despliegue en Producción

El proyecto está dockerizado para facilitar su despliegue en producción. Sigue estos pasos:

1. Instala Docker en tu servidor de producción.
2. Clona el repositorio en tu servidor.
3. Ve a la carpeta del proyecto: `cd tu-repositorio`
4. Crea un archivo `.env` con las variables de entorno necesarias (por ejemplo, la configuración de la base de datos y las claves secretas).
5. Construye la imagen de Docker: `docker build -t blog-app .`
6. Ejecuta el contenedor: `docker run -d --env-file .env -p 8000:8000 blog-app`
7. Abre tu navegador y visita `http://tu-dominio` para acceder al blog en producción.

## Contribuciones

Contribuciones son bienvenidas. Si deseas mejorar el proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b mejora/funcionalidad`
3. Realiza tus cambios y commitea: `git commit -m "Añade una mejora"`
4. Haz push a la rama: `git push origin mejora/funcionalidad`
5. Abre un pull request en GitHub.

---

**Blog con Django, Bootstrap y HTMX** - Todos los derechos reservados.

Hecho con ❤️ por [emanuelB1](https://github.com/emanuelB1)
