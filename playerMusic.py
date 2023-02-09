import os
from tkinter import *
from pygame import mixer

# Global Layout

player = Tk()
player.geometry('822x620')
player.title('playerMusic')
bg = PhotoImage(file='Illustration_sans_titre.png')
label1 = Label(player, image=bg)
label1.place(x=0, y=0)
songs = ''


def search_songs():     # Searches the files from the directory list_of_songs
    global songs
    path = 'list_of_songs'
    songs = os.listdir(path)


search_songs()


def play():     # Uses the list from OptionMenu song_choice to load the selected music
    mixer.init()
    mixer.music.load(os.path.join('list_of_songs', song.get()))
    mixer.music.set_volume(0.5)
    mixer.music.play()


def pause():        # Pauses the current music
    mixer.music.pause()


def unpause():      # Unpauses the current music
    mixer.music.unpause()


def stop():     # Stops the music
    mixer.music.stop()


def loop():     # Loop the selected music infinitely
    mixer.music.play(loops=-1)


playlist = list(songs)      # Transforms the files from directory into list for the OptionMenu song_choice
song = StringVar()
song.set(playlist[0])


# Button layout and function


play_button = Button(player, text="Play", bg='black', fg='white', command=lambda: play())
play_button.place(x=260, y=160)

pause_button = Button(player, text="Pause", bg='black', fg='white', command=lambda: pause())
pause_button.place(x=230, y=265)

unpause_button = Button(player, text="Unpause", bg='black', fg='white', command=lambda: unpause())
unpause_button.place(x=220, y=375)

stop_button = Button(player, text="Stop", bg='black', fg='white', command=lambda: stop())
stop_button.place(x=240, y=460)

loop_button = Button(player, text="Loop", bg='black', fg='white', command=lambda: loop())
loop_button.place(x=185, y=570)

volume = Scale(player, from_=100, to=0)
volume.set(50)
volume.configure(bg='black', fg='white')
volume.place(x=730, y=480)

song_choice = OptionMenu(player, song, *playlist)
song_choice.place(x=380, y=520)
song_choice.configure(bg="black", fg="white")


player.mainloop()