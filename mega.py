from speach import *
from func import *

#---------Intro
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
	if y == "Error":
		print("TRY AGAIN")
	if y == "x":
		quit()
	else:
		print("Try again")

x = True
while x == True:
	Loop()
	


