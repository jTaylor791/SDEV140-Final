import tkinter as tk

class Game:
    def __init__(self, name, kills, deaths, matches):
        self.name = name
        self.kills = kills
        self.deaths = deaths
        self.matches = matches

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getKills(self):
        return self.kills
    
    def setKills(self, newKills):
        self.kills = newKills

    def getDeaths(self):
        return self.deaths
    
    def setDeaths(self, newDeaths):
        self.deaths = newDeaths

    def getMatches(self):
        return self.matches()
    
    def setMatches(self, newMatches):
        self.matches = newMatches

    def calculateStats(self):
        nameString = str(self.name)
        killTotal = self.kills
        deathTotal = self.deaths
        matchTotal = self.matches
        averageKD = killTotal / deathTotal
        avgKillsPerMatch = killTotal / matchTotal
        avgDeathsPerMatch = deathTotal / matchTotal
        print("Your average KD in", nameString, "is:", averageKD)
        print("Your average kills per match in", nameString, "is:", avgKillsPerMatch)
        print("Your average deaths per match in", nameString, "is:", avgDeathsPerMatch)

class Counter:
    def __init__(self):
        self.gameList = []
    
    def addGame(self, gameInput):
        print("add game ran")
        #self.gameList.append(gameInput)
    
    def showAllStats(self):
        for game in self.gameList:
            game.calculateStats()
    
    def hasGame(self, inputName):
        for game in self.gameList:
            if game.getName() == inputName:
                return True
        return False
    
    def updateGame(self):
        print("update game ran")

def main():
    newCounter = Counter()
    while True:
        try:
            userInput = str("Enter a game you would like to track, a game being tracked, or nothing to quit: ")
            if userInput == "":
                break
            elif newCounter.hasGame(userInput):
                newCounter.updateGame()
            else:
                newCounter.addGame()
        except:
            print("Enter a valid input")

if __name__ == "__main__":
    main()