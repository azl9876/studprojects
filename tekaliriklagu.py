import pyttsx3
import time
import random

skor = 0
#bil_cuba = 0

# Define the verses of the songs
verses_gerimis_mengundang = [
    "pernah juga kau pinta perpisahan",
    "aku sangkakan itu hanyalah gurauan",
    "nyata kau serius dalam senyuman"
    ]

verses_demi_masa = [
    "Sihat sebelum sakit",
    "Muda sebelum tua",
    "Kaya sebelum miskin",
    "Lapang sebelum sempit",
]

verses_warisan = [
    "andai ku terbiar tak diterima",
    "andai aku disingkirkan",
    "kemana harus ku bawakan",
    "Ke mana harusku semaikan cinta ini",
]

verses_tinggal_kenangan = [
    "Pernah ada rasa cinta antara kita",
    "Kini tinggal kenangan",
    "Ingin ku lupakan semua tentang dirimu",
 ]

verses_tepuk_tangan = [
    "bila rasa gembira tepuk tangan",
    "bila rasa gembira beginilah caranya",
    "bila rasa gembira tepuk tangan",
 ]

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to play a verse
def play_verse(verse):
    engine.say(verse)
    engine.runAndWait()
    time.sleep(2)  # Add a pause between verses

# Function to select a random song
def select_song():
    song = random.choice(["gerimis_mengundang","warisan", "demi_masa", "tinggal_kenangan","tepuk_tangan"])
    return song

print("*********************************")
print("SILA DENGAR DENGAN TELITI")
print("TEKA NAMA LAGU TERSEBUT")
print("*********************************")

# Game loop
while True:
    # Select a random song
    #bil_cuba +=1
    song = select_song()

    # Play the verses based on the selected song
    if song == "gerimis_mengundang":
        for verse in verses_gerimis_mengundang:
            play_verse(verse)
    elif song == "demi_masa":
        for verse in verses_demi_masa:
            play_verse(verse)
    elif song == "tinggal_kenangan":
        for verse in verses_tinggal_kenangan:
            play_verse(verse)
    elif song == "tepuk_tangan":
        for verse in verses_tepuk_tangan:
            play_verse(verse)
    elif song == "warisan":
        for verse in verses_warisan:
            play_verse(verse)       
            
    # Ask the player to guess the song's name
    guess = input("TEKA NAMA LAGU: ")

    # Check if the guess is correct
    if song == "gerimis_mengundang" and guess.lower() == "gerimis mengundang":
        print("Congratulations! You guessed it right!")
        skor = skor + 5
    elif song == "demi_masa" and guess.lower() == "demi masa":
        print("Congratulations! You guessed it right!")
        skor = skor + 5
    elif song == "tinggal_kenangan" and guess.lower() == "tinggal kenangan":
        print("Congratulations! You guessed it right!")
        skor = skor + 5
    elif song == "tepuk_tangan" and guess.lower() == "tepuk tangan":
        print("Congratulations! You guessed it right!")
        skor = skor + 5
    elif song == "warisan" and guess.lower() == "warisan":
        print("Congratulations! You guessed it right!")
        skor = skor + 5
    else:
        print("Oops! Maaf anda salah. Tajuk lagu yang betul ialah '{}'.".format(song.capitalize()))

    # Ask if the player wants to replay
    replay = input("Nak main lagi? (ya/tidak): ")
    if replay.lower() != "ya":
        break
# paparkan skor player
print("Skor anda ialah:", skor)

# Clean up the text-to-speech engine
engine.stop()
