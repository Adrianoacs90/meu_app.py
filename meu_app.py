import pyttsx3
import time
friend=pyttsx3.init()
volume=friend.getProperty('volume')
print=volume
friend.setProperty('volume',9.0)
voices=friend.getProperty('voices')
friend.setProperty('voice',voices[0].id)
friend.say(" ")
friend.say ("Bom dia Adriano bora trabalhar")
time.sleep(1)
friend.say("")
friend.say(" ")

friend.runAndWait()
#friend.stop
