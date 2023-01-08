import stddraw
import stdaudio
from picture import Picture
from guitarstring import GuitarString

p = Picture('keyboard.png')
stddraw.setCanvasSize(624, 214)
stddraw.picture(p)
stddraw.show(0.0)

keys = ['q', '2', 'w', 'e', '4', 'r', '5', 't', 'y', '7', 'u', '8', 'i', '9', 'o', 'p', '-', '[', '=', 'z', 'x', 'd', 'c', 'f', 'v', 'g', 'b', 'n', 'j', 'm', 'k', ',', '.', ';', '/', "'", ' ']
strings = []
for i in range(len(keys)):
    strings.append(GuitarString(110 * 2 ** (i/12)))

escape = False
while not escape:
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == chr(27):
            escape = True
        elif key in keys:
            strings[keys.index(key)].pluck()

    y = 0

    for string in strings:
        y += string.tick()
    
    stdaudio.playSample(y)