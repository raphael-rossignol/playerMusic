import os
from tkinter import *
from pygame import mixer

player = Tk()
player.geometry('480x360')
player.title('playerMusic')
frame = Frame(width=480, height=360, bg='gray60')
frame.grid(row=0, column=0)

play_button = Button(frame, width=30, height=5, text="Play", bg='grey40', fg='white', command=lambda: play())
play_button.grid(row=0, column=0)

pause_button = Button(frame, width=30, height=5, text="Pause", bg='grey40', fg='white', command=lambda: pause())
pause_button.grid(row=1, column=0)

unpause_button = Button(frame, width=30, height=5, text="Unpause", bg='grey40', fg='white', command=lambda: unpause())
unpause_button.grid(row=2, column=0)

stop_button = Button(frame, width=30, height=5, text="Stop", bg='grey40', fg='white', command=lambda: stop())
stop_button.grid(row=3, column=0)
songs = ''


def search_songs():
    global songs
    path = 'list_of_songs'
    songs = os.listdir(path)


search_songs()


playlist = list(songs)
song = StringVar()
song.set(playlist[0])
song_choice = OptionMenu(frame, song, *playlist)
song_choice.place(x=60, y=60)


def play():
    mixer.init()
    mixer.music.load(os.path.join('list_of_songs', song.get()))
    mixer.music.set_volume(0.5)
    mixer.music.play()


def pause():
    mixer.music.pause()


def unpause():
    mixer.music.unpause()


def stop():
    mixer.music.stop()


player.mainloop()