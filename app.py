from flask import Flask, request, render_template, jsonify
import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
import io
import os

app = Flask(__name__)

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file:
        filepath = 'uploaded_audio.wav'
        file.save(filepath)

        recognizer = sr.Recognizer()
        with sr.AudioFile(filepath) as source:
            audio = recognizer.record(source)

        try:
            transcript = recognizer.recognize_google(audio)
            return jsonify({"transcript": transcript})

        except sr.UnknownValueError:
            return jsonify({"error": "Google Speech Recognition could not understand audio"})

        except sr.RequestError as e:
            return jsonify({"error": f"Could not request results from Google Speech Recognition service; {e}"})


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio_file = request.files['audio']
    audio_content = audio_file.read()

    recognizer = sr.Recognizer()

    with sr.AudioFile(io.BytesIO(audio_content)) as source:
        audio = recognizer.record(source)

        try:
            transcript = recognizer.recognize_google(audio)
            return jsonify({"transcript": transcript})
        except sr.UnknownValueError:
            return jsonify({"error": "Google Web Speech API could not understand the audio."})
        except sr.RequestError:
            return jsonify({"error": "Could not request results from Google Web Speech API."})


@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    target_language = data.get('target_language')

    try:
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text')
    language = data.get('language')

    try:
        # Ensure the static folder exists
        if not os.path.exists('static'):
            os.makedirs('static')

        tts = gTTS(text=text, lang=language, slow=False)
        output_file = 'static/output.mp3'
        tts.save(output_file)

        return jsonify({"message": "Audio saved", "audio_url": output_file})

    except ValueError as e:
        return jsonify({"error": f"Error: {str(e)}"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
