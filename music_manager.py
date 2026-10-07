from song_library import Song, SongLibrary

library = SongLibrary()

print("Before adding songs:")
print(library)

song1 = Song("Blinding Lights", "The Weeknd", "Pop", "", 5)
song2 = Song("Levitating", "Dua Lipa", "Pop", "", 3)

library.perform_add_song(song1)
library.perform_add_song(song2)

print("\nAfter adding songs:")
print(library)

print("\nSearch by artist:")
found_song = library.perform_search("artist", "Dua Lipa")

if found_song is not None:
    print(found_song)
else:
    print("Song not found.")

print("\nSearch for a missing title:")
found_song = library.perform_search("title", "Missing Song")

if found_song is not None:
    print(found_song)
else:
    print("Song not found.")

print("\nSearch by index:")
found_song = library.perform_search("index", "0")

if found_song is not None:
    print(found_song)
else:
    print("Song not found.")

print("\nSong index check:")
print(library.get_song_index(song1))  
print(library.get_song_index(song2))

another_song = Song("Blinding Lights", "The Weeknd", "Pop", "", 5)
print(library.get_song_index(another_song))

print("\nRemoving Dua Lipa's song:")

found_song = library.perform_search("artist", "Dua Lipa")

if found_song is not None:
    index = library.get_song_index(found_song)
    library.perform_remove_song(index)

else:
    print("Song not found.")

print(library)