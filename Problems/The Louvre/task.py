class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


pain = Painting(input(), input(), input())
print(f'"{pain.title}" by {pain.artist} ({pain.year}) hangs in the {Painting.museum}.')
