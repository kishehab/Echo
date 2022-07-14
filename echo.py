from flask import Flask, render_template, request
from datetime import date
from flask_cors import CORS, cross_origin
import speech_recognition as sr
from scipy.io import wavfile
import numpy as np


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    today = date.today()
    return"Today date is: " + today.strftime("%Y")

# upload file

@app.route('/uploader', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        fl = request.files['file']
        blob = fl.read()
        f = open("audio.wav", "wb")
        f.write(blob)
        f.close()
        # initialize the recognizer
        r = sr.Recognizer()
        harvard = sr.AudioFile('audio.wav')
        # open the file
        text = 'Something went wrong while processing the voice.'
        with harvard as source:
            try:
                # listen for the data (load audio to memory)
                audio = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio)
            except Exception as e:
                 print(e)
    return text

app.run(host='localhost', port=5000)
