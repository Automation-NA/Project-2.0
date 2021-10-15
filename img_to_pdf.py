import os
from os import path
import easygui
from PIL import Image

def img_to_pdf(args):
    print(args)
    img_file = [Image.open(filepath) for filepath in args]
    img_obj = [img.convert('RGB') for img in img_file]
    img_obj[0].save(r'C:\Users\Naveen\Documents\Project 2.0\output\final_pdf.pdf',
                    save_all=True, append_images=img_obj[1:])

    

if __name__ == '__main__':
    #input_path = easygui.fileopenbox()
    print("Enter image file paths. Press X to Exit")
    list_path=[]
    while True:
        filepath = input()
        if filepath.upper() != 'X':
            list_path.append(filepath)
        else:
            break
    
    img_to_pdf(list_path)
