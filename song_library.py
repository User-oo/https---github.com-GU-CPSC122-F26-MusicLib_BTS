class Song:
    MIN_RATING = 1
    MAX_RATING = 5

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