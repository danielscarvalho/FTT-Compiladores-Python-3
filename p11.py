# node (JavaScript) npm
# Python pip

# pip install PyLyrics

from PyLyrics import *

print(PyLyrics.getLyrics('Taylor Swift','Blank Space')) #Print the lyrics directly

albums = PyLyrics.getAlbums(singer='Eminem')
for a in albums:
    print (a) #Each album printed is a Album Object