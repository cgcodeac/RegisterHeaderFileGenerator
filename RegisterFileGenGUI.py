import tkinter as tk
from tkinter import StringVar, ttk


class RegisterEditor():
    def __init__(self, parent):

        self.frame = ttk.LabelFrame(parent, text="Register Editor")
        self.frame.grid(row=0,column=0, sticky="news")

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1) 

        self.register = RegisterInfoEditor(self.frame, 0, 0)
        self.fields = FieldsEditor(self.frame, 0, 1)
        self.settings = SettingsEditor(self.frame, 0, 2)   

class RegisterInfoEditor():
    def __init__(self, parent, rowPos, columnPos):
        self.frame = ttk.LabelFrame(parent, text="Register List")
        self.frame.grid(row=rowPos,column=columnPos, sticky="news")

        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0,weight=1)
        registerList = ['hi', 'there']
        registerListVar = tk.StringVar(value=registerList)

        self.list = tk.Listbox(self.frame, listvariable=registerListVar)
        self.list.grid(row=0, column=0, sticky="news")

        self.buttonFrame = ttk.Frame(self.frame)
        self.buttonFrame.grid(row=1,column=0, sticky="news")

        self.addButton = ttk.Button(self.buttonFrame, text="Add Reg")
        self.addButton.grid(row=0,column=0,sticky="news")

        self.delButton = ttk.Button(self.buttonFrame, text="Del Reg")
        self.delButton.grid(row=0,column=1,sticky="news")

        self.selectedRegFrame = ttk.Frame(self.frame)
        self.selectedRegFrame.grid(row=2,column=0, sticky="news")

        self.regNameLabel = ttk.Label(self.selectedRegFrame, text="Name:")
        self.regNameLabel.grid(row=0,column=0,sticky="news")

        self.regDescLabel = ttk.Label(self.selectedRegFrame, text="Description:")
        self.regDescLabel.grid(row=1,column=0,sticky="news")

        # label1 = 
        # label1.grid(row=0,column=0, sticky="news")
        
class FieldsEditor():
    def __init__(self, parent, rowPos, columnPos):
        self.frame = ttk.LabelFrame(parent, text="Register Fields")
        self.frame.grid(row=rowPos,column=columnPos, sticky="news")

        label1 = ttk.Label(self.frame, text="Register Name")
        label1.grid(row=0,column=0, sticky="news")

class SettingsEditor():
    def __init__(self, parent, rowPos, columnPos):
        self.frame = ttk.LabelFrame(parent, text="Field Settings")
        self.frame.grid(row=rowPos,column=columnPos, sticky="news")

        label1 = ttk.Label(self.frame, text="Register Name")
        label1.grid(row=0,column=0, sticky="news")


root = tk.Tk()
root.title("Register Header File Generator")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)




mainFrame = ttk.LabelFrame(root, text='Main Frame')
mainFrame.grid(column=0, row=0, sticky="news")
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)

regEditor = RegisterEditor(mainFrame)




root.mainloop()








