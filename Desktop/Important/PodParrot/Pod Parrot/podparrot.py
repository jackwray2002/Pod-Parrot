from numpy import *
import tkinter as tk
from tkinter import *
import pygame
import os
from command import *
from graphics import graphics

main()
menuTop()
menu1()

while True:
    pygame.display.update()
    root.update()
    glLoadIdentity()
root.mainloop() 

#def save():
#Updates the file created in saveAs()

#def saveAs():
#Should prompt a user with a file explorer window; change the name or directory

#def exit():
#Exit the program cleanly; prompt the user to save changes
    
#def bake():
#Runs when button is clicked; takes all the values and puts them into main frame
    
#def enter():
#Exits out of entry window; Checks for proper values

#def new():
#Resets the program and the values

#def open():
#Opens a new file
