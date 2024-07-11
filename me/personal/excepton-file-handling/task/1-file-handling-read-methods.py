import sys

def main():

    """
        Using forr method to read files
    """
    # a file named "geek", will be opened with the reading mode.
    file = open('../src/data/geek.txt', 'r')
    # This will print every line one by one in the file
    for each in file:
        print(each)
    file.close()



    # a file named "geek", will be opened with the reading mode.
    file = open('../src/data/geek.txt', 'r')
    print (file.read())



    # Python code to illustrate with()
    with open("../src/data/geek.txt") as file:
        data = file.read()
    print(data)




    # Python code to illustrate read() mode character wise
    file = open("../src/data/geek.txt", "r")
    print(file.read(5))




    # Python code to illustrate split() function
    with open("../src/data/geek.txt", "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split()
            print (word)



if __name__ == "__main__":
    main()

