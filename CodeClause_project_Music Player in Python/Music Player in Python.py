import os
from tkinter import *
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, window):
        window.geometry('400x350')
        window.title('Music Player')
        window.resizable(0,0)

        pygame.init()
        pygame.mixer.init()

        # Initializing variables
        self.playlist = []
        self.current = 0

        # Creating UI elements
        self.playlist_box = Listbox(window, bg='#f3f3f3', fg='black', font=('Arial', 12), width=40)
        self.playlist_box.pack(pady=20)

        self.controls_frame = Frame(window)
        self.controls_frame.pack()

        self.play_button = Button(self.controls_frame, text='▶', font=('Arial', 12), command=self.play_music)
        self.play_button.grid(row=0, column=0, padx=10)

        self.pause_button = Button(self.controls_frame, text='❚❚', font=('Arial', 12), command=self.pause_music)
        self.pause_button.grid(row=0, column=1, padx=10)

        
        self.stop_button = Button(self.controls_frame, text='■', font=('Arial', 12), command=self.stop_music)
        self.stop_button.grid(row=0, column=2, padx=10)

        self.add_button = Button(window, text='Add Music', font=('Arial', 12), command=self.add_music)
        self.add_button.pack(pady=10)

    def add_music(self):
        # file dialog to select music files
        files = filedialog.askopenfilenames(title='Select Music', filetypes=(('MP3 Files', '*.mp3'), ('WAV Files', '*.wav')))

        # Adding selected files to playlist
        for file in files:
            self.playlist.append(file)
            filename = os.path.basename(file)
            self.playlist_box.insert(END, filename)

    def play_music(self):
        if pygame.mixer.music.get_busy() == 1:
            # If music is already playing, just unpause it
            pygame.mixer.music.unpause()
        else:
            # Load and play first song in playlist
            pygame.mixer.music.load(self.playlist[self.current])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def run(self):
        mainloop()

if __name__ == '__main__':
    window = Tk()
    music_player = MusicPlayer(window)
    music_player.run()
