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
        killTotal = int(self.kills)
        deathTotal = int(self.deaths)
        matchTotal = int(self.matches)
        averageKD = killTotal / deathTotal
        avgKillsPerMatch = killTotal / matchTotal
        avgDeathsPerMatch = deathTotal / matchTotal
        print("Your average KD in", nameString, "is:", averageKD)
        print("Your average kills per match in", nameString, "is:", avgKillsPerMatch)
        print("Your average deaths per match in", nameString, "is:", avgDeathsPerMatch)
        return "Your average KD in", nameString, "is:", averageKD, "\nYour average kills per match in", nameString, "is:", avgKillsPerMatch, "\nYour average deaths per match in", nameString, "is:", avgDeathsPerMatch
    

class Counter(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.gameList = []

        kill_entry = tk.StringVar()
        game_entry = tk.StringVar()
        death_entry = tk.StringVar()
        match_entry = tk.StringVar()
        self.wm_title("Kill Counter")
        self.geometry("500x500")
        container = tk.Frame(self, height=400, width=600)
        titleLabel = tk.Label(self, text="Kill tracker").grid(row = 0)
        gameLabel = tk.Label(self, text="Enter game name:").grid(row = 1)
        killEntryLabel = tk.Label(self, text="Enter kill amount:").grid(row = 2)
        deathEntryLabel = tk.Label(self, text="Enter death amount:").grid(row=3)
        matchLabel = tk.Label(self, text="Enter matches played").grid(row=4)
        gameEntry = tk.Entry(self, textvariable=game_entry)
        killEntry = tk.Entry(self, textvariable=kill_entry)
        deathEntry = tk.Entry(self, textvariable=death_entry)
        matchEntry = tk.Entry(self, textvariable=match_entry)
        gameEntry.grid(row = 1, column = 1)
        killEntry.grid(row = 2, column = 1)
        deathEntry.grid(row = 3, column = 1)
        matchEntry.grid(row = 4, column = 1)
        submitButton = tk.Button(self, text="Submit", width=25, command = lambda : self.submitPressed(game_entry.get(),kill_entry.get(),death_entry.get(),match_entry.get())).grid(row=5)
        calculate_entry = tk.StringVar()
        calculateLabel = tk.Label(self, text="Enter game name you want to calculate stats for:").grid(row=6)
        calculateEntry = tk.Entry(self, textvariable=calculate_entry)
        calculateEntry.grid(row = 6, column = 1)
        calculateButton = tk.Button(self, text="Calculate", width=50, command = lambda : self.findGameStats(calculate_entry.get())).grid(row=7)
        stats_message = tk.StringVar()
        stats_message.set("Stats show here")
        statsMessage = tk.Message(self, textvariable=stats_message, bg="grey", width="100").grid(row=8)
        self.stats_message = stats_message


    def findGameStats(self, gameName):
        for game in self.gameList:
            if game.getName() == gameName:
                self.stats_message.set(game.calculateStats())

    def submitPressed(self, name, kills, deaths, matches):
        print(name)
        gameCheck = self.hasGame(str(name))
        if gameCheck == False:
            game = Game(str(name), str(kills), str(deaths), str(matches))
            self.addGame(game)
        else:
            self.updateGame()

    def updateGame(self, gameToUpdate, kills, deaths, matches):
        for game in self.gameList:
            if game.getName() == gameToUpdate:
                game.setKills(game.getKills()+kills)
                game.setDeaths(game.getDeaths()+deaths)
                game.setMatches(game.getMatches()+matches)

    def addGame(self, gameInput):
        print("add game ran")
        self.gameList.append(gameInput)
    
    def showAllStats(self):
        for game in self.gameList:
            game.calculateStats()
    
    def hasGame(self, inputName):
        for game in self.gameList:
            if game.getName() == inputName:
                return True
        return False


def main():
    newCounter = Counter()
    newCounter.mainloop()

if __name__ == "__main__":
    main()