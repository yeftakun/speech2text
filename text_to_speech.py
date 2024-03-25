from gtts import gTTS
import pygame
import os
import keyboard

def ngomong():
    # Baca isi file translated.txt
    with open("./output/translated.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Sintesis teks menjadi audio dengan bahasa Indonesia
    tts = gTTS(text=text, lang="id")

    # Simpan audio dalam file "output.mp3"
    tts.save("./output/output.mp3")

    # Inisialisasi Pygame
    pygame.init()

    # Putar audio
    pygame.mixer.music.load("./output/output.mp3")
    pygame.mixer.music.play()

    # Loop utama
    running = True
    while running:
        # Periksa tombol 'f' ditekan
        if keyboard.is_pressed('f'):
            running = False

        # Tunggu hingga audio selesai diputar
        pygame.time.Clock().tick(10)
        if not pygame.mixer.music.get_busy():
            running = False

    # Hentikan Pygame
    pygame.quit()

ngomong()
os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan terminal
