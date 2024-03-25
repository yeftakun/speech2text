import speech_to_text as sr
import pyttsx3
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

def record_text():
    # Loop in case of errors
    while (1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer adjust the
                # energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                # listens for the user's input
                audio2 = r.listen(source2)
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")

def output_text(text):
    r = open("output.txt", "a")
    r.write(text)
    r.write("\n")
    r.close()
    return

while (1):
    text = record_text()
    output_text(text)

    print("Wrote text")