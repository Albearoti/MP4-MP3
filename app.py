from flask import Flask, request, send_from_directory, jsonify
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/convert', methods=['POST'])
def convert():
    video_file = request.files['file']
    filename = os.path.splitext(video_file.filename)[0] + '.mp3'
    filepath = os.path.join('static', filename)
    clip = VideoFileClip(video_file.stream)
    clip.audio.write_audiofile(filepath)
    clip.close()
    return jsonify({"success": True, "filename": filename})

if __name__ == '__main__':
    app.run(debug=True)
