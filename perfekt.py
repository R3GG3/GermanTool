###LIBRARIES###
st = ['backen', 'befinden', 'beginnen', 'bekommen', 'besprechen', 'bitten', 'bleiben', 'bringen', 'denken', 'empfehlen', 'essen', 'fahren', 'finden', 'fliegen', 'geben', 'gefallen', 'gehen', 'gewinnen', 'haben', 'hAAngen', 'heiSSen', 'helfen', 'kennen', 'kommen', 'laden', 'laufen', 'leiden', 'leihen', 'liegen', 'nehmen', 'nennen', 'reiten', 'rufen', 'schlafen', 'schlieSSen', 'schreiben', 'schwimmen', 'sehen', 'sein', 'singen', 'sitzen', 'sprechen', 'stehen', 'steigen', 'sterben', 'streiten', 'tragen', 'treffen', 'trinken', 'tun', 'verbringen', 'vergessen', 'verlieren', 'verschreiben', 'verstehen', 'wachsen', 'werden', 'wissen']
un = ['gebacken', 'befunden', 'begonnen', 'bekommen', 'besprochen', 'gebeten', 'geblieben', 'gebracht', 'gedacht', 'empfohlen', 'gegessen', 'gefahren', 'gefunden', 'geflogen', 'gegeben', 'gefallen', 'gegangen', 'gewonnen', 'gehabt', 'gehangen', 'geheiSSen', 'geholfen', 'gekannt', 'gekommen', 'geladen', 'gelaufen', 'gelitten', 'geliehen', 'gelegen', 'genommen', 'genannt', 'geritten', 'gerufen', 'geschlafen', 'geschlossen', 'geschrieben', 'geschwommen', 'gesehen', 'gewesen', 'gesungen', 'gesessen', 'gesprochen', 'gestanden', 'gestiegen', 'gestorben', 'gestritten', 'getragen', 'getroffen', 'getrunken', 'getan', 'verbracht', 'vergessen', 'verloren', 'verschrieben', 'verstanden', 'gewachsen', 'geworden', 'gewusst']

def perfect(word):
	if word in st:
		unregular(word)
	else:
		regular(word)

def regular(word):
	

def unregular(word):
	print(un[st.index(word)])