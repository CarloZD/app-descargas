 Cómo usar
1. Construir la imagen
docker build -t insta-downloader:v1 .
2. Ejecutar el contenedor
docker run -d -p 5000:5000 insta-downloader:v1
3. Abrir en el navegador

Ir a:

http://localhost:5000
4. Descargar video
Pegar un link de Instagram
Hacer clic en Descargar
Versiones disponibles
v1 → versión base
v2-alpine → optimizada (más ligera)
v3-multistage → multi-stage

Ejemplo:

docker run -d -p 5000:5000 insta-downloader:v2-alpine
 Nota
Solo funciona con links públicos de Instagram
Algunos videos pueden no descargarse por restricciones
