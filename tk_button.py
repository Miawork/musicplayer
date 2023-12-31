import tkinter as tk
import tkinter.filedialog


#I had planned to replay each song after it was played
#But that performance is so low that it can take hours to load

#import the class from another file
from music_class import Music

class FileGUI:

    def __init__(self):
        #initialize the main window
        self.main_window=tk.Tk()
        self.file=Music()
        self.left_frame=tk.Frame(self.main_window)
        self.right_frame=tk.Frame(self.main_window)
        #create 10 new buttons to promote
        self.playbutton = tk.Button(self.left_frame,text='-Play-',
                                        command=self.file.play_music,
                                        width=8,height=2)
        self.playbutton.pack()
        self.pausebutton = tk.Button(self.left_frame,text='-Pause-',
                                         command=self.file.pause_music,
                                         width=8,height=2)
        self.pausebutton.pack()
        self.stopbutton = tk.Button(self.left_frame,text='-Stop-',
                                         command=self.file.stop_music,
                                         width=8,height=2)
        self.stopbutton.pack()
        #back to last one
        self.previousbutton = tk.Button(self.left_frame,text='-Previous-',
                                         command=self.file.previous_music,
                                         width=8,height=2)
        self.previousbutton.pack()
        #display the next song
        self.nextbutton = tk.Button(self.left_frame,text='-Next-',
                                         command=self.file.next_music,
                                         width=8,height=2)
        self.nextbutton.pack()
        self.lyricbutton = tk.Button(self.left_frame,text='-Lyric-',
                                         command=self.read_lyric,
                                         width=8,height=2)
        self.lyricbutton.pack()
        #press the playlist button to see the play list
        self.listbutton = tk.Button(self.left_frame,text='-PlayList-',
                                         command=self.file.get_playlist,
                                         width=8,height=2)
        self.listbutton.pack()
        #three mode to display songs
        self.mode1button = tk.Button(self.right_frame, text='-List Loop-',
                                         command=self.file.listtoloop_music,
                                         width=8,height=2)
        self.mode1button.pack()
        self.mode2button = tk.Button(self.right_frame, text='-Single Loop-',
                                         command=self.file.singletoloop_music,
                                         width=8,height=2)
        self.mode2button.pack()
        self.mode3button = tk.Button(self.right_frame, text='-Random-',
                                         command=self.file.playatrandom_music,
                                         width=8,height=2)
        self.mode3button.pack()
        #create the text frame to open the lyric file
        self.center_frame=tk.Frame(self.main_window) 
        self.scrollbar = tk.Scrollbar(self.center_frame)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.text=tk.Text(self.center_frame, yscrollcommand = self.scrollbar.set)
        self.text.pack(side=tk.LEFT)
        self.scrollbar.config(command=self.text.yview)
        self.left_frame.pack(side=tk.LEFT)
        self.center_frame.pack(side=tk.LEFT)
        self.right_frame.pack(side=tk.LEFT)
        tk.mainloop()

    def read_lyric(self):
        #load the lyric file
        self.file.set_filename(tk.filedialog.askopenfilename())
        self.file.read_file()
        self.text.delete('1.0',tk.END)
        self.text.insert(tk.INSERT,self.file.get_lyric())

#call the main function
Music()
FileGUI()
