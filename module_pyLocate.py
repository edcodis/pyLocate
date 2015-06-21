import sys
import re
import os

def printOutputFile(locationInputFile):
    """Open the file in locationFile and
        print the output in an another file.
        The function return the the number of matches"""

    inputFile = open(locationInputFile,'r')

    count = 0
    list = []
    for line in inputFile:
        str_control = re.compile('\S[\][.]\S') # find files only visible
        match_control = str_control.search(line)

        if (match_control):
            count = count + 1
            list.append(line)

    inputFile.close()


    return list
