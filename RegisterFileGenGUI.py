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
        registerList = ['register0', 'register1']
        registerListVar = tk.StringVar(value=registerList)

        self.list = tk.Listbox(self.frame, listvariable=registerListVar)
        self.list.grid(row=0, column=0, sticky="news")

        self.buttonFrame = ttk.Frame(self.frame)
        self.buttonFrame.grid(row=1,column=0, sticky="news")
        self.buttonFrame.columnconfigure(0,weight=1)
        self.buttonFrame.columnconfigure(1,weight=1)
        self.buttonFrame.rowconfigure(0, weight=1)

        self.addButton = ttk.Button(self.buttonFrame, text="Add Reg")
        self.addButton.grid(row=0,column=0,sticky="news")

        self.delButton = ttk.Button(self.buttonFrame, text="Del Reg")
        self.delButton.grid(row=0,column=1,sticky="news")

        self.selectedRegFrame = ttk.Frame(self.frame)
        self.selectedRegFrame.grid(row=2,column=0, sticky="news")
        self.selectedRegFrame.columnconfigure(0,weight=1)
        self.selectedRegFrame.columnconfigure(1,weight=5)
        self.selectedRegFrame.rowconfigure(0, weight=1)
        self.selectedRegFrame.rowconfigure(1, weight=1)
        self.selectedRegFrame.rowconfigure(2, weight=1)
        self.selectedRegFrame.rowconfigure(3, weight=1)

        self.regNameLabel = ttk.Label(self.selectedRegFrame, text="Name:")
        self.regNameLabel.grid(row=0,column=0,sticky="news")

        self.regDescLabel = ttk.Label(self.selectedRegFrame, text="Description:")
        self.regDescLabel.grid(row=1,column=0,sticky="news")

        self.numBitsLabel = ttk.Label(self.selectedRegFrame, text="Address:")
        self.numBitsLabel.grid(row=2,column=0,sticky="news")

        self.numBitsLabel = ttk.Label(self.selectedRegFrame, text="Num Bits:")
        self.numBitsLabel.grid(row=3,column=0,sticky="news")

        self.name = StringVar()
        self.description = StringVar()
        self.address = StringVar()
        self.numBits = StringVar()

        self.nameEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.name)
        self.nameEntry.grid(row = 0, column=1, sticky="news")

        self.descriptionEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.description)
        self.descriptionEntry.grid(row = 1, column=1, sticky="news")

        self.addressEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.address)
        self.addressEntry.grid(row = 2, column=1, sticky="news")

        self.numBitsEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.numBits)
        self.numBitsEntry.grid(row = 3, column=1, sticky="news")

        # label1 = 
        # label1.grid(row=0,column=0, sticky="news")
        
class FieldsEditor():
    def __init__(self, parent, rowPos, columnPos):
        self.frame = ttk.LabelFrame(parent, text="Fields List")
        self.frame.grid(row=rowPos,column=columnPos, sticky="news")

        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0,weight=1)
        registerList = ['field0', 'field1']
        registerListVar = tk.StringVar(value=registerList)

        self.list = tk.Listbox(self.frame, listvariable=registerListVar)
        self.list.grid(row=0, column=0, sticky="news")

        self.buttonFrame = ttk.Frame(self.frame)
        self.buttonFrame.grid(row=1,column=0, sticky="news")
        self.buttonFrame.columnconfigure(0,weight=1)
        self.buttonFrame.columnconfigure(1,weight=1)
        self.buttonFrame.rowconfigure(0, weight=1)

        self.addButton = ttk.Button(self.buttonFrame, text="Add Field")
        self.addButton.grid(row=0,column=0,sticky="news")

        self.delButton = ttk.Button(self.buttonFrame, text="Del Field")
        self.delButton.grid(row=0,column=1,sticky="news")

        self.selectedRegFrame = ttk.Frame(self.frame)
        self.selectedRegFrame.grid(row=2,column=0, sticky="news")
        self.selectedRegFrame.columnconfigure(0,weight=1)
        self.selectedRegFrame.columnconfigure(1,weight=5)
        self.selectedRegFrame.rowconfigure(0, weight=1)
        self.selectedRegFrame.rowconfigure(1, weight=1)
        self.selectedRegFrame.rowconfigure(2, weight=1)
        self.selectedRegFrame.rowconfigure(3, weight=1)

        self.regNameLabel = ttk.Label(self.selectedRegFrame, text="Name:")
        self.regNameLabel.grid(row=0,column=0,sticky="news")

        self.regDescLabel = ttk.Label(self.selectedRegFrame, text="Description:")
        self.regDescLabel.grid(row=1,column=0,sticky="news")

        self.numBitsLabel = ttk.Label(self.selectedRegFrame, text="Start Bit Num:")
        self.numBitsLabel.grid(row=2,column=0,sticky="news")

        self.numBitsLabel = ttk.Label(self.selectedRegFrame, text="Num Bits:")
        self.numBitsLabel.grid(row=3,column=0,sticky="news")

        self.name = StringVar()
        self.description = StringVar()
        self.startBitNum = StringVar()
        self.numBits = StringVar()

        self.nameEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.name)
        self.nameEntry.grid(row = 0, column=1, sticky="news")

        self.descriptionEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.description)
        self.descriptionEntry.grid(row = 1, column=1, sticky="news")
        
        self.numBitsEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.startBitNum)
        self.numBitsEntry.grid(row = 2, column=1, sticky="news")
        
        self.numBitsEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.numBits)
        self.numBitsEntry.grid(row = 3, column=1, sticky="news")
        

class SettingsEditor():
    def __init__(self, parent, rowPos, columnPos):
        self.frame = ttk.LabelFrame(parent, text="Settings List")
        self.frame.grid(row=rowPos,column=columnPos, sticky="news")

        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0,weight=1)
        registerList = ['setting0', 'setting1']
        registerListVar = tk.StringVar(value=registerList)

        self.list = tk.Listbox(self.frame, listvariable=registerListVar)
        self.list.grid(row=0, column=0, sticky="news")

        self.buttonFrame = ttk.Frame(self.frame)
        self.buttonFrame.grid(row=1,column=0, sticky="news")
        self.buttonFrame.columnconfigure(0,weight=1)
        self.buttonFrame.columnconfigure(1,weight=1)
        self.buttonFrame.rowconfigure(0, weight=1)

        self.addButton = ttk.Button(self.buttonFrame, text="Add Setting")
        self.addButton.grid(row=0,column=0,sticky="news")

        self.delButton = ttk.Button(self.buttonFrame, text="Del Setting")
        self.delButton.grid(row=0,column=1,sticky="news")

        self.selectedRegFrame = ttk.Frame(self.frame)
        self.selectedRegFrame.grid(row=2,column=0, sticky="news")
        self.selectedRegFrame.columnconfigure(0,weight=1)
        self.selectedRegFrame.columnconfigure(1,weight=5)
        self.selectedRegFrame.rowconfigure(0, weight=1)
        self.selectedRegFrame.rowconfigure(1, weight=1)
        self.selectedRegFrame.rowconfigure(2, weight=1)

        self.regNameLabel = ttk.Label(self.selectedRegFrame, text="Name:")
        self.regNameLabel.grid(row=0,column=0,sticky="news")

        self.regDescLabel = ttk.Label(self.selectedRegFrame, text="Description:")
        self.regDescLabel.grid(row=1,column=0,sticky="news")

        self.valueLabel = ttk.Label(self.selectedRegFrame, text="Value:")
        self.valueLabel.grid(row=2,column=0,sticky="news")

        self.name = StringVar()
        self.description = StringVar()
        self.value = StringVar()

        self.nameEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.name)
        self.nameEntry.grid(row = 0, column=1, sticky="news")

        self.descriptionEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.description)
        self.descriptionEntry.grid(row = 1, column=1, sticky="news")
        
        self.valueEntry = ttk.Entry(self.selectedRegFrame, textvariable=self.value)
        self.valueEntry.grid(row = 2, column=1, sticky="news")
        

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








