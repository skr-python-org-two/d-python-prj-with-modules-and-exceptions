import sys

def main():
    print("### Length of arguments ::: "+str(len(sys.argv)))
    if sys.argv[1] > sys.argv[2] :
        print("arg1 > arg2")
    else:
        print("arg1 < arg2")


if __name__ == "__main__":
    main()

