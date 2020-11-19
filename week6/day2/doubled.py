import sys

def decrypt(file_name):
    try:
        with open(file_name,'r') as f:
            
            content = f.read()
        

            new_lines = ""
            for char in range(len(content)):
                if char % 2!= 0:
                    new_lines += content[char]
            print(new_lines)
        return True

        


    except IOError as error: 
        print(error)
        print("Error occurred decrypting the file")
        sys.exit()


decrypt("duplicated_chars.txt")



  
