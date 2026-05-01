

class Song:
    def __init__(self, title, artist, streams):
        self.title = title
        self.artist = artist
        self.streams = streams

    def __str__(self):
        return f"'{self.title}' by {self.artist} has been streamed {self.streams:,} times"

    def update_streams(self, additional_streams):
        self.streams += additional_streams

    def compare_songs(self, other_song):
        if self.streams > other_song.streams:
            print(f"{self.title} is more popular than {other_song.title}")
        elif self.streams < other_song.streams:
            print(f"{other_song.title} is more popular than {self.title}")
        else:
            print(f"{self.title} and {other_song.title} are equally popular")

# __init__ = creates the object data
# __str__ = controls how the object prints
# update_streams() = adds more streams
# compare_songs() = compares two song objects

