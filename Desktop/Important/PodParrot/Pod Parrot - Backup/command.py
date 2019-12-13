from numpy import *
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pygame
import os
from main import *

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
right_height = int(round(int(screen_height) * .5, 4))
action_height = int((right_height)*.5)
main_width = int(round(int(screen_width) * .7, 4))
right_width = int(round(int(screen_width) * .3, 4))
frameRightCenter = int((int(right_width) / 2) + int(main_width))

frameRight = tk.Frame(root, bg='#240090', width=right_width, height=right_height)
frameAction = tk.Frame(root, bg='#000000', width=right_width, height=right_height)

frameMain = tk.Frame(root, bg='#282828', width=main_width, height=screen_height)
frameMain.grid(row=0, column=0, columnspan=main_width, rowspan=screen_height, sticky=NE)
os.environ['SDL_WINDOWID'] = str(frameMain.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((main_width,screen_height))
screen.fill(pygame.Color(40,40,40))
pygame.display.init()
pygame.display.update()

menubar = tk.Menu(root, fg="#190061")
file = tk.Menu(menubar, tearoff=0)
edit = tk.Menu(menubar, tearoff=0)
help = tk.Menu(menubar, tearoff=0)

massEntry = tk.Entry(frameAction)
strengthEntry = tk.Entry(frameAction)
initialVelocityEntry = tk.Entry(frameAction)
initialHeightEntry = tk.Entry(frameAction)
spinEntry = tk.Entry(frameAction)
particleEntry = tk.Entry(frameAction)

entryList = [1]

def main():
    root.title('Pod Parrot')
    root.state('zoomed')
    frameMain.grid(row=0, column=0, columnspan=main_width, rowspan=screen_height, sticky=NE)
    screen.fill(pygame.Color(40,40,40))
    pygame.display.init()
    pygame.display.update()
    frameRight.grid(row=0, column=main_width, columnspan=right_height, rowspan=right_width, sticky=NW)
    frameAction.grid(row=right_height, column=main_width, columnspan=right_width, rowspan=right_height, sticky=NW)

def saveAs():
    mass = massEntry.get()
    strength = strengthEntry.get()
    initialvelocity = initialVelocityEntry.get()
    initialheight = initialHeightEntry.get()
    spin = spinEntry.get()
    particle = particleEntry.get()

    entryList.append(mass)
    entryList.append(strength)
    entryList.append(initialvelocity)
    entryList.append(initialheight)
    entryList.append(spin)
    entryList.append(particle)
    #root.filename = filedialog.asksaveasfilename()
    #print(root.filename)

def menu1():
    massLbl = tk.Label(frameAction, text = "Mass", fg="#FFFFFF", bg="#282828", padx = 31)
    massLbl.place(relx=.1, y=10)
    massEntry.place(relx=.35, y=10)

    stengthLbl = tk.Label(frameAction, text = "Strength", fg="#FFFFFF", bg="#282828", padx = 22)
    stengthLbl.place(relx=.1, y=50)
    strengthEntry.place(relx=.35, y=50)

    initialVelocityLbl = tk.Label(frameAction, text = "Initial Velocity", fg="#FFFFFF", bg="#282828", padx = 7)
    initialVelocityLbl.place(relx=.1, y=90)
    initialVelocityEntry.place(relx=.35, y=90)

    initialHeightLbl = tk.Label(frameAction, text = "Initial Height", fg="#FFFFFF", bg="#282828", padx = 10)
    initialHeightLbl.place(relx=.1, y=130)
    initialHeightEntry.place(relx=.35, y=130)

    spinLbl = tk.Label(frameAction, text = "Spin", fg="#FFFFFF", bg="#282828", padx = 32)
    spinLbl.place(relx=.1, y=170)
    spinEntry.place(relx=.35, y=170)

    particleLbl = tk.Label(frameAction, text = "Surface Particles", fg="#FFFFFF", bg="#282828")
    particleLbl.place(relx=.1, y=210)
    particleEntry.place(relx=.35, y=210)

    bakeButton = tk.Button(frameAction, text = "Bake", padx = 150)
    bakeButton.place(relx =.1, y=300)

def menuTop():
    file.add_command(label="New")
    file.add_command(label="Open")
    file.add_command(label="Save")
    file.add_command(label="Save as...", command = saveAs())
    file.add_command(label="Close")
    file.add_separator()
    file.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file)
    edit.add_command(label="Undo")
    edit.add_separator()
    edit.add_command(label="Cut")
    edit.add_command(label="Copy")
    edit.add_command(label="Paste")
    edit.add_command(label="Delete")
    edit.add_command(label="Select All")
    menubar.add_cascade(label="Edit", menu=edit)
    help.add_command(label="About")
    help.add_command(label="Credits")
    menubar.add_cascade(label="Help", menu=help)
    root.config(menu=menubar)