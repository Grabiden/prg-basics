# class definition
class Song:
    def __init__(self,performer,title,album,year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f"{self.year} {self.title} {self.album} {self.performer}"    
    def lista(self):
        print(f"performer: {self.performer}")
        print(f"title: {self.title}")
        print(f"album: {self.album}")
        print(f"year: {self.year}")

# object creation
def main():
    song1 = Song("Ed Sheeran","Hearts Don't Break Around Here","Divide", 2017)
    song2 = Song("Queen","Bohemian Rhapsody","A Night at the Opera", 1975)
    Song.lista(song1)
    print()
    Song.lista(song2)


main()    
