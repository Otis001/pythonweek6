def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied. Unable to create file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Execution completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Content of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Cannot read.")
    except PermissionError:
        print("Permission denied. Unable to read file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Execution completed.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("98765\n")
            file.write("Appending another line\n")
        print("Content appended to my_file.txt.")
    except FileNotFoundError:
        print("File not found. Cannot append.")
    except PermissionError:
        print("Permission denied. Unable to append to file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()
