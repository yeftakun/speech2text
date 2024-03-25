import deepl
import os
import pyttsx3
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

translator = deepl.Translator(os.getenv("DEEPL_API_KEY")) # Inisialisasi objek Translator dengan API key DeepL

with open('./output/output.txt', 'r') as file:
    word = file.read()

result = translator.translate_text(word, target_lang="ID")
translated_text = result.text  # Mendapatkan teks hasil terjemahan dari objek TextResult

with open("./output/log.txt", "a") as file:
    file.write("Translate: " + translated_text + "\n") # Append the translated text to the log.txt file
with open("./output/translated.txt", "w") as file:
    file.write(translated_text)    # Write the translated text to the translated.txt file
    
print("Translate " + translated_text)
