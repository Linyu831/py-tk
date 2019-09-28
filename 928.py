# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
window.iconbitmap("ball_128px_1226110_easyicon.ico")
window.maxsize(600,400)
from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=q68hRJbuqtc")
stream=yt.streams.filter(res="720p",fps=30).first()
stream.download("C:Users\\Administrator\\.spyder-py3","video")



window.mainloop()