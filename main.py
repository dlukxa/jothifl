import random

class Node:
    def __init__(self, song_name, artist, taste, duration):
        self.song_name  = song_name
        self.artist     = artist
        self.taste      = taste
        self.duration   = duration
        self.next       = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song_name, artist, taste, duration):
        new_song = Node(song_name, artist, taste, duration)

        if self.head is None:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song

        print(f"Added '{song_name}' by {artist} to the playlist.")

    def remove_song(self, song_name):
        if self.head is None:
            print("The playlist is empty.")
            return

        if self.head.song_name == song_name:
            self.head = self.head.next
            print(f"Removed '{song_name}' from the playlist.")
            return

        current = self.head
        prev = None
        while current and current.song_name != song_name:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
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
            songs[i].next = songs[i+1]

        songs[-1].next = None
        print("Playlist shuffled.")

    def display_playlist(self):
        if self.head is None:
            print("The playlist is empty.")
        else:
            current = self.head
            print("Playlist:")
            while current:
                print(f"'{current.song_name}' by {current.artist} [{current.duration}]; Taste {current.taste}")
                current = current.next


# Testing the playlist manager
playlist = Playlist()

# Adding songs to the playlist
playlist.add_song("Song 1", "Artist 1", "POP","3:30")
playlist.add_song("Song 2", "Artist 2", "RAP", "4:15")
playlist.add_song("Song 3", "Artist 3", "HIPHOP", "2:50")

# Displaying the playlist
#playlist.display_playlist()

# Removing a song from the playlist
#playlist.remove_song("Song 2")

# Displaying the updated playlist
playlist.display_playlist()

# Shuffling the playlist
playlist.shuffle_playlist()

# Displaying the shuffled playlist
playlist.display_playlist()
