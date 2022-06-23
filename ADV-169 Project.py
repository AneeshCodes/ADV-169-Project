from tkinter import *
from tkinter import ttk
import messagebox

root = Tk()
root.geometry("900x600")
root.title("ADV-169 Project")

gui_elements = ["Label","Button","Dropdown"]
dropdown = ttk.Combobox(root, state="readonly", values = gui_elements)
dropdown.pack()

class CreateElements():
    
    def __init__(self):
        print("This is CreateElements Class")
        
    def newLabel(self):
        label = Label(root,text='A new label has been created using class', fg="red")
        label.pack()
        
    def newButton(self):
        button = Button(root,text="Button", command=self.message)
        button.pack(padx=20,pady=10)
    
    def newDropdown(self):
        value = [1,2,3,4]
        newDropdown = ttk.Combobox(root, state="readonly", values = value)
        newDropdown.pack()
        
    def choose(self):
        elements = dropdown.get()
        if(elements=="Label"):
            self.newLabel()
        elif(elements=="Button"):
            self.newButton()
        else:
            self.newDropdown()

    def message(self):
        messagebox.showinfo("showinfo","You clicked the button created using class")
        
obj = CreateElements()
btn = Button(root,text="Click", command=obj.choose)
btn.pack(padx=20,pady=10)

root.mainloop()