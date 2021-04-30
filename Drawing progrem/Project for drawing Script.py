from pygame_functions import *

screenSize(600, 600)

setBackgroundColour('black')

print("Controls")
print("b = blue")
print("r = red")
print("O = white")
print("y = yellow")
print("1 = small")
print("2 = medeum")
print("3 = large")
print("m = web")
print("w,s,d,a = moving")
                       

x=90
y=250
trace=False

colour = "white"
sizeR = 10
mreza = True

import pygame
pygame.init()
pygame.display.set_mode()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if trace == False: drawRect(x, y, sizeR, sizeR, "black", 0)
                y=y-sizeR
                drawRect(x, y, sizeR, sizeR, colour, 0)  
            if event.key == pygame.K_s:
                if trace == False: drawRect(x, y, sizeR, sizeR, "black", 0)
                y=y+sizeR
                drawRect(x, y, sizeR, sizeR, colour, 0)  
            if event.key == pygame.K_d:
                if trace == False: drawRect(x, y, sizeR, sizeR, "black", 0)
                x=x+sizeR
                drawRect(x, y, sizeR, sizeR, colour, 0)   
            if event.key == pygame.K_a:
                if trace == False: drawRect(x, y, sizeR, sizeR, "black", 0)
                x=x-sizeR
                drawRect(x, y, sizeR, sizeR, colour, 0)
            if event.key == pygame.K_r:
                colour = "#b02323"
            if event.key == pygame.K_b:
                colour = "#0d78db"
            if event.key == pygame.K_o:
                colour = "#ffffff"
            if event.key == pygame.K_y:
                colour = "#d9e000"
            if event.key == pygame.K_1:
                sizeR = 10
            if event.key == pygame.K_2:
                sizeR = 20
            if event.key == pygame.K_3:
                sizeR = 40
            if event.key == pygame.K_m:
                if mreza == True:
                    mreza = False
                else:
                    mreza = True
                for i in range(15):
                    if mreza == False:
                        drawLine(i * 40, 0, i * 40, 600, 'black')
                        drawLine(0, i * 40, 600, i * 40, 'black')
            if event.key == pygame.K_t:
                if trace == False:
                    trace = True
                else:
                    trace = False
            
    
    for i in range(15):
        if mreza == True:
            drawLine(i * 40, 0, i * 40, 600, 'gray')
            drawLine(0, i * 40, 600, i * 40, 'gray')
        
        




endWait()
