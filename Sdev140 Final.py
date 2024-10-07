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

def main():
    testGame = Game("Fortnite", 500, 10, 10)
    testGame.calculateStats()
    anotherTest = Game("Halo", 745, 452, 328)
    anotherTest.calculateStats()

if __name__ == "__main__":
    main()