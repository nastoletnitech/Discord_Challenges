import pygame as pg
from string import ascii_uppercase
from random import randint

class Interface:
    def __init__(self, width, height):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.font = pg.font.SysFont('yugothicyugothicuilight', 30)
        self.botFont = pg.font.SysFont('bahnschrift', 30)
        self.running = True
        pg.display.set_caption("Last is First")
        self.botWord = "dwunastnica"
        self.playerWord = ""
        self.score = 0
        self.wordList = []
        self.firstLetterList = []
        self.start_ticks = 0
        self.seconds = 0
        self.timeLimit = 5
        self.initializeWordList()
        self.starIcon = pg.image.load("images/star.png")
        self.timeColors = {
            "good": (255, 255, 255),
            "hurry": (255, 140, 0),
            "bad": (255, 0, 0)
        }

    def initializeWordList(self):
        with open("slowa-nopl.txt") as file:
            for row in file:
                row = row.strip()
                self.wordList.append(row)
                self.firstLetterList.append(row[0])
        self.firstLetterList = "".join(self.firstLetterList)

    def startTimer(self):
        self.seconds = 0
        self.start_ticks = pg.time.get_ticks()

    def calculateTime(self):
        self.seconds = (pg.time.get_ticks() - self.start_ticks) / 1000

    def printTimer(self):
        timeLeft = round(self.timeLimit-self.seconds,1)
        percentage = timeLeft/self.timeLimit*100
        if percentage > 50:
            color = self.timeColors['good']
        elif percentage > 20:
            color = self.timeColors['hurry']
        else:
            color = self.timeColors['bad']
        seconds = f"Time left: {timeLeft}"
        message = self.botFont.render(seconds, True, color)
        messageWidth = self.botFont.size(seconds)[0]
        x = (self.width - messageWidth)/2
        y = 200
        self.screen.blit(message, (x, y))

    def printScore(self):
        score = str(self.score)
        message = self.botFont.render(score, True, (255, 255, 255))
        messageWidth = self.botFont.size(score)[0]
        x = self.width - (self.width - messageWidth) / 8
        y = 50
        self.screen.blit(message, (x, y))
        self.screen.blit(self.starIcon, (x+30, y))

    def printBotWord(self):
        message = self.botFont.render(self.botWord.upper(), True, (0,0,205))
        messageWidth = self.botFont.size(self.botWord.upper())[0]
        x = (self.width - messageWidth)/2
        y = 100
        self.screen.blit(message, (x, y))

    def printUserInputArea(self):
        width = 2*self.width/3
        height = 100
        x = (self.width - width)/2
        y = 300
        area = pg.Rect(x, y, width, height)
        pg.draw.rect(self.screen, (255, 255, 255), area)

    def printUserInputMessage(self):
        message = self.botFont.render(self.playerWord.upper(), True, (0, 0, 205))
        messageWidth = self.botFont.size(self.playerWord.upper())[0]
        x = (self.width - messageWidth) / 2
        y = 330
        self.screen.blit(message, (x, y))

    def checkWord(self):
        if self.playerWord == "":
            self.playerLose()
        elif self.botWord[-1] != self.playerWord.lower()[0]:
            self.playerLose()
        elif self.playerWord.lower() not in self.wordList:
            self.playerLose()
        else:
            self.playerWin()
        self.playerWord = ""
        self.startTimer()

    def newBotWord(self):
        firstLetter = self.playerWord.lower()[-1]
        a = self.firstLetterList.index(firstLetter)
        b = self.firstLetterList.rindex(firstLetter)
        self.botWord = self.wordList[randint(a, b)]

    def playerLose(self):
        self.score = 0
        print("Player LOST")

    def playerWin(self):
        self.score += 1
        print("Good job")
        self.newBotWord()

    def main(self):
        self.startTimer()
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYUP:
                    if chr(event.key).upper() in ascii_uppercase:
                        self.playerWord += chr(event.key)
                    elif event.key == pg.K_BACKSPACE:
                        self.playerWord = self.playerWord[0:-1]
                    elif event.key == pg.K_RETURN:
                        self.checkWord()
            self.calculateTime()
            if self.seconds > self.timeLimit:
                self.checkWord()
            self.screen.fill((0, 207, 145))
            self.printScore()
            self.printTimer()
            self.printBotWord()
            self.printUserInputArea()
            self.printUserInputMessage()
            pg.display.update()
