#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import operator

dic = { }

myFile = codecs.open( "outFile.txt", "r", "utf-8")

for line in myFile:
    for i in line:        
        if i not in dic:
            dic[i] = 1
        elif i in dic:
            dic[i] += 1

for i, j in sorted(dic.items(), key=operator.itemgetter(1)):
    print i, j

