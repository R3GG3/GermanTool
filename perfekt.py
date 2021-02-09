st = ['backen', 'befinden', 'beginnen', 'bekommen', 'besprechen', 'bitten', 'bleiben', 'bringen', 'denken', 'empfehlen', 'essen', 'fahren', 'finden', 'fliegen', 'geben', 'gefallen', 'gehen', 'gewinnen', 'haben', 'hAAngen', 'heiSSen', 'helfen', 'kennen', 'kommen', 'laden', 'laufen', 'leiden', 'leihen', 'liegen', 'nehmen', 'nennen', 'reiten', 'rufen', 'schlafen', 'schlieSSen', 'schreiben', 'schwimmen', 'sehen', 'sein', 'singen', 'sitzen', 'sprechen', 'stehen', 'steigen', 'sterben', 'streiten', 'tragen', 'treffen', 'trinken', 'tun', 'verbringen', 'vergessen', 'verlieren', 'verschreiben', 'verstehen', 'wachsen', 'werden', 'wissen']
un = ['gebacken', 'befunden', 'begonnen', 'bekommen', 'besprochen', 'gebeten', 'geblieben', 'gebracht', 'gedacht', 'empfohlen', 'gegessen', 'gefahren', 'gefunden', 'geflogen', 'gegeben', 'gefallen', 'gegangen', 'gewonnen', 'gehabt', 'gehangen', 'geheiSSen', 'geholfen', 'gekannt', 'gekommen', 'geladen', 'gelaufen', 'gelitten', 'geliehen', 'gelegen', 'genommen', 'genannt', 'geritten', 'gerufen', 'geschlafen', 'geschlossen', 'geschrieben', 'geschwommen', 'gesehen', 'gewesen', 'gesungen', 'gesessen', 'gesprochen', 'gestanden', 'gestiegen', 'gestorben', 'gestritten', 'getragen', 'getroffen', 'getrunken', 'getan', 'verbracht', 'vergessen', 'verloren', 'verschrieben', 'verstanden', 'gewachsen', 'geworden', 'gewusst']

def perfect(word):
	if word in st:
		unregular(word)
		input("---DALEJ---")
	else:
		regular(word)
		input("---DALEJ---")

def regular(word):
	beginning = word[:3]
	ending = word[-5:]
	unregular_beg = ['auf', 'ein', 'uber']
	unregular_end = ['t', 'd', 'chn', 'ffn', 'mn']
	final = ""
	for x in unregular_end:
		if "t" == word[-3]:
			final = "ge"+word[:-2]+"et"
		if "d" == word[-3]:
			final = "ge"+word[:-2]+"et"
		if word.find(x) != -1 and x != "t" and x!= "d":
			final = "ge"+word[:-2]+"et"

		if final != "":
			print(final)
			return 0 

	if beginning in unregular_beg:
		final = beginning+"ge"+word[3:-2]+"t"
		print(final)

	elif ending == "ieren":
		final = word[:-2]+"t"
		print(final)

	else:
		final = "ge"+word[:-2]+"t"
		print(final)

def unregular(word):
	print(un[st.index(word)])