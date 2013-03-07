#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import operator
import linecache
from random import randint


dic = { }
lines = []
num_line = 0
maxSize = 21
line_accept = []
alphaCounter = []


myFile = codecs.open("finaltokens.txt", "r", "utf-8")

for line in myFile:
    for i in line:        
        if i not in dic:
            dic[i] = 1
        elif i in dic:
            dic[i] += 1
    num_line += 1

myFile.close()


dic = sorted(dic, key=lambda key: dic[key])
#dic.pop(-1)
dic = dic[0:-1]
dic_1 = dic[:8]
dic_2 = dic[8:]

for i in range(len(dic)):
    alphaCounter.append(0)
    

outFile = codecs.open('outFile.txt', 'w', 'utf-8')
    
def createTrainFile():    
    for cnt in range(6):
        getChoice(dic_1)                    
    for cnt in range(4):
        getChoice(dic_2)           
                        

def getChoice(dictionary):
    for i in dictionary:        
            while(1):
                lineChoice = randint(0, num_line)
                if lineChoice in line_accept:
                    continue            
                choice = linecache.getline("finaltokens.txt", lineChoice)
                choice = unicode(choice, 'utf-8')
                #choice = choice[:-1]
                choice = choice.replace("\n", "")
                if i not in choice:            
                    continue
                elif not checkChoice(choice):
                    addItem(choice, lineChoice)
                    print choice
                    outFile.write(choice+'\n')
                    break 
      
                                   
def checkChoice(choice):
    for i in choice:
        if i in dic_1:
            if alphaCounter[dic.index(i)] > maxSize/3:
                return True
        elif i in dic_2:
            if alphaCounter[dic.index(i)] > maxSize:
                return True
    return False    
    
    
def addItem(choice, num):
    for i in choice:
        alphaCounter[dic.index(i)] += 1
    line_accept.append(num)    


myFile = codecs.open("finaltokens.txt", "r", "utf-8")    
def createNewText():
    outFile = codecs.open('text.txt', 'w', 'utf-8')
    cnt = 0
    for line in myFile:
        cnt += 1
        if cnt not in line_accept:
            outFile.write(line)
                    
    
def main():
    createTrainFile()
    outFile.close()
    createNewText()    
    

if __name__ == '__main__':
    main()

    
    



