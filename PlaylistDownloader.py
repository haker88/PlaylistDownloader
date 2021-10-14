#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import unicode_literals
import tkinter as tk
import youtube_dl

root= tk.Tk()
root.title('Playlist Downloader')
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():  
    x1 = entry1.get()
    
    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl_opts = {
        'format': 'bestaudio/best',       
        'outtmpl': '%(title)s.%(ext)s',        
        'noplaylist' : False,        
        'progress_hooks': [my_hook],  
        'audiotformat': 'mp3',
        'preferredquality': '320',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([x1])
    
button1 = tk.Button(text='Download playlist', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

