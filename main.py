import PIL.Image
from pathlib import Path
import os

delete=False


while (True):
    print("Do you want the files you want to convert to be deleted? Y/n : ",end="")
    a = input()
    if (a=="Y" or a=="y"):
        delete=True
        print("The converted files will be deleted.")
        break
    elif(a=="N" or a=="n"):
        delete =False
        print("The converted files will not be deleted.")
        break
    else:
        print("Sorry, that wasn't Y or N. Try again.")

from tkinter import filedialog
from tkinter import *
print("Select a Folder...")

root = Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)
PATH = filedialog.askdirectory(title="Select a Folder")

def convert_to_webp(source):
    
    destination = source.with_suffix(".webp")
    image = PIL.Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp
    return destination

def main():
    i=1
    extensions = ('*.jpg', '*.jpeg', '*.png')

    files_list=[]
    for ext in extensions:
        files_list.extend(Path(PATH).glob(ext))
    
    if(files_list!=[]):
        for path in files_list:
            print(str(i)+" -- ",end="")
            print(path)
            convert_to_webp(path)
            if (delete):
                os.remove(path)
            i+=1
        print("The files converted.")
    else:
        print("Can't find any images on the folder.")
         
main()
input()