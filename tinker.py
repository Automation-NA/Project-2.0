from tkinter.filedialog import askopenfile, askopenfilename
from tkinter import Tk
from os import path


class OpenFileDialogBox:
    """
    A class used to create a Open File DialogBox

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """


    def __init__(self, screenname=None):

        self.screenname = screenname


    def window():

        self.ws = Tk(className= self.screenname)
        self.ws.geometry('400x200')
        adhar = Label(
            self.ws, 
            text='Upload the file in excel format '
            )
        adhar.grid(row=0, column=0, padx=10)

        adharbtn = Button(
            self.ws, 
            text ='Choose File', 
            command = lambda:self.open_file()
            ) 
        adharbtn.grid(row=0, column=1)

        time.sleep(10)

        
        #self.read_sheet()
        #self.validate_columns()

        upld = Button(
            self.ws, 
            text='Upload Files', 
            command = lambda: self.uploadFiles()
            )
        upld.grid(row=1, columnspan=3, pady=10)
        

        win = Tk()
