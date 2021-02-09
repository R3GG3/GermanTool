# -*- coding: utf-8 -*-
###LIBRARIES###
import requests

def translate(word):
	try:
		f = open("translator.txt")
		ok = 0
		for i in f.readlines():
			x = i
			x = x.replace("\n", "")
			if i == "" or i == " " or i =="\n":
				continue
			if ok == 1:
				print("\nPo polsku to: "+x)
				return 0
			if x == word:
				ok = 1
		del ok
		f.close()

	except:
		f = open("translator.txt", "a")
		f.write("")
		f.close()


	link = "https://www.google.com/search?q={0}+na+polski".format(word)
	
	#UTF-8 ISSUES, MANUALLY NEEDED
	encoded = ['&#263;', '&#322;', '&#380;']
	decoded = ['ć', 'ł', 'ż']

	scrapper = requests.get(link)
	scrapper.encoding = "utf-8"
	scrapping = scrapper.text
	scrapping = scrapping[scrapping.index("lrtl-translation-text"):]
	scrapping = scrapping[:scrapping.index("</div>")]
	scrapping = scrapping[scrapping.index(">")+1:]
	word2 = scrapping
	while word2.find("&") != -1:
		#try:
		for i in encoded:
			last = word2[word2.index("&"):word2.index(";")+1]
			if i == last:
				letter = decoded[encoded.index(i)]
				word2 = word2.replace(last, letter)
		#except:
			#pass

	f = open("translator.txt", "a")
	f.write(word+"\n")
	f.write(word2+"\n")
	f.close()
	
	print("\nPo polsku to: "+word2)
	input("---DALEJ---")