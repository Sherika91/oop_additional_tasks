"""
Create a class called Album with the following fields:

Artist (artist) - string
Title (title) - string
Tracks (tracks) - lists
Create two instances, album_1 and album_2:

Artist: Queen

Title: Killer Queen

Tracks: Brighton Rock, Killer Queen, Tenement Funster

Artist: Metallica

Title: Black Album

Tracks: Enter Sandman, Sad But True, Holier Than Thou
"""


class Album:

    def __init__(self, artist, title, tracks):
        self.artist = artist
        self.title = title
        self.tracks = tracks


# Create two instances of the Album class
album_1 = Album("Queen", "Killer Queen", ['Brighton rock', 'Killer Queen', 'Tenement Funster'])

album_2 = Album("Metallica", "Black Album", ['Enter Sandman', 'Sad But True', 'Holier Than Thou'])

# Print the artist, title, and number of tracks for each album
print(album_1.artist, album_1.title, len(album_1.tracks), "треков")  # Queen Killer Queen 3 треков
print(album_2.artist, album_2.title, len(album_2.tracks), "треков")  # Metallica Black Album 3 треков
