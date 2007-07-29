#!/usr/bin/env python

# iqt is part of PyQwt
import PyQt4.Qwt5.iqt
from PyQt4.Qwt3D import save


def main():
    for demo in ['EnrichmentDemo',
                 'ParametricSurfaceDemo',
                 'SimplePlot',
                 'TestNumPy',
                 ]:
        result = __import__(demo).make()
        raw_input("Is the demo looking HAPPY? ")

        print save(result, demo + '.png', 'png')
        print save(result, demo + '.pdf', 'pdf')
	print save(result, demo + '.ps', 'pdf')
	print save(result, demo + '.eps', 'eps')
        print save(result, demo + '.svg', 'svg')

# main()

if __name__ == '__main__':
    main()

# Local Variables: ***
# mode: python ***
# End: ***
