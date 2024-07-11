import sys


if __name__ == "__main__" :
    """
        Exception keyword used to raise specific exception
    """
    if len(sys.argv) < 5:
        raise Exception(" Please enter atleast 5 arguments")
    else:
        print("no of arguments given ::: " , len(sys.argv))


