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

        elif choice in ("7", "8", "9"):
            print("We will connect this option next.")

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Please enter a number from 1 to 10.")


if __name__ == "__main__":
    main()