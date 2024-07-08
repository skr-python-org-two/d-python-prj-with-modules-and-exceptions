import sys


if __name__ == "__main__":
        arg = sys.argv[2]
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        except Exception as e:
            print(" Generic Exception ",e)

        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()


