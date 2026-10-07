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