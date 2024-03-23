class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {"sam":0}
    
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.add_to_genre_count(genre)
        Song.add_to_genres(genre)
        Song.add_to_artist_count(artist)
        Song.add_to_artists(artist)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count+=1
        
    @classmethod
    def add_to_genres(cls,genre):
        if not (genre in cls.genres):
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls,artist):
        if not (artist in cls.artists):
            cls.artists.append(artist)
    
    @classmethod
    def add_to_artist_count(cls,artist):
        if not (artist in cls.artists):
            cls.artist_count.update({artist:1})
        else:            
            cls.artist_count[artist] +=1 
            
    @classmethod
    def add_to_genre_count(cls,genre):
        if not (genre in cls.genres):
            cls.genre_count.update({genre:1})
        else:            
            cls.genre_count[genre] +=1 
            


new = Song("title","zip",'...')
new2 = Song("title2","zip",'...')
new4 = Song("title2","zip",'...')
new3 = Song("title2","---",'...')

print(Song.artist_count)
print(Song.artists)

# obj = {"k1":1,"k2":2}

# obj["k3"] =3 

# print(obj)