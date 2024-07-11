from pathlib import Path


def main():
    print("current working directory ::: ",Path.cwd())
    print("verify whether file or directory is specified ::: ",Path.is_dir(Path("C:\\Users\\ASUS\\Documents\\Learning\\dummy_folder\\abc.txt")))
    print("verify whether file or directory is specified ::: ",Path.is_file(Path("C:\\Users\\ASUS\\Documents\\Learning\\dummy_folder\\abc.txt")))
    print("check for path existense ::: ",Path.exists(Path("C:\\Users\\ASUS\\Documents\\Learning\\dummy_folder\\")))
    print("using read_txt ::: ",Path.read_text(Path("C:\\Users\\ASUS\\Documents\\Learning\\dummy_folder\\abc.txt")))
    p = Path("C:\\Users\\ASUS\\Documents\\Learning\\dummy_folder\\def.txt")
    print("using write_txt ::: ",p.write_text("this is new file"))


if __name__ == "__main__":
    main()

