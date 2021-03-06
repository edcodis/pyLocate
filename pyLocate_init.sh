#!/bin/bash

# the script generates database for pyLocare, a program thar search files
# only in chosen directories 
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

# The script creates the database in a temporary file.
# The directories are chosen from the configuration file
# ~/.config/pyLocate.conf

settingsFile="$HOME/.config/pyLocate.conf"

dirs=$(cat "$settingsFile")

mkdir /tmp/pyLocate

updatedb -l 0 -o /tmp/pyLocate/databasepyLocate -U $dirs
