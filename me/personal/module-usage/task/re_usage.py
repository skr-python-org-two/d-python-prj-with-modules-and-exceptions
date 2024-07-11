import sys
import time
import re


def main():

    """"""
    """
        search method
    """
    data = 'GeeksforGeeks: A computer science portal for geeks'
    match = re.search(r'portal', data)
    print('Start Index:', match.start())
    print('End Index:', match.end())




    s = 'geeks.forgeeks'
    # without using \
    match = re.search(r'.', s)
    print(match)
    # using \
    match = re.search(r'\.', s)
    print(match)




    string = "The quick brown fox jumps over the lazy dog"
    pattern = "[a-m]"
    result = re.findall(pattern, string)
    print(result)



    regex = r'^The'
    strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
    for string in strings:
        if re.match(regex, string):
            print(f'Matched: {string}')
        else:
            print(f'Not matched: {string}')



    string = "Hello World!"
    pattern = r"World!$"
    match = re.search(pattern, string)
    if match:
            print("Match found!")
    else:
            print("Match not found.")

    print(match.start() , match.end() , match.group() , match.string)



    """"
        find all method
    """
    string = 'hello 12 hi 89. Howdy 34'
    pattern = '\d+'
    result = re.findall(pattern, string)
    print(result)



    """
        split method
    """
    string = 'Twelve:12 Eighty nine:89.'
    pattern = '\d+'
    result = re.split(pattern, string)
    print(result)


    string = 'Twelve:12 Eighty nine:89.'
    pattern = '\d+'
    # maxsplit = 1
    # split only at the first occurrence
    result = re.split(pattern, string, 1)
    print(result)


    """
        sub and subn methods
    """
    # multiline string
    string = 'abc 12\
    de 23 \n f45 6'
    # matches all whitespace characters
    pattern = '\s+'
    # empty string
    replace = ''
    new_string = re.sub(pattern, replace, string)
    print(new_string)



    # multiline string
    string = 'abc 12\
    de 23 \n f45 6'
    # matches all whitespace characters
    pattern = '\s+'
    replace = ''
    new_string = re.sub(r'\s+', replace, string, 1)
    print(new_string)



    # multiline string
    string = 'abc 12\
    de 23 \n f45 6'
    # matches all whitespace characters
    pattern = '\s+'
    # empty string
    replace = ''
    new_string = re.subn(pattern, replace, string)
    print(new_string)




if __name__ == "__main__":
    main()

