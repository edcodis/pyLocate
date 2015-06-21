#!/bin/bash
# The script creates the database in a temporary file.
# The directories are chosen from the configuration file
# ~/.config/pyLocate.conf
# 

settingsFile="$HOME/.config/pyLocate.conf"

dirs=$(cat "$settingsFile")

mkdir /tmp/pyLocate

updatedb -l 0 -o /tmp/pyLocate/databasepyLocate -U $dirs
