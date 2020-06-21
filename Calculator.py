#Calculator GUI ->

from tkinter import *

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("My Python Calculator!")
    
        #Build Calculator Screen ->
        self.screen = Text(master, state='disabled', width=40, height=8, background="white", foreground="blue")
        self.screen.grid(row=0, column=0, columnspan=4, padx=4, pady=4)
        self.equation = ''
        #Line 1 - Create Screen Widget - Custom Adjust Width, Height and Colors
        #Line 2 - Position the Screen in the Window
        #Line 3 - Set the Screen Value to Empty

        #Build Calculator Buttons ->
        c1 =  self.createButton(7)
        c2 = self.createButton(8)
        c3 = self.createButton(9)
        c4 = self.createButton(u"\u232B",None)
        c5 = self.createButton(4)
        c6 = self.createButton(5)
        c7 = self.createButton(6)
        c8 = self.createButton(u"\u00F7")
        c9 = self.createButton(1)
        c10 = self.createButton(2)
        c11 = self.createButton(3)
        c12 = self.createButton('*')
        c13 = self.createButton('.')
        c14 = self.createButton(0)
        c15 = self.createButton('+')
        c16 = self.createButton('-')
        c17 = self.createButton('=',None,34)
        #Build buttons using createButton method

        buttons = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17]
        #Store all Buttons in a List

        #Build Calculator Counter ->
        count = 0
        #Counter starts at 0
        for row in range(1,5):
            for column in range(4):
                buttons[count].grid(row=row,column=column)
                count += 1
                #Arrange Buttons with Grid Manager
        buttons[16].grid(row=5,column=0,columnspan=4)
        #Arrange the last button "=" at the bottom of the GUI
   
    def createButton(self, val, write=True, width=10):
        return Button(self.master, text=val, command = lambda: self.click(val,write), width=width)
        #This function is used to create a button.

    def click(self,text,write):
        if write == None:
            if text == '=' and self.equation: 
                self.equation= re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == u"\u232B":
                self.clear_screen()
        else:
            self.insert_screen(text)
        #This function handles what happens when you click a button
 
    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)
        #Used to clear the screen - Set to empty before deleting screen.
        
    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        self.equation += str(value)
        self.screen.configure(state ='disabled')
        #Keeps record of every value inserted into the screen.

root = Tk()
my_gui = Calculator(root)
root.mainloop()
