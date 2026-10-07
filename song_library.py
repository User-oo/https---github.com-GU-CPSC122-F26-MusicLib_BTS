class Song:
    MIN_RATING = 1
    MAX_RATING = 5
    SORT_ATTRIBUTE = "title"

    def __init__(self, title_param: str = "", artist_param: str = "", genre_param: str = "", clip_param: str = "", rating_param: int = 1) -> None:
        self._title = title_param.lower()
        self._artist = artist_param.lower()
        self._genre = genre_param.lower()
        self._clip = clip_param
        self.set_rating(rating_param)

    def set_rating(self, rating_param: int) -> None:
        if rating_param < Song.MIN_RATING:
            self._rating = Song.MIN_RATING
        elif rating_param > Song.MAX_RATING:
            self._rating = Song.MAX_RATING
        else:
            self._rating = rating_param

    def __str__(self) -> str:
        return (
            f"Title: {self._title}\n"
            f"Artist: {self._artist}\n"
            f"Genre: {self._genre}\n"
            f"Clip: {self._clip}\n"
            f"Rating: {self._rating}"
        )
    def get_attribute_string_value(self, attribute: str) -> str:
        if attribute == "title":
            return self._title
        elif attribute == "artist":
            return self._artist
        elif attribute == "genre":
            return self._genre
        elif attribute == "rating":
            return str(self._rating)
        else:
            return ""

    def set_attribute_value(self, attribute: str, new_attribute_value: str) -> None:
        if attribute == "title":
            self._title = new_attribute_value.lower()
        elif attribute == "artist":
            self._artist = new_attribute_value.lower()
        elif attribute == "genre":
            self._genre = new_attribute_value.lower()
        elif attribute == "clip":
            self._clip = new_attribute_value
        elif attribute == "rating":
            self.set_rating(int(new_attribute_value))

    def __lt__(self, other: "Song") -> bool:
        return self._title < other._title

class SongLibrary:
    def __init__(self) -> None:
        self._songs = []

    def perform_add_song(self, new_song: Song) -> None:
        self._songs.append(new_song)

    def __str__(self) -> str:
        if not self._songs:
            return "The library is empty."

        result = ""
        for index, song in enumerate(self._songs):
            result += f"Song index {index}:\n{song}\n\n"

        return result.rstrip()

    def perform_search(self, search_attribute: str, search_attribute_value: str) -> Song | None:
        search_attribute = search_attribute.lower()

        if search_attribute == "index":
            try:
                index = int(search_attribute_value)
            except ValueError:
                return None

            if 0 <= index < len(self._songs):
                return self._songs[index]

            return None

        if search_attribute not in ("title", "artist", "genre", "rating"):
            return None

        for song in self._songs:
            value = song.get_attribute_string_value(search_attribute)

            if value == search_attribute_value.lower():
                return song

        return None

    def get_song_index(self, song: Song) -> int:
        for index, current_song in enumerate(self._songs):
            if current_song is song:
                return index

        return -1

    def perform_remove_song(self, index_to_remove: int) -> None:
        if 0 <= index_to_remove < len(self._songs):
            self._songs.pop(index_to_remove)

    def perform_update_song(self, index_to_update: int, attribute_to_update: str, new_attribute_value: str) -> None:
        if 0 <= index_to_update < len(self._songs):
            song_to_update = self._songs[index_to_update]
            song_to_update.set_attribute_value(attribute_to_update, new_attribute_value)

    def perform_sort(self, attribute: str) -> None:
        Song.SORT_ATTRIBUTE = attribute
        self._songs.sort()

    def perform_save(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            for song in self._songs:
                file.write(f"{song.get_attribute_string_value('title')}\n")
                file.write(f"{song.get_attribute_string_value('artist')}\n")
                file.write(f"{song.get_attribute_string_value('genre')}\n")
                file.write(f"{song.get_attribute_string_value('clip')}\n")
                file.write(f"{song.get_attribute_string_value('rating')}\n")
                file.write("\n")  