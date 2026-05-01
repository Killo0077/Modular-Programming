
from class_def import Song


def main():
    song1 = Song("Bohemian Rhapsody", "Queen", 900000)
    song2 = Song("Blinding Lights", "The Weeknd", 1200000)

    print(song1)
    print()
    print(song2)

    song1.update_streams(200000)

    print("\nAfter updating streams: ")
    print(song1)

    print()
    song1.compare_songs(song2)

    songs = [song1, song2]

    print("\nSongs with more than 1,000,000 streams: ")
    for song in songs:
        if song.streams > 1000000:
            print("-",song.title)

main()