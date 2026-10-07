from song_library import Song, SongLibrary


def display_menu() -> None:
    print("\n--- Music Library Manager ---")
    print("1. Display library")
    print("2. Load library")
    print("3. Store library")
    print("4. Sort library")
    print("5. Search library")
    print("6. Play song clip")
    print("7. Add song")
    print("8. Remove song")
    print("9. Update song")
    print("10. Quit")


def find_song(library: SongLibrary) -> Song | None:
    attribute = input(
        "Search by title, artist, genre, rating, or index: "
    ).strip().lower()

    if attribute not in ("title", "artist", "genre", "rating", "index"):
        print("Invalid search field.")
        return None

    value = input("Enter the search value: ").strip()
    song = library.perform_search(attribute, value)

    if song is None:
        print("Song not found.")

    return song

def get_rating() -> int:
    while True:
        try:
            rating = int(input("Rating (1-5): "))

            if Song.MIN_RATING <= rating <= Song.MAX_RATING:
                return rating

            print("Please enter a rating from 1 to 5.")
        except ValueError:
            print("Please enter a whole number.")


def add_song(library: SongLibrary) -> None:
    title = input("Title: ").strip()
    artist = input("Artist: ").strip()
    genre = input("Genre: ").strip()
    clip = input("Clip path (Enter for none): ").strip()
    rating = get_rating()

    song = Song(title, artist, genre, clip, rating)
    library.perform_add_song(song)

    print("Song added.")


def update_song(library: SongLibrary) -> None:
    song = find_song(library)

    if song is None:
        return

    print("\nSelected song:")
    print(song)

    attribute = input(
        "Attribute to edit (title, artist, genre, clip, rating): "
    ).strip().lower()

    if attribute not in ("title", "artist", "genre", "clip", "rating"):
        print("Invalid attribute.")
        return

    if attribute == "rating":
        new_value = str(get_rating())
    else:
        new_value = input("New value: ").strip()

    index = library.get_song_index(song)
    library.perform_edit_song(index, attribute, new_value)

    print("\nUpdated song:")
    print(song)

def main() -> None:
    library = SongLibrary()

    while True:
        display_menu()
        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            print(library)

        elif choice == "2":
            filename = input("File to load: ").strip()

            try:
                library.perform_load(filename)
                print("Library loaded.")
            except OSError as error:
                print(f"Could not read the file: {error}")
            except ValueError:
                print("Invalid file data. Some songs may have loaded.")

        elif choice == "3":
            filename = input("File to save to: ").strip()

            try:
                library.perform_save(filename)
                print("Library saved.")
            except OSError as error:
                print(f"Could not save the file: {error}")

        elif choice == "4":
            library.perform_sort("title")
            print("Library sorted by title.")

        elif choice == "5":
            song = find_song(library)

            if song is not None:
                print(song)

        elif choice == "6":
            song = find_song(library)

            if song is not None:
                song.play_clip()

        elif choice == "7":
            add_song(library)

        elif choice == "8":
            song = find_song(library)

            if song is not None:
                index = library.get_song_index(song)
                library.perform_remove_song(index)
                print("Song removed.")

        elif choice == "9":
            update_song(library)

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Please enter a number from 1 to 10.")


if __name__ == "__main__":
    main()