import stddraw
import stdaudio
from picture import Picture
from guitarstring import GuitarString

a_string = GuitarString(440.00)
c_string = GuitarString(523.25)

# show a nice background picture
p = Picture('introcs-guitar.png')
stddraw.picture(p)
stddraw.show(0.0)

escape = False
while not escape:
    # check for and process events
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == chr(27):
            escape = True
        elif key == 'a':
            a_string.pluck()
        elif key == 'c':
            c_string.pluck()

    # simulate and play strings
    y = a_string.tick()
    y += c_string.tick()
    stdaudio.playSample(y)