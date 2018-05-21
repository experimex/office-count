import os

for filename in os.listdir("characters"):
	os.remove("characters/" + filename)