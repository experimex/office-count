import urllib.request
from bs4 import BeautifulSoup

season_number = int(input("Season number: "))
season_length = int(input("Season length: "))

for episode in range(1, season_length + 1):
	filename = "scripts/" + str(season_number) + "-" + str(episode) + ".txt"
	file = open(filename, 'w') #create file
	
	if episode < 10:
		episode = "0" + str(episode) #to match the website url
	page = urllib.request.urlopen("http://officequotes.net/no" + str(season_number) + "-" + str(episode) + ".php")
	soup = BeautifulSoup(page, "html.parser")
	
	for div in soup.find_all("div", {"class": "DSblock"}): #get rid of deleted scenes
		div.decompose()
	for stuff_box in soup.find_all("div", attrs={"class": "quote"}):
		file.write(stuff_box.text.strip() + "\n")
	file.close()