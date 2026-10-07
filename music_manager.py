from song_library import Song, SongLibrary


library = SongLibrary()

print("Before adding songs:")
print(library)

# Add two songs
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

print("\nUpdated Blinding Lights song:")
found_song = library.perform_search("title", "Blinding Lights")

if found_song is not None:
    index = library.get_song_index(found_song)
    library.perform_update_song(index, "rating", "4")
    library.perform_update_song(index, "genre", "Synthwave")
else:
    print("Song not found.")

print(library)

sort_library = SongLibrary()

sort_library.perform_add_song(
    Song("Smooth", "Santana", "Rock", "", 4)
)
sort_library.perform_add_song(
    Song("Blinding Lights", "The Weeknd", "Pop", "", 5)
)
sort_library.perform_add_song(
    Song("Levitating", "Dua Lipa", "Pop", "", 3)
)

print("\nBefore sorting:")
print(sort_library)

sort_library.perform_sort("title")

print("\nAfter sorting:")
print(sort_library)

print("\nSaving the sorted library:")
sort_library.perform_save("test_library.txt")
print("Library saved to test_library.txt")

print("\nLoading the saved library:")
loaded_library = SongLibrary()
loaded_library.perform_load("test_library.txt")
print(loaded_library)

audio_song = Song("Blood sweat & Tears", "BTS", "K-Pop", r"clips\Blood Sweat & Tears - BTS - KPop.mp3", 5)

print("\nPlaying audio clip")
audio_song.play_clip()