#!/usr/bin/python3
# feedback_solution.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

class Feedback:

    def __init__(self, master):
        
        master.title('nVision Group Feedback')
        master.resizable(False, False)
        master.configure(background = '#ffffff')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#ffffff')
        #self.style.configure('Content.TFrame', background)
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#ffffff', font = ('TkCaptionFont', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 16, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'nvision_theme.png')
        self.logo = PhotoImage(file=image_path)
        self.logo = self.logo.subsample(5)
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Thanks for Subscribing!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose nVision Group as your partner. "
                          "Please feel free to give us feedback on our services.")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        
        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
        
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
        
        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        
        edt_name = self.entry_name.get()
        edt_email = self.entry_email.get()
        txt_comment = self.text_comments.get(1.0, 'end')

        print(len(edt_name))
        print(len(edt_email))
        print(txt_comment)

        if(len(edt_name)==0 or len(edt_email)==0 or txt_comment=="\n"):
            messagebox.showerror(title="Error", message="Please fill in all the fields.")
        else:
            print('Name: {}'.format(edt_name))
            print('Email: {}'.format(edt_email))
            print('Comments: {}'.format(txt_comment))
            self.clear()
            messagebox.showinfo(title = 'nVision Group Feedback', message = 'Comments Submitted!')
    
    
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
         
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
