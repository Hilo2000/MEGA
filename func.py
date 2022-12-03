import pywhatkit as kt
import urllib.request
import re

def sort(line):

	if line == None:
		return("ERROR")
	
	#X is the line that is broken into a list by each space
	x = line.split()
	
	#Looks for words "Search" and "Play" and returns a letter based off of the result where as E is to return an error.
	if len(x) < 2:
		return("ERROR")
	
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
		
