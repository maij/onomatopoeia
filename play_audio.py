#/usr/bin/env python2.7

from glob import glob
import pyglet
from time import sleep
import pyglet.media as media

player = media.Player()
player.volume=1.0    

for file in glob('./ogg_files/*.ogg'):
    song = pyglet.media.load(file)
    player.queue(song)

#song = media.load('mpthreetest.mp3')
#player.queue(song)
#song = media.load('mpthreetest.ogg')
#player.queue(song)
player.play()
pyglet.app.run()
while True:
    player.next()

