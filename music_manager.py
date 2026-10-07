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