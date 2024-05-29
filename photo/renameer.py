import os
import shutil

def get_files():
    return os.listdir()

def reader():
    i = 1
    for file in get_files():
        if file.endswith('.jpeg'):
            new_name = f"IMG_{str(i).zfill(2)}.jpeg"
            shutil.move(file, new_name)   
            i += 1
            print(f'old_name: {file}, new_name: {new_name}')
        
        
if __name__ == '__main__':
    reader()