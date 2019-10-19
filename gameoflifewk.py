#!/usr/bin/env python
#author:wk 2019.10.18

import tkinter
import numpy
import time

EDGE_WIDTH = 2
WIN_SIZE_X = 200
WIN_SIZE_Y = 200
CUBE_SIZE = 20
MAX_CELL_X = (int) (WIN_SIZE_X/CUBE_SIZE)
MAX_CELL_Y = (int) (WIN_SIZE_Y/CUBE_SIZE)
	
isrun = True

def main():	
    window = tkinter.Tk()

    window.title("game of life")
    window.geometry('700x700')
    la = tkinter.Label(window, text = 'input', bg='yellow',font=('Arial', 12),width=30,height=2)
    la.pack()
    bt2 = tkinter.Button(window, anchor='e',bg='blue',width = 10, height=10,text='end',command = beginCallBack)
    bt2.pack()
    cv = tkinter.Canvas(window, width=WIN_SIZE_X+2*EDGE_WIDTH, height=WIN_SIZE_Y+2*EDGE_WIDTH, bg = 'black')
    cv.pack()
    world = numpy.random.randint(0,2, (MAX_CELL_X,MAX_CELL_Y))
    T_world = world.copy()
    global isrun
    while True:
        if isrun == True:
            cv.delete('rect')
            draw(cv, world, T_world)        
            world = T_world.copy()
            window.update_idletasks()
            window.update()
            isrun = False
        window.update_idletasks()
        window.update()


    window.mainloop()

def draw(cv, world, T_world):
    for i in range(MAX_CELL_X):
        for j in range(MAX_CELL_Y):
            if world[i,j] == 1:
                cv.create_rectangle(i*CUBE_SIZE+EDGE_WIDTH, j*CUBE_SIZE+EDGE_WIDTH,
                (i+1)*CUBE_SIZE+EDGE_WIDTH, (j+1)*CUBE_SIZE+EDGE_WIDTH,
                fill='white', outline='blue', tags='rect')
            #draw netline
            if i == 0:
                cv.create_line(i*CUBE_SIZE, j*CUBE_SIZE, MAX_CELL_X*CUBE_SIZE, j*CUBE_SIZE, fill='red')
            if j == 0:
                cv.create_line(i*CUBE_SIZE, j*CUBE_SIZE, i*CUBE_SIZE, MAX_CELL_Y*CUBE_SIZE, fill='red')
            #判断生命下一状态
            if i == 0 and j == 0: #左上角
                aliveCell = world[i+1,j] + world[i+1,j+1]+world[i,j+1]
                revelution(T_world, aliveCell, i, j)
            elif i == MAX_CELL_X-1 and j == 0: #右上角
                aliveCell = world[i-1,j]+world[i-1,j+1]+world[i,j+1]
                revelution(T_world, aliveCell, i, j)
            elif i == 0 and j == MAX_CELL_Y-1: #左下角
                aliveCell = world[i,j-1]+world[i+1,j-1]+world[i+1,j]
                revelution(T_world, aliveCell, i, j)
            elif i == MAX_CELL_X-1 and j == MAX_CELL_Y-1: #右下角
                aliveCell = world[i-1,j]+world[i-1,j-1]+world[i,j-1]
                revelution(T_world, aliveCell, i, j)
            elif j==0: #上边界
                aliveCell = world[i-1,j]+world[i-1,j+1]+world[i,j+1]+world[i+1,j+1]+\
                            world[
                                i+1,j]
                revelution(T_world, aliveCell, i, j)
            elif j == MAX_CELL_Y-1: #xiabianjie
                aliveCell = world[i-1,j]+world[i-1,j-1]+world[i,j-1]+world[i+1,j-1]+\
                            world[
                                i+1,j]
                revelution(T_world, aliveCell, i, j)
            elif i == 0: #zuobianjie
                aliveCell = world[i,j-1]+world[i+1,j-1]+world[i+1,j]+world[i+1,j+1]+\
                            world[
                                i,j+1]
                revelution(T_world, aliveCell, i, j)
            elif i == MAX_CELL_X-1: #youbianjie
                aliveCell = world[i,j-1]+world[i-1,j-1]+world[i-1,j]+world[i-1,j+1]+\
                            world[
                                i,j+1]
                revelution(T_world, aliveCell, i, j)
            else:
                aliveCell = world[i-1,j-1]+world[i,j-1]+world[i+1,j-1]+world[i+1,j]+\
                            world[
                                i+1,j+1]+world[i,j+1]+world[i-1,j+1]+world[i-1,j]
                revelution(T_world, aliveCell, i, j)

def revelution(T_world,aliveCell,i,j):
    if aliveCell == 3:
        T_world[i,j] = 1
    elif aliveCell == 2:
        T_world[i,j]= T_world[i,j]
    elif aliveCell !=2:
        T_world[i,j]=0

def beginCallBack():
    global isrun
    isrun = True



main()
