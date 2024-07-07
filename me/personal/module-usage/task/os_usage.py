import os
import time

def main():
    print("Base path is ::: ",os.path)
    location = """C:\\Users\\ASUS\\Documents\\Learning\\PythonLearning"""
    print("New Path is ::: " , os.path.join(location))

    print("current working directory ::: ",(os.getcwd()))
    os.environ["sample_var"] = "hello"
    print("accessing environment variables ::: ",os.getenv("sample_var"))
    current_dir = os.getcwd()
    print("get current working directory ::: ", os.getcwd())
    print("create directory in cwd  ::: ", os.mkdir(f"{current_dir}/dummy"))
    print("list files in directory ::: ",os.listdir(os.getcwd()))
    print("remove directory  ::: ",os.rmdir(f"{current_dir}/dummy"))
    print("get process_id  ::: ",os.getpid())
    print("get os name ::: ",os.name)
    print("Size of the file is ::: ", os.path.getsize(f"{current_dir}/os_usage.py") , " bytes.")
    print("directory name in given path ::: ", os.path.dirname(f"C:\\Users\\ASUS\\Documents\\Learning\\PythonLearning\\PythonConcepts.txt"))
    print("filename name in given path ::: ", os.path.basename(f"C:\\Users\\ASUS\\Documents\\Learning\\PythonLearning\\PythonConcepts.txt"))

    #os.system("date")
    os.system("notepad")
    os.system("pip install numpy")


    os.chdir(f"os.getcwd()/../../../../../../..")
    print(os.getcwd())


if __name__ == "__main__":
    main()

