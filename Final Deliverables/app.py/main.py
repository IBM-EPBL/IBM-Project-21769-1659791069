import pyttsx3

text_speech = pyttsx3.init()

answer = input("How is the day MR jayasuriya: ")

text_speech.say(answer)
text_speech.runAndWait()
text_speech.say()