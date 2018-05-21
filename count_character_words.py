character_words = {}
word_count = 0
counting = True

season_number = int(input("Season number: "))
season_length = int(input("Season length: "))

for episode in range(1, season_length + 1):
	episode_file =  "e" + str(season_number) + "-" + str(episode) + ".txt"
	transcript = open(episode_file)
	
	while True:
		line = transcript.readline()
		if " " not in line: #stop at end of file
			break
		else:
			words = line.split(" ")
			
			for word in words:
				if '[' in word: #ignore words inside brackets
					counting = False
				if counting:
					word_count += 1
				if ']' in word:
					counting = True
			character_words[words[0]] = character_words.get(words[0], 0) + word_count - 1 #the first word is the character's name
			word_count = 0

for x in character_words:
	print(x, character_words[x])