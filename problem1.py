import random
import stdstats
import stddraw
import sys

def fill_brownian(a, i0, i1, variance, scale):
        im = i0 + (i1 - i0) // 2
        a[im] = 0.5 * (a[i0] + a[i1]) + random.gauss(0, variance ** 0.5)
        if i1 - im > 1:
            a = fill_brownian(a, im, i1, variance / 2 ** (2 * scale), scale)
        if im - i0 > 1:
            a = fill_brownian(a, i0, im, variance / 2 ** (2 * scale), scale)
        return a

if len(sys.argv) >= 2:

    stdstats.plotLines([v + 0.5 for v in fill_brownian([0] * 129, 0, 128, 0.05, float(sys.argv[1]))])

    stddraw.show()

else:
    print('please specify a hurst exponent')