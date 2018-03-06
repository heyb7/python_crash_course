def make_album(singer_name, album_name):
    album_dict = {'singer': singer_name, "album": album_name}

    return album_dict

album = make_album("metallica", "ride the lightning")
print(album)

album = make_album("beethoven", "ninth symphony")
print(album)

album = make_album("willie nelson", "red-headed stranger")
print(album)

print("*" * 50)
print("\n")

def make_album_1(singer_name, album_name, music_num=0):
    if music_num:
        album_dict = {"singer": singer_name, "album": album_name, "music_num": music_num}
    else:
        album_dict = {'singer': singer_name, "album": album_name}

    return album_dict

album = make_album_1("metallica", "ride the lightning")
print(album)

album = make_album_1("beethoven", "ninth symphony", 20)
print(album)