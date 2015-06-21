# pyLocate
pyLocare is a program written in python to find files(everything in a file in linux) with locate comand only in chosen directories.
The program works on linux. It was written in ubuntu, I think that can works also in other distros.
The program uses the file pyLocate.conf to create the database for the command locate.
The configuration file can be find in $HOME/.config/ .
The invisible file are ignored.

# Installation
There is an installation script, to use it type in the terminal:

	$ ./install

A directory called .pyLocateDir is created in $HOME. All the program file can be found there.
Also the uninstallation script can be found there

# Uninstallation
If you don't like the program go to $HOME/.pyLocateDir and then type in a terminal:

	$ ./uninstall
  
