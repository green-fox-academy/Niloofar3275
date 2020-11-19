import sys

def decrypt(file_name):
    try:
        with open(file_name,'r') as f:
            
            content = f.read()
        
        
        for line in reversed(content):
            print(line, end='')
            
            
        

    except IOError as error: 
        print(error)
        print("Error occurred decrypting the file")
        sys.exit()


decrypt("reversed-lines.txt")
