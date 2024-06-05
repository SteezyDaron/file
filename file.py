try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("Another line, line 3.\n")
        print("File created successfully.")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Contents of 'my_file.txt':")
        print(content)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("67890\n")
        file.write("Another appended line, line 6.\n")
        print("Content appended successfully.")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied to access the file.")

finally:
    print("Execution completed.")
