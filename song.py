class Song:
    count = 0
    genre = []
    artists = []
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()


    @classmethod
    def add_to_genre(cls, genre):
        if cls.genre not in cls.genre:
            cls.genre.append(cls.genre)


    @classmethod
    def add_to_artists(cls, artist):
        if cls.artist not in cls.artists:
            cls.artists.append(cls.artist)


    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre in cls.genre_count:
            cls.genre_count[cls.genre] += 1
        else:
            cls.genre_count[cls.artist] = 1


    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1     


