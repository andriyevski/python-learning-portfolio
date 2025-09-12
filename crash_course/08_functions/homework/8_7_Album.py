# Homework from file tasks/8_7_Album.md
## Task ## : 8.7
# 8_7_Album
from typing import Dict

favorite_music = {}

def make_album(name_artist: str, name_album: str, tracks: str) -> Dict:
    """
    Make dict with favorite music
    - name_artist
    - name_album
    """
    validate_name_artist = validate_data(name_artist)
    validate_album = validate_data(name_album)
    validate_music = validate_data(tracks)

    result_name_artist = check_formatted_data(validate_name_artist)
    result_album = check_formatted_data(validate_album)
    result_music = check_formatted_data(validate_music)

    if result_music not in favorite_music:
        favorite_music.update({result_music:[result_name_artist, result_album]})
        return {
            'status': 'Added',
            'track': result_music,
            'artist': result_name_artist,
            'album': result_album
        }
    else:
        return f"This music: '{result_music} - {result_name_artist} : {result_album}' you are added before!"


def validate_data(data: str) -> str:
    """
    Validate all data to any error!
    """
    data = data.lower()
    if not data or not isinstance(data, str):
        raise ValueError("Error of type data input!")
    else:
        return data

def check_formatted_data(data: str) -> str:
    """
    Formatted data to correct view
    """
    formatted_d = data.title()
    return formatted_d

# Show if we add Music = Name of artist -> Album name -> Name of music
print(make_album('Mikle Jackson','Billie jean','Thriller 40'))
print(make_album('Jack Harlow', 'Sweet Action', 'Whats Poppin'))
print(make_album('mikle jackson', 'hollywood tonight', 'michael'))
print(make_album('mikle jackson', 'hollywood tonight', 'michael'))

# We can test and print with simple UX our Music list
def test_list_music_print(favorite_music):
    print("\n\nFavorite list music:\n")
    print("-"*50)
    for x in favorite_music:
        print(f"\n-{x}")
    print("-"*50)


test_list_music_print(favorite_music)
