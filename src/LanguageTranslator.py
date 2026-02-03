from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os
from mtranslate import translate
import tkinter as tk
from tkinter import ttk

# A dictionary containing language names and their corresponding ISO language codes
languages = {
    "afrikaans": "af",
    "albanian": "sq",
    "hindi": "hi",
    "zulu": "zu",
    "english": "en",
    "spanish": "es",
    "italian": "it",
    "german": "de",
    "french": "fr",
    "russian": "ru",
    "chinese": "zh",
    "japanese": "ja",
    "korean": "ko",
    "arabic": "ar",
    "portuguese": "pt",
    "turkish": "tr",
    "dutch": "nl",
    "swedish": "sv",
    "greek": "el",
    "polish": "pl",
    "czech": "cs",
    "hungarian": "hu",
    "romanian": "ro",
    "danish": "da",
    "norwegian": "no",
    "finnish": "fi",
    "thai": "th",
    "vietnamese": "vi",
    # Add more languages as needed
}


# Capture Voice - takes command through the microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query

# Translate and speak the text
def translate_and_speak():
    query = takecommand()
    while query == "None":
        query = takecommand()

    # Get the destination language from the user's input
    to_lang = to_lang_entry.get()
    to_lang = to_lang.lower()

    # Mapping user input to ISO language code
    to_lang_code = languages.get(to_lang)

    # Check if the user-provided language is valid
    while to_lang_code is None:
        print("Language is currently not available, please input another language.")
        to_lang = to_lang_entry.get()
        to_lang = to_lang.lower()
        to_lang_code = languages.get(to_lang)

    # Translating from source to destination using the mtranslate module
    translated_text = translate(query, to_lang_code)

    # Using gTTS to convert translated text to speech
    speak = gTTS(text=translated_text, lang=to_lang_code, slow=False)
    speak.save("captured_voice.mp3")

    # Using OS module to play the translated voice
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')

    # Printing Output
    translated_text_label.config(text=translated_text)

# Create a Tkinter window
window = tk.Tk()
window.title("Voice Translator")
window.geometry("500x300")  # Set the window size

# Create a frame to center the content
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create GUI elements with rounded borders
style = ttk.Style()
style.configure("TButton", relief="flat", background="#3498db", foreground="red")
style.map("TButton", background=[("active", "#2980b9")])

to_lang_label = ttk.Label(frame, text="Enter the language in which you want to convert:")
to_lang_label.grid(row=0, column=0, padx=10, pady=5)

to_lang_entry = ttk.Entry(frame)
to_lang_entry.grid(row=0, column=1, padx=10, pady=5)

translate_button = ttk.Button(frame, text="Translate and Speak", command=translate_and_speak)
translate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

translated_text_label = ttk.Label(frame, text="")
translated_text_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter main loop
window.mainloop()
