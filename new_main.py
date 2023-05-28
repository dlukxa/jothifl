import random
import os
import pygame
from mutagen.easyid3 import EasyID3
import time


class Node:
    def __init__(self, song_name, artist, taste):
        self.song_name = song_name
        self.artist = artist
        self.taste = taste
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song_name, artist, taste):
        new_song = Node(song_name, artist, taste)

        if self.head is None:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
            new_song.prev = current

        print(f"Added '{song_name}' by {artist} to the playlist.")

    def remove_song(self, song_name):
        if self.head is None:
            print("The playlist is empty.")
            return

        current = self.head
        while current and current.song_name != song_name:
            current = current.next

        if current:
            if current.prev:
                current.prev.next = current.next
            else:
                self.head = current.next

            if current.next:
                current.next.prev = current.prev

            print(f"Removed '{song_name}' from the playlist.")
        else:
            print(f"'{song_name}' is not found in the playlist.")

    def shuffle_playlist(self):
        songs = []
        current = self.head
    
        while current:
            songs.append(current)
            current = current.next

        random.shuffle(songs)
        self.head = songs[0]

        for i in range(len(songs) - 1):
            songs[i].next = songs[i + 1]

        songs[-1].next = None
        print("Playlist shuffled.")
        # Update the current_song attribute to the first song in the shuffled playlist

    def play_song(self):
        if self.head is None:
            print("The playlist is empty.")
            return

        print(f"Now playing: '{self.head.song_name}' by {self.head.artist}")
        # Play the song using the default media player
        pygame.mixer.init()
        pygame.mixer.music.load('songs'+'/'+f"{self.head.song_name[0]}.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            command = input("Enter a command (pause as p, next as n, prev as m): ")

            if command == "p":
                pygame.mixer.music.pause()
                print("Song paused.")
            elif command == "n":
                pygame.mixer.music.stop()
                self.play_next_song()
            elif command == "m":
                pygame.mixer.music.stop()
                self.play_previous_song()
            else:
                # Automatically play the next song
                pygame.mixer.music.stop()
                self.play_next_song()
            # Wait for a short duration before checking for commands again
            time.sleep(0.1)



    def play_next_song(self):
        if self.head is None:
            print("The playlist is empty.")
            return

        if self.head.next:
            self.head = self.head.next
            print(f"Playing next song: '{self.head.song_name}' by {self.head.artist}")
            pygame.mixer.init()
            pygame.mixer.music.load('songs'+'/'+f"{self.head.song_name[0]}.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                command = input("🎵 JothiFl ~ Enter a command (pause as p, next as n, prev as m): ")

                if command == "p":
                    pygame.mixer.music.pause()
                    print("🎵 JothiFl: Song paused.")
                elif command == "n":
                    pygame.mixer.music.stop()
                    self.play_next_song()
                elif command == "m":
                    pygame.mixer.music.stop()
                    self.play_previous_song()
                else:
                    # Automatically play the next song
                    pygame.mixer.music.stop()
                    self.play_next_song()
                # Wait for a short duration before checking for commands again
                time.sleep(0.1)

        else:
            print("🎵 JothiFl ~ End of the playlist.")


    def play_previous_song(self):
        if self.head is None:
            print("🎵 JothiFl ~ The playlist is empty.")
            return

        if self.head.prev:
            self.head = self.head.prev
            print(f"Playing previous song: '{self.head.song_name}' by {self.head.artist}")
            pygame.mixer.init()
            pygame.mixer.music.load('songs'+'/'+f"{self.head.song_name[0]}.mp3")
            pygame.mixer.music.play()
        else:
            print("🎵 JothiFl ~ Beginning of the playlist.")

    def play_song_by_path_num(self, path_num):
        if self.head is None:
            print("The playlist is empty.")
            return

        current = self.head
        for _ in range(path_num - 1):
            if current.next:
                current = current.next
            else:
                print("Invalid path number.")
                return

        print(f"Now playing: '{current.song_name}' by {current.artist}")
        pygame.mixer.init()
        pygame.mixer.music.load('songs'+'/'+f"{current.song_name[0]}.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            command = input("Enter a command (pause as p, next as n, prev as m): ")

            if command == "p":
                pygame.mixer.music.pause()
                print("Song paused.")
            elif command == "n":
                pygame.mixer.music.stop()
                self.play_next_song()
            elif command == "m":
                pygame.mixer.music.stop()
                self.play_previous_song()
            else:
                # Automatically play the next song
                pygame.mixer.music.stop()
                self.play_next_song()
            # Wait for a short duration before checking for commands again
            time.sleep(0.1)


    def display_playlist(self):
        if self.head is None:
            print("🎵 JothiFl ~ The playlist is empty.")
        else:
            current = self.head
            print("Playlist:")
            path_num = 1
            print(current.song_name)
            while current:
                print(f"{path_num}. '{current.song_name}' by {current.artist}; Taste: {current.taste}")
                current = current.next
                path_num += 1


    def add_songs_from_folder(self, folder_path):
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist.")
            return

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and file_path.endswith(".mp3"):
                try:
                    audio = EasyID3(file_path)
                    song_name = audio.get("title", filename)
                    artist    = audio.get("artist", ["Unknown Artist"])[0]
                    taste     = audio.get("genre", ["Unknown Genre"])[0]
                    self.add_song(song_name, artist, taste)
                except Exception as e:
                    print(f"Error occurred while reading file '{filename}': {str(e)}")
            else:
                print(f"Skipping file: '{filename}'")   


# Testing the playlist manager
playlist = Playlist()

# Adding songs from a folder to the playlist
playlist.add_songs_from_folder(r"C:\Users\User\Documents\Karapan\songs")

inp = input("🎵 JothiFl ~ ")

while inp != "q":

    if inp == 'd': 
        # Displaying the playlist
        playlist.display_playlist()
    
    elif inp == 'dele':
        # Removing a song from the playlist        
        print("🎵 JothiFl ~ Tell me the number of the song you want to delete.")
        inp = input("🎵 JothiFl ~ ")
        playlist.remove_song(int(inp))

    elif inp == 'p':
        # Playing the current song
        playlist.play_song()

    elif inp == 'n':
        # Playing the next song
        playlist.play_next_song()

    elif inp == 'r':
        # Playing the previous song
        playlist.play_previous_song()

    elif inp == 's':
        # Shuffling the playlist
        playlist.shuffle_playlist()

    elif inp.isdigit():
        playlist.play_song_by_path_num(int(inp))
    inp = input("🎵 JothiFl ~ ")
