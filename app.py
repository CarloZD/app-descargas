from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <body style="text-align:center; font-family:Arial;">
        <h2>Descargar video de Instagram</h2>
        <form method="POST" action="/descargar">
            <input type="text" name="url" placeholder="Pega link de Instagram" required style="width:300px;">
            <br><br>
            <button type="submit">Descargar</button>
        </form>
    </body>
    </html>
    '''

@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form['url']

    if "instagram.com" not in url:
        return "Solo se permiten enlaces de Instagram"

    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir():
        if file.startswith("video."):
            return send_file(file, as_attachment=True)

    return "Error al descargar"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)