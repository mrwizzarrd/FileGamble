import random
import tkinter as tk
import os
import pygame
import time


#This is the part that makes the game not malware, the choice to do this to themselves.
mainDirectory = input("Main directiory you want the game to delete files from: ")
if mainDirectory in ["test", "t", "testing"]:
    mainDirectory = "C:\\Users\\rverm\\Desktop\\VS Code Projects\\FileGamble\\testing"


#basic initialization
score = 0
fileList = []
for root, _, files in os.walk(mainDirectory, topdown=True):
        for file in files:
            fileList.append(os.path.join(root, file))
pygame.mixer.init()

dingSound = pygame.mixer.Sound(".\ding-101492.mp3")
evilLaugh = pygame.mixer.Sound(".\evil-laugh-89423.mp3")
#The concequences of losing the game
def YouLose():
        
    choiceFile = random.choice(fileList)
    print(choiceFile)
    os.remove(choiceFile)
    return(choiceFile)


root = tk.Tk()

root.geometry("5000x825")
root.title("File Gamble")
Label1 = tk.Label(root, text="Welcome to the game!", font = ("Comic Sans", 15))
Label1.pack(pady=10)

ScoreLabel = tk.Label(root, text=f"Score: {score}", font = ("Comic Sans", 15))
ScoreLabel.pack(pady=11)
root.configure(background='black')

def onButtonClick(num):
    global score
    nums = ["1", "2", "3", "4", "5", "6"]
    choice = random.choice(nums)
    if num == choice:
        evilLaugh.play()
        Label1.config(text=f"{YouLose()} deleted!")
        score = 0
        ScoreLabel.config(text=f"Score: {score}")
    else:
        Label1.config(text=f"Safe!")
        dingSound.play()
        score += 1
        ScoreLabel.config(text=f"Score: {score}")
        




button1 = tk.Button(root, text="1", width = 50, height = 3, bg ="#1c8c85",  command=lambda: onButtonClick("1")).pack(pady=12)
button2 = tk.Button(root, text="2", width = 50, height = 3, bg ="#1c8c85", command=lambda: onButtonClick("2")).pack(pady=14)
button3 = tk.Button(root, text="3", width = 50, height = 3, bg ="#1c8c85", command=lambda: onButtonClick("3")).pack(pady=16)
button4 = tk.Button(root, text="4", width = 50, height = 3, bg ="#1c8c85", command=lambda: onButtonClick("4")).pack(pady=18)
button5 = tk.Button(root, text="5", width = 50, height = 3, bg ="#1c8c85", command=lambda: onButtonClick("5")).pack(pady=20)
button6 = tk.Button(root, text="6", width = 50, height = 3, bg ="#1c8c85", command=lambda: onButtonClick("6")).pack(pady=22)
quitButton = tk.Button(root, text="QUIT", width = 50, height = 3, bg ="#FF0000", command=lambda: root.quit()).pack(pady=24)

root.mainloop()




