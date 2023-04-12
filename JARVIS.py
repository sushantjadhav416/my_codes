import pyttsx3
import datetime

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
	 engine.say(audio)
	 engine.runAndWait()

def wishme():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good morning sir!")

	elif hour>=12 and hour<=18:
		speak("Good  sir!")
	
	elif hour>=19:
		speak("Good afternoon sir!")


speak("Hello handsome, i'm FRIDAY !,How can i help you!")



if __name__ == "__main__":
	 wishme()
	 