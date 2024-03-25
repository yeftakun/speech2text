import speech_recognition
import pyttsx3
import keyboard
import os

recognizer = speech_recognition.Recognizer()

recording = False  # Menandakan apakah sedang dalam proses rekaman

while True:
    try:
        if keyboard.is_pressed('f'):  # Check if the "f" button is pressed
            if not recording:  # Jika belum merekam
                # Clear the terminal
                os.system('cls' if os.name == 'nt' else 'clear')
                # Clear the contents of the output.txt file
                with open("./output/output.txt", "w") as file:
                    file.write("")
                print("Loading...")
                recording = True  # Menandakan bahwa sedang merekam
                
                with speech_recognition.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Record...")  
                    audio = recognizer.listen(mic, timeout=6)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Recognizing...")
                    text = recognizer.recognize_google(audio)
                    text = text.lower()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("You say : ", text)

                    with open("./output/output.txt", "a") as file:
                        file.write(text + "\n")  # Append the recognized text to the file
                    with open("./output/log.txt", "a") as file:
                        file.write("You say : " + text + "\n")

                os.system('python translate.py')  # Run the translate.py script
                os.system('python text_to_speech.py')
            
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
