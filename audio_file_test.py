#!/usr/bin/env python2.7

import sys
import os
import IPA_primitives as IPA

#print IPA.pulmonic_consonants
#print IPA.vowels

for key in IPA.pulmonic_consonants.keys():
    #print audio_path + key[1] + '_' + key[2] + '.ogg'
    audio_path = IPA.pulmonic_consonants[key,1]
    if (os.path.isfile(audio_path)):
        print key[1] + '_' + key[2]
    else:
    	print "Not found: {file}".format(file = audio_path)

for key in IPA.vowels.keys():
    audio_path = IPA.vowels[key,1]
    #print audio_path + key[0] + '_' + key[1] + '.ogg'
    if (os.path.isfile(audio_path)):
        print key[0] + '_' + key[1]
    #print IPA.pulmonic_consonants[key]
#for i in range(0x0000, 0xFFFF+1):
    #print u'\u{:04x}'.format(str(i).decode('utf-8'))
    # .encode('utf-8')

sys.stdin.readline()
