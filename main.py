import time
import os
import pyautogui as pg
import pyperclip3
from tkinter import *
from tkinter import messagebox

def removerNomesRepetidos():
    inputFile = open(os.getcwd() + '/WhiteList', "r+")
    outputFile = []
    lines_seen_so_far = set()
    for line in inputFile:
        if line not in lines_seen_so_far:
            outputFile.append(line)
            lines_seen_so_far.add(line)
    inputFile.truncate(0)
    inputFile.seek(0)
    for line in outputFile:
        inputFile.write(line)
    inputFile.close()

def setDeNomes():
    inputFile = open(os.getcwd() + '/WhiteList', "r+")
    output = set()
    for line in inputFile:
        output.add(line)
    inputFile.close()
    return output

'''
Inicio dos comandos
'''
removerNomesRepetidos()

pg.keyDown('alt')
pg.press(['tab'])
pg.keyUp('alt')
time.sleep(1)
pg.press(['home'])
time.sleep(1)
pg.press(['pagedown'])
X = 0
while 1==1:
    time.sleep(1)
    pg.moveTo(380, 450+X)
    time.sleep(1)
    pg.dragTo(630, 450+X)
    time.sleep(1)
    pg.keyDown('ctrl')
    pg.keyDown('c')
    pg.keyUp('c')
    pg.keyUp('ctrl')
    time.sleep(1)

    name = pyperclip3.paste()
    name = name.decode('utf8') + '\n'

    print(name)

    Nomes = setDeNomes()

    if name not in Nomes:
        messagebox.showinfo("Remover", 'Remover amizade com "' + name + '"?')
        break

    time.sleep(1)
    pg.moveTo(805, 450+X)
    time.sleep(1)
    pg.dragTo(1050, 450+X)
    time.sleep(1)
    pg.keyDown('ctrl')
    pg.keyDown('c')
    pg.keyUp('c')
    pg.keyUp('ctrl')
    time.sleep(1)

    name = pyperclip3.paste()
    name = name.decode('utf8') + '\n'

    print(name)

    Nomes = setDeNomes()

    if name not in Nomes:
        messagebox.showinfo("Remover", 'Remover amizade com "' + name + '"?')
        break

    pg.keyDown('Down')
    pg.keyUp('Down')
    pg.keyDown('Down')
    pg.keyUp('Down')
    pg.keyDown('Down')
    pg.keyUp('Down')

    X = X + 4