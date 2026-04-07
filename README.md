Instagram Video Downloader (Docker)

Aplicación web desarrollada con Flask que permite descargar videos de Instagram mediante una interfaz simple.

Repositorio:
https://github.com/CarloZD/app-descargas.git

Requisitos

Antes de empezar, asegúrate de tener instalado:

Docker
Git (opcional, para clonar el repositorio)
Instalación y uso
1. Clonar el repositorio
git clone https://github.com/CarloZD/app-descargas.git
cd app-descargas
2. Construir las imágenes
Versión base
docker build -t insta-downloader:v1 .
Versión optimizada (Alpine)
docker build -f Dockerfile.optimizado -t insta-downloader:v2-alpine .
Versión multi-stage
docker build -f Dockerfile.multistage -t insta-downloader:v3-multistage .

3. Ejecutar el contenedor

Ejecuta solo una versión a la vez.

Ejecutar versión base
docker run -d -p 5000:5000 --name insta-container insta-downloader:v1
Ejecutar versión optimizada
docker run -d -p 5000:5000 --name insta-container insta-downloader:v2-alpine
Ejecutar versión multi-stage
docker run -d -p 5000:5000 --name insta-container insta-downloader:v3-multistage

4. Acceder a la aplicación

Abrir en el navegador:

http://localhost:5000

5. Uso de la aplicación
Pegar un enlace de Instagram (video o reel público)
Hacer clic en Descargar
El archivo se descargará automáticamente

6. Comandos útiles

Ver imágenes creadas
docker images
Ver contenedores en ejecución
docker ps
Ver logs
docker logs insta-container
Detener contenedor
docker stop insta-container
Eliminar contenedor
docker rm insta-container
🏷️ Versionado
v1 → versión base
v2-alpine → imagen optimizada (menor tamaño)
v3-multistage → construcción en múltiples etapas
