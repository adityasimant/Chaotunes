import os
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    pygame.mixer.music.load(file_path)

def play_music():
    pygame.mixer.music.play()

def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()


def stop_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

def main():
    root = tk.Tk()
    root.title("Chaotunes")

    root.geometry("900x400")
    root.configure(bg="#f0f0f0")


    pygame.mixer.init()

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)
    style.configure("TLabel", font=("Helvetica", 20), background="#f0f0f0")

    title_label = ttk.Label(root, text="Load the music before playing it :)")
    title_label.pack(pady=10)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)

    load_button = ttk.Button(button_frame, text="Load Music", command=load_music)
    load_button.pack(side=tk.LEFT, padx=10)

    play_button = ttk.Button(button_frame, text="Play", command=play_music)
    play_button.pack(side=tk.LEFT, padx=10)

    pause_button = ttk.Button(button_frame, text="Pause", command=pause_music)
    pause_button.pack(side=tk.LEFT, padx=10)

    

    stop_button = ttk.Button(button_frame, text="Stop", command=stop_music)
    stop_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
