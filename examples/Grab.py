#!/usr/bin/env python

# iqt is part of PyQwt
import iqt

def main():
    for demo in ['ParametricSurfaceDemo',
                 'SimplePlot',
                 'TestNumeric',
                 ]:
        result = __import__(demo).make()
        raw_input("Is the demo looking HAPPY? ")
        result.save(demo + '.png', 'PNG')
        result.save(demo + '.pdf', 'PDF')

# main()

if __name__ == '__main__':
    main()

# Local Variables: ***
# mode: python ***
# End: ***
