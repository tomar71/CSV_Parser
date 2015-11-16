'''
Created on 2015-11-01

@author: tomar
'''

from Tkinter import Tk
from src.gui import MainInterface_mod

def main():
  
    root = Tk()
    MainInterface_mod.MainInterface(root)
    root.geometry("1024x768+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()