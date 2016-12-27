#!/usr/bin/env python


"""
Since I hate repetition I programmed this script to read the
"Rolling Stone's definitive list of the 500 greatest albums of all time"
you can find here:
http://www.rollingstone.com/music/lists/500-greatest-albums-of-all-time-20120531

This script will output a random line of the 500 album list and append it to a
"listened" file. Continue this until you have listened the complete list.

Music is love.
"""

from random import randint


random_line = randint(1, 500)

with open('500') as music:
    for n, album in enumerate(music):
        if n == random_line:
            break

with open('listened', 'a') as listened:
    listened.write(album)

print(n, album.strip())
