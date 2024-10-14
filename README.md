# Language Translator with Speech Recognition

This project demonstrates a Python-based **Language Translator** that uses **speech recognition**, **translation**, and **text-to-speech** features. The application captures speech input, converts it to text, translates it into a target language, and plays the translated text back as speech.

## Features:
- **Speech Recognition:** Captures spoken input via a microphone and converts it to text.
- **Language Translation:** Translates the recognized text into a specified target language.
- **Text-to-Speech:** Converts the translated text into speech and plays it aloud.

## Libraries Used:
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/): For recognizing speech input.
- [`googletrans`](https://pypi.org/project/googletrans/): For translating text to different languages.
- [`gtts`](https://pypi.org/project/gTTS/): For converting text to speech (Google Text-to-Speech).
- `os`: For playing the audio file with the translated speech.

## How It Works:
1. **Speech Recognition:** The `speech_recognition` library listens to the user's speech and converts it to text using Google's speech recognition engine.
2. **Translation:** The recognized text is translated into the target language using the `googletrans` library. In this example, the default target language is Spanish (`'es'`), but this can be changed to any supported language.
3. **Text-to-Speech:** The `gtts` library then converts the translated text back into speech, saves it as an MP3 file, and plays it.

## Prerequisites:
- Python 3.x
- Install the required libraries:

```bash
pip install SpeechRecognition googletrans==4.0.0-rc1 gtts pyaudio
