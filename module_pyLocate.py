# module for pyLocate, a program thar search files only in chosen directories 
#  
#    Copyright (C) 2015  Edoardo Codispoti
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.



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
