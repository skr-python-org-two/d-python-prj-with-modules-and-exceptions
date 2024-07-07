import sys
import time

def main():
    print("### Length of arguments ::: "+str(len(sys.argv)))
    age =  int(sys.argv[1])
    for i in sys.argv:
        print(i)

    print("### List of modules::: ")
    print(sys.modules)
    for i in sys.modules:
        print(i)

    print("### List of modules::: ")
    print(sys.path)
    for i in sys.path:
        print(i)

    print("### usage of exit::: ")
    if age < 18:
        #sys.exit("Age less than 18")
        #sys.exit(1)
        pass
    else:
        print("Age is not less than 18")


    print("### usage of stdout::: ")
    sys.stdout.write('Geeks \n')

    print("### usage of stderr::: ")
    def print_to_stderr(*a):
        print(*a, file=sys.stdout)
        time.sleep(60)
        print(*a, file=sys.stderr)

    print_to_stderr("Hello World")

print("### usage of stdin is to read interactively from stdin or ui::: ")
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')


if __name__ == "__main__":
    main()

