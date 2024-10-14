import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize the recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Function to capture speech input
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening for speech...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"Speech recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Error with the request; check your internet connection.")
        return None

# Function to translate text to the target language
def translate_text(text, target_language):
    translated = translator.translate(text, dest=target_language)
    print(f"Translated text: {translated.text}")
    return translated.text

# Function to convert text to speech
def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("translated_speech.mp3")
    os.system("start translated_speech.mp3")

if __name__ == "__main__":
    # Specify target language (e.g., 'fr' for French, 'es' for Spanish)
    target_language = 'es'

    print("Speak in your native language...")
    speech_text = recognize_speech()

    if speech_text:
        translated_text = translate_text(speech_text, target_language)
        # Convert the translated text back to speech
        text_to_speech(translated_text, target_language)
