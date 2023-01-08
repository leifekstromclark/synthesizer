import random
import math
import stdaudio

def fill_brownian(a, i0, i1, variance, scale):
    im = i0 + (i1 - i0) // 2
    a[im] = 0.5 * (a[i0] + a[i1]) + random.gauss(0, variance ** 0.5)
    if i1 - im > 1:
        a = fill_brownian(a, im, i1, variance / 2 ** (2 * scale), scale)
    if im - i0 > 1:
        a = fill_brownian(a, i0, im, variance / 2 ** (2 * scale), scale)
    return a

wave = []

for i in range(294):
    nb = fill_brownian([0] * 3000, 0, 2999, 0.05, 0.5)
    for k in range(3000):
        t = (i * 3000 + k + 1) / 44100
        s = math.sin(3.14159265359 * 0.25 * t) ** 6
        wave.append((1 - s) * nb[k] + s * random.uniform(-0.25, 0.25))

stdaudio.playSamples(wave)