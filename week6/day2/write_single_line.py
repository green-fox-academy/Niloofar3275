import sys 
try : 
    with open('my_file.txt' , "r") as file: 
        my_file_content = file.read()    
except FileNotFoundError: 
    print("Unable to write file: my-file.txt")
    sys.exit(2)