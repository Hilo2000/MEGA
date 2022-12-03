import speech_recognition as sr
import pyttsx3

#Thanks to GeeksforGeeks.org for supplying MEGA with this substantual amout of code.
r = sr.Recognizer()
#Install useless crap for lazy ppl who want to type r instead of sr.Recognizer()


def Listen():
	try:
		#Uses mic
		with sr.Microphone() as source2:

			#IDK I just followed the tutorial for this one
			r.adjust_for_ambient_noise(source2, duration=0.2)

			#Something useful
			audio2 = r.listen(source2)

			#Exploiting Google for recognisable words
			Result = r.recognize_google(audio2)
			Result = Result.lower()

			#Returs what the person was saying
			return(Result)

		#More useless error crap
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

	except sr.UnknownValueError:
		print("unknown error occurred")
