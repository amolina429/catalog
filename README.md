# Backend Technical Test

Proyecto Catálogo basado en Django - Django Rest Framework.
A continuación presento algunos elementos utilizados para el desarrollo de la aplicación

Login y autenticación: 
* django-rest-framework simple-jwt

Usuarios: 
* Modelo de usuarios de Django con implementación de permisos de administrador o usuario no administrador.

Notificaciones y/o envio de correos:
* smtplib, email, email.MIME.

Contenedorización:
* docker-compose

Documentacion:
* Documentación realizada en postman https://documenter.getpostman.com/view/16708282/2s9YCBt9Dg
* Documentación realizada con rest_framework.documentation.include_docs_urls. (/api/v1/docs/). Esta documentación es una herramienta para la depuraración.

# Proceso de ejecución de la aplicación con docker: 
- docker-compose run web python manage.py createsuperuser
- docker-compose run web python manage.py makemigrations
- docker-compose run web python manage.py migrate
- docker-compose up --build
