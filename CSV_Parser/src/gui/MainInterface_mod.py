#!/usr/bin/python
from Tkinter import Frame, Tk, BOTH, Text, Menu, END, INSERT
import tkFileDialog, tkMessageBox 

from src.parser import Parser_csv_mod
from src.generator import Generator_csv_mod,Generator_dox_mod,Generator_mm_mod 

class MainInterface(Frame):
    
    reqMngr = None
    
    def __init__(self, parent):
        Frame.__init__(self, parent)         
        self.parent = parent        
        self.initUI()
        self.csvParser = Parser_csv_mod.Parser()
        self.csvGenerator = Generator_csv_mod.Generator()
        self.doxGenerator = Generator_dox_mod.Generator()
        self.mmGenerator  = Generator_mm_mod.Generator()
        
    def initUI(self):
      
        self.parent.title("Simple CSV parser GUI")
        self.pack(fill=BOTH, expand=1)
        
        menu = Menu(self.parent)
        self.parent.config(menu=menu)
        
        filemenu = Menu(menu)
        menu.add_cascade(label="File"        , menu=filemenu)
        
        fileOpenMenu = Menu(filemenu)
        filemenu.add_cascade(label="Open..." , menu=fileOpenMenu)
        fileOpenMenu.add_command(label="CSV..." , command=self.open_reqCSVcommand)

        fileSaveMenu = Menu(filemenu)
        filemenu.add_cascade(label="Save..." , menu=fileSaveMenu)
        fileSaveMenu.add_command(label="CSV..." , command=self.save_reqCSVcommand)
        fileSaveMenu.add_command(label="DOX..." , command=self.save_reqDOXcommand)
        fileSaveMenu.add_command(label="MM..."  , command=self.save_reqMMcommand)
        
        filemenu.add_separator()
        filemenu.add_command(label="Exit"    , command=self.exit_command)
        
        helpmenu = Menu(menu)
        menu.add_cascade(label="Help"        , menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about_command)
        # end of menu creation       
        
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def open_reqCSVcommand(self):
        ftypes = [('Requirements CSV files', '*.csv')]
        fileName = tkFileDialog.askopenfilename(filetypes=[("allfiles","*")])
        if len(fileName) > 0:
            self.csvParser.parse(fileName)
            self.txt.insert(END, "Total number of lines parsed: " + str(self.csvParser.getTotalLinesCount()) + '\n')
            self.txt.insert(END, "Total number of Valid lines parsed: " + str(self.csvParser.getTotalValidLinesCount()) + '\n' )
            for i in range(0,self.csvParser.getTotalValidLinesCount()):
                self.txt.insert(END, str(self.csvParser.getLineData(i)) + '\n' )
            
    def save_reqCSVcommand(self):
        ftypes = [('Requirements CSV files', '*.csv')]
        fileName = tkFileDialog.asksaveasfilename(filetypes=[("allfiles","*")])
        if len(fileName) > 0:
            self.csvGenerator.addData(self.csvParser.getData())
            self.csvGenerator.generate(fileName)
            self.txt.insert(END, "Total number of lines generated: " + str(self.csvGenerator.getTotalLinesCount()) + '\n')

    def save_reqDOXcommand(self):
        ftypes = [('Requirements DOX files', '*.dox')]
        fileName = tkFileDialog.asksaveasfilename(filetypes=[("allfiles","*")])
        if len(fileName) > 0:
            self.doxGenerator.addData(self.csvParser.getData())
            self.doxGenerator.generate(fileName)
            self.txt.insert(END, "Total number of lines generated: " + str(self.doxGenerator.getTotalLinesCount()) + '\n')

    def save_reqMMcommand(self):
        ftypes = [('Requirements MM files', '*.mm')]
        fileName = tkFileDialog.asksaveasfilename(filetypes=[("allfiles","*")])
        if len(fileName) > 0:
            self.mmGenerator.addData(self.csvParser.getData())
            self.mmGenerator.generate(fileName)
            self.txt.insert(END, "Total number of lines generated: " + str(self.mmGenerator.getTotalLinesCount()) + '\n')
                     
    def exit_command(self):
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            self.parent.destroy()
     
    def about_command(self):
        label = tkMessageBox.showinfo("About", "Parser project with GUI \n Copyright TOMAR\n No rights reserved")        
