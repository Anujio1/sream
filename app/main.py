import os
from flask import Flask, request, Response, render_template
import requests
from telegram import Bot
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Telegram Video Streamer</h1>
    <form action='/player' method='get'>
      <input type='text' name='file_id' placeholder='Enter Telegram file_id' required>
      <button type='submit'>Play</button>
    </form>
    """

@app.route('/player')
def player():
    file_id = request.args.get('file_id')
    return render_template('player.html', file_id=file_id)

@app.route('/stream/<file_id>')
def stream_video(file_id):
    # Fetch the file URL from Telegram
    tfile = bot.get_file(file_id)
    file_url = tfile.file_path

    # Forward range headers for smooth streaming
    headers = {}
    range_header = request.headers.get('Range')
    if range_header:
        headers['Range'] = range_header

    req = requests.get(file_url, headers=headers, stream=True)
    return Response(
        req.iter_content(chunk_size=8192),
        headers={
            'Content-Range': req.headers.get('Content-Range'),
            'Accept-Ranges': req.headers.get('Accept-Ranges'),
            'Content-Length': req.headers.get('Content-Length'),
            'Content-Type': req.headers.get('Content-Type')
        },
        status=req.status_code
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
