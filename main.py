# main.py
"""Simple Image Viewer Plugin for displaying .bin formatted picture

This is a plugin application which also can work as standalone program
Copyright 2020 Nur Mahmud Ul Alam Tasin

INSTALLATION: Put this file somewhere where Python can see it.
WARNING: THIS PROGRAM IS NOT OPTIMIZED AT ALL
"""
import tkinter
from graphics import *
optimization=3
def plotImage(path):
    with open(path,mode="rb") as file:
        ImgMap=file.read()
        height=(ImgMap[1]<<8)|ImgMap[0]
        width=(ImgMap[3]<<8)|ImgMap[2]
        ImgMap=ImgMap[4:]
        
        subWin=GraphWin(path+" |Bin Viewer",width,height)
        #print(ImgMap[0],ImgMap[1],ImgMap[2])
        for y in range(height):
            for x in range(width):
                #print(len(ImgMap))
                if ImgMap[3]!=0 and not (((ImgMap[0],ImgMap[1],ImgMap[2])>(200,200,200))if optimization>2 else True):
                	subWin.plot(x,y,color=color_rgb(ImgMap[0],ImgMap[1],ImgMap[2]))
                ImgMap=ImgMap[4:]
        print(len(ImgMap))
        return subWin
if __name__=="__main__":
    from sys import argv
    from time import time
    start=time()
    win=plotImage("mkbhdFullOptimized.bin")
    end=time()
    with open("LastLog.txt","w+")as f:
    	f.write(str(end-start))
    win.getMouse()
