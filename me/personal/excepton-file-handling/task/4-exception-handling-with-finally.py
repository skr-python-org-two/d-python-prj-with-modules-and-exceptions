import sys
from io import BufferedReader


if __name__ == "__main__":
        arg = sys.argv[1]
        f = BufferedReader
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
        finally:
            f.close()


