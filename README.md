# 🏥 Healthcare Translation Web App with Generative AI
A real-time, multilingual translation web app to bridge communication between patients and healthcare providers.  
Built with Flask and generative AI tools for rapid development.

---

## 🎯 Objective

- 🎤 Convert spoken input from patients or doctors into live text transcripts.
- 🌍 Translate the transcript into another language with high medical accuracy.
- 🔊 Provide audio playback of the translated text for seamless conversations.

---

## 🚀 Features

- **Voice-to-Text with Generative AI**: Converts patient/doctor speech into a transcript, enhancing accuracy for medical terms.
- **Real-Time Translation**: Instantly translates the transcript into the target language.
- **Audio Playback**: Play translated speech using a "Speak" button.
- **Language Selection**: Easily choose source and target languages.
- **Mobile-First Design**: Fully responsive for mobile and desktop users.
- **Automatic Folder Management**: Automatically creates the `static/` folder if missing to store generated audio files.

---

## 📂 Project Structure

```plaintext
├── app.py            # Main Flask application
├── templates/
│   └── index.html    # Frontend page
├── static/
│   └── output.mp3    # Generated audio files (auto-created)
├── README.md         # Project documentation
```
## Technologies Used

* **Python**
* **Flask**
* **SpeechRecognition**
* **gTTS (Google Text-to-Speech)**
* **Deep Translator (Google Translate API)**
* **HTML, CSS, JavaScript (frontend)**
