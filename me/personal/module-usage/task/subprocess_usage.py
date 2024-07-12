import subprocess
import sys

def main():

    """"""
    """
        call method
    """
    print("\n \n  ###############    using call method ###############    \n \n")
    res = subprocess.call(['ls', '-l'], shell=True)  # using the call() function
    print(res)
    res = subprocess.call([sys.executable, 'print("hello world")'], shell=True)  # using the call() function
    print(res)
    res = subprocess.call(["echo", 'hello world'], shell=True)  # using the call() function
    print(res)



    """
        run method
    """
    print("\n \n  ###############    using run method   ###############    \n \n")
    res = subprocess.run(['ls', "-l"], shell=True , capture_output=True)  # using the run() function
    print("returncode ::: " , res.returncode )
    print("args ::: " , res.args)
    print("stdout ::: " , res.stdout)
    print("stderr ::: " , res.stderr)
    #print("check_returncode ::: " , res.check_returncode())

    res = subprocess.run([sys.executable, '2+3'], shell=True , capture_output=True)  # using the run() function
    print("returncode ::: " , res.returncode )
    print("args ::: " , res.args)
    print("stdout ::: " , res.stdout)
    print("stderr ::: " , res.stderr)
    #print("check_returncode ::: " , res.check_returncode())

    res = subprocess.run(["echo", "hello how are you from run() method"], shell=True, capture_output=True)  # using the run() function
    print("returncode ::: " , res.returncode )
    print("args ::: " , res.args)
    print("stdout ::: " , res.stdout)
    print("stderr ::: " , res.stderr)
    print("check_returncode ::: " , res.check_returncode())



    """ 
        check_call method
    """
    print("\n \n  ###############"
          "    using check_call() method   ###############    \n \n")
    res = subprocess.check_call(["echo", "hello how are you from check_call() method"], shell=True)  # using the check_call() function
    print("returncode ::: " , res)


    """
        check_output method
    """
    print("\n \n  ###############    using check_output() method   ###############    \n \n")
    res = subprocess.check_output(["echo", "hello how are you from check_output() method"], shell=True)  # using the check_output() function
    print("returncode ::: " , res)



if __name__ == "__main__":
    main()

