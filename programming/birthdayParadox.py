import urllib2
from BeautifulSoup import BeautifulSoup
import re
from datetime import datetime
import collections

'''
we need to find out find how many teams out of the 32 have at least 2 
players who share the same birthday. 
'''

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

def getPlayersListByCountry():
	playersList = []
	teams = getTeamsByCountry()
	for team in teams:
		initTeam = {team['country']:[]}
		#initTeam = [{team['country']:{[]}]
		for row in team['playersTable'].findAll("tr"):
			cells = row.findAll("td")
			if len(cells) > 0:
				name = cells[2].find(text=True)
				bday = cells[3].find("span", { "class" : "bday" }).find(text=True)
				#bday = datetime.strptime(bday, '%Y-%m-%d').strftime('%-d %B %Y')
				bday = datetime.strptime(bday, '%Y-%m-%d').strftime('%-d %B')
				club = cells[5].findChildren()[3].find(text=True)
				#eachProcess = {'name':name, 'bday':bday,'club':club}
				#eachProcess = {'bday':bday}
				eachProcess = bday
				initTeam[team['country']].append(eachProcess)
		playersList.append(initTeam)
	return playersList

def findCommandBithday():	
	newList = {}
	birthDayList = []
	birthDayListByCountry = getPlayersListByCountry()
	print birthDayListByCountry
	count = len(birthDayListByCountry)
	for index, playersByCountry in enumerate(birthDayListByCountry):
		for jindex, element in enumerate(birthDayListByCountry):
			if index == jindex:
				continue
			birthDayList1 = set(birthDayListByCountry[index].values()[0])
			birthDayList2 = set(birthDayListByCountry[jindex].values()[0])
			commanBithDay = birthDayList1.intersection(birthDayList2)				
			commanBithDay = list(commanBithDay)
			if commanBithDay:	
				process = birthDayListByCountry[index].keys()[0]
				if newList.has_key(process):
					newList[process].append({birthDayListByCountry[jindex].keys()[0]:commanBithDay})
				else:
					newList[process] = [{birthDayListByCountry[jindex].keys()[0]:commanBithDay}]
	for key in newList:
		if len(newList[key]) > 2:
			print key + " : " + "True"
		#print key, newList[key], len(newList[key])
		'''
		print "********************"
		print key, newList[key], len(newList[key]) 
		print "********************"
		'''
	return newList

def findComman():	
	newList = []
	count = 0
	birthDayList = []
	birthDayListByCountry = getPlayersListByCountry()
	#print birthDayListByCountry
	for index, item in enumerate(birthDayListByCountry):
		cout = birthDayListByCountry[index].values()[0]
		process =  {birthDayListByCountry[index].keys()[0]:[x for x, y in collections.Counter(cout).items() if y > 1]}
		newList.append(process)

	for i in newList:		
		if len(i.values()[0])>=2:
			count = count + 1
			print i.keys()[0] + " : " + "True" + " " + str(i.values()[0])
		#else:
			#print i.keys()[0] + " : " + "False" + " " + str(i.values()[0])
	print "Total Number of countries is" + " " + str(count)

findComman()


