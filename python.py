import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete (1.0 , tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt" , filetypes=[("text files ", " *.txt ")])
    if file_path:
        with open (file_path ,'r') as file:
            text.delete (1.0 , tk.END)
            text.insert (tk.END , file.read())

def save_file():
    file_path =  filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files" ,"*.txt")])
    if file_path:
        with open (file_path , "w" ) as file:
            file.write (text.get (1.0 , tk.END))
            messagebox.showinfo("INFO" , "File Save Sussfully ")

root  = tk.Tk()
root.title ("Simple text Editor ")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="NEW", command=new_file)
file_menu.add_command(label="OPEN", command=open_file)
file_menu.add_command(label="SAVE", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="EXIT",command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="black")
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
