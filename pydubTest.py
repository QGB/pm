# coding=utf-8
from qgb import U,T,Clipboard

##U.write(sf,'ddddd')

# sf='c:\\users\\qgb\\appdata\\local\\temp\\tmpworpnk.wav'
# print sf[-13:]
# open(r'c:\users\qgb\appdata\local\temp\tmpls79ml.wav','w')
# exit()
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("a.mp3")
backwards = song.reverse()
play(backwards)
# U.write('rd.dub',backwards.raw_data)