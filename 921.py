# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import tkinter.messagebox as messagebox
window=tk.Tk()
window.title("linyu GUI")
window.geometry('300x300')
def do_job():
    messagebox.showinfo(title='prompt',message='Open File')

label=tk.Label(window,
    text="my Gui",
    bg='black',
    fg='#aaffaa'
    )
label.pack()
menuBar=tk.Menu(window)
filemenu=tk.Menu(menuBar)
filemenu.add_command(label='New',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.destroy)
menuBar.add_cascade(label='File',menu=filemenu)
window.config(menu=menuBar)
def do_select():
    label.config(text=dish.get())
    

dish=tk.StringVar()
dish.set('NULL')
rA=tk.Radiobutton(window,text='soup',variable=dish,value='corn soup',command=do_select)
rA.pack()
rB=tk.Radiobutton(window,text='soup',variable=dish,value='cheese soup',command=do_select)
rB.pack()
                     
window.mainloop()