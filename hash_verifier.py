import hashlib
import tkinter as tk
from tkinter import filedialog

def Open_file():
    # create a root window (it will be hidden)
    root = tk.Tk()
    root.withdraw() # hide the root window
    global file_path
    # OPen the file dialog and store file path
    file_path = filedialog.askopenfilename(
        title = "Select a file",
        filetypes = (("text files","*.txt"), ("All Files", "*.*"))
        )
    if file_path:
        print(f"file Selected: {file_path}")
        return True
    else:
        print("no file selected.")
    
    
def hashit():
    userinput = input("which algorithm do you want? \n type 256 for sha256 and 5 for md5")
    if userinput == '256':
        hashfile = file_path
        h = hashlib.sha256()
        h.update(hashfile.encode())
        filehash = h.hexdigest()
        print(f"here's the hash: {filehash}")
    elif userinput == '5':
        hashfile = file_path
        h = hashlib.md5()
        h.update(hashfile.encode())        
        filehash = h.hexdigest()
        print(f"here's the hash: {filehash}")
    
    
    
   

Open_file()
hashit()