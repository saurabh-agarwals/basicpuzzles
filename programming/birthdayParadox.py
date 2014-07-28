import urllib2
from BeautifulSoup import BeautifulSoup
import re

template = "{0:10} {1:20} {2:30} {3:40}"
data = open("fifa.html",'r').read()
soup = BeautifulSoup(data)
#soup = getPlayersDataFromWiki()


def setGlobalVaribales():
	global soup
	if soup is None:
		soup = getPlayersDataFromWiki()

def getPlayersDataFromWiki():
	url = "http://en.wikipedia.org/wiki/2014_FIFA_World_Cup_squads"
	info = BeautifulSoup(urllib2.urlopen(url).read())
	return info

def getPlayersList():
	playersList = []
	teams = getTeamsByCountry()
	print len(teams)
	for team in teams:
		for row in team['playersTable'].findAll("tr"):
			cells = row.findAll("td")
			if len(cells) > 0:
				name = cells[2].find(text=True)
				bday = cells[3].find("span", { "class" : "bday" }).find(text=True)
				club = cells[5].findChildren()[3].find(text=True)
				eachProcess = {'name':name, 'bday':bday,'club':club,'country':team['country']}
				playersList.append(eachProcess)
	return playersList

def getTeamsByCountry():
	listOfCountries = getAllCountryName()
	tables = soup.findAll("table")
	teamList = []
	for table in tables:
		team = table.find("table", { "class" : "sortable jquery-tablesorter" })		
		if team:			
			myTeam = {'country':listOfCountries[0],'playersTable':team}
			teamList.append(myTeam)
			listOfCountries.remove(listOfCountries[0])
	return teamList

def createPlayersInfoStructure(playersList):
	players = {}
	for player in playersList:
		if players.has_key(player['bday']):
			players[player['bday']].append(player)
		else:
			players[player['bday']] = [player]		
	
	for info in players:
		if len(players[info]) >= 2:
			print template.format("BIRTHDAY" ,"NAME", "CLUB" , "COUNTRY")
			print ("*************************************************")
			#Put logic of sharing birthday with two differnt countries
			#print players[info]
			for player in players[info]:
				print template.format(player['bday'].encode('utf-8').strip(), player['name'].encode('utf-8').strip(), 
					player['club'].encode('utf-8').strip(), player['country'].encode('utf-8').strip())


def getAllCountryName():	
	countries = []	
	countryList = soup.findAll(False,{'class': re.compile(r'\btoclevel-2\b')})
	for country in countryList[:32]:
		country = country.find("span",{"class":"toctext"})
		countries.append(country.getText())
	return countries

#setGlobalVaribales()
playersList = getPlayersList()
createPlayersInfoStructure(playersList)
