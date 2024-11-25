from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    # Список альбомов и треков
    albums = [
        {"name": "Трек 1", "image": "images/album1.jpg", "file": "music/song1.mp3"},
        {"name": "Трек 2", "image": "images/album1.jpg", "file": "music/song1.mp3"},
    ]
    return render_template('index.html', albums=albums)

# Для обработки запросов на скачивание трека
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('static/music', filename)

if __name__ == '__main__':
    app.run(debug=True)