import pywhatkit as kt
import urllib.request
import re
import speech_recognition as sr
import pyttsx3

def sort(line):

	if line == None:
		return("ERROR")

	#X is the line that is broken into a list by each space
	x = line.split()
	
	if len(x) < 2:
		return("ERROR")
	
	#Looks for words "Search" and "Play" and returns a letter based off of the result where as E is to return an error.
	for word in x:
		if word == "search":
			return("S") 
		if word == "play":
			return("P")
		if word == "exit":
			return("X")
		else:
			return("E")

def filterx(linef):
	
	#Same varibles as last time but Y can be used
	a = linef.split()
	b = ""
	
	#Reconstructs a string, but instead, removes words "Search" or "Play" to limit search results
	for think in a:
		if think != "search":
			print("Loading...")
			b = b + think + " "
			 
		if think != "play":
			print("Loading...")
			b = b + think + " "
		else:
			print("Sorting...")
	return(b)

#Uses the kt module to make a google search	
def googlesearch(zline):
	kt.search(zline)

#Uses 2 diffrent modules to find the link to the first youtube video based on search, and then looks it up.
def youtubesearch(line):
	search_keyword = "line"
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	print("")
	print("DEBUG: https://www.youtube.com/watch?v=" + video_ids[0])
	print("")
	kt.search("https://www.youtube.com/watch?v=" + video_ids[0])
	
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
		
		
print(" ")
print("███╗░░░███╗███████╗░██████╗░░█████╗░")
print("████╗░████║██╔════╝██╔════╝░██╔══██╗")
print("██╔████╔██║█████╗░░██║░░██╗░███████║")
print("██║╚██╔╝██║██╔══╝░░██║░░╚██╗██╔══██║")
print("██║░╚═╝░██║███████╗╚██████╔╝██║░░██║")
print("╚═╝░░░░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝")
print("WORLDS FIRST OPEN-SOURCE ASSISTANT")
print("")

#TERMS
print("Terms and conditions---")
print("Microphone---")
print("This program uses microphone settings for a better experiance. It is proven to not track or record any personalised text or voice recordings. For more information please refer to privacy article III. Microphone usage in MEGA is limited to search results. Microphone ussage will be turned on for the entire duriation of the program starting after terms and conditions is accepeted. Any questions about microphone usage can go to: mielo.symeonidis@gmail.com")
print("")
print("Browser Settings---")
print("MEGA is optimized for Firefox usage only any other program may be fatal to MEGA's programming and servers may be temerarly down after MEGA missusage. MEGA is also proven NOT to track web data and other privacy on Firefox.")
print("")
print("Privacy---")
print("We care about your privacy, and to make sure your search results are never used against you, or in benifit of others, the MEGA team will always clear all data copies of MEGA and any other saved data that was not intended to be stored. MEGA master copy is the only exeption to resets as it will always be stored in a flash drive and cannot be removed. To reset all other copies of MEGA, the master copy will automatically replace the flash drive of the other copy of MEGA. After updates and re-programms the main MEGA computer will have to be nuked in order to contain computer spyware, trogans, viruses, and hackers.")
print("")
print("Data---")
print("Data may be recorded in the local drive. This data includes a history, and other sensitve information. To make sure this data is secure, we have included no phyiscal saved data so that when the MEGA program is closed, any prerecorded and presant data can be wiped and then secure. If you have any conserns about your privacy, please result to aricle III. Any further questions can go to: mielo.symeondis@gmail.com")
print("")
print("Usage---")
print("To use MEGA, please enter multi word commands starting with search or play dpending on the platform |Google or Youtube|. You can also exit by starting a sentince off with exit. DO NOT using single word sentinces or do not use multiple keywords.")
print("")
print("By continuing onto MEGA software, you agree to these terms...")
input(">>>")

message = "Welcome to MEGA! Following this message, the microphone for your new voice assistant will activate. Use keywords search and play at the start of a sentince to trigger a command. Thank you for choosing MEGA!"

print(message)

print("Also remember that if you want to exit out of MEGA, please say exit to the microphone.")

def Loop():
	word = Listen()
	print(word)
	y = sort(word)
	if y == "S":
		z = filterx(word)
		googlesearch(z)
	if y == "P":
		z = filterx(word)
		youtubesearch(z)
	if y == "x":
		quit()
	if y == "Error":
		print("TRY AGAIN")
	else:
		print("Try again")


x = True
while x == True:
	Loop()
	input("Press to Cont.>>>")
	

