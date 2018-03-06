def make_album_1(singer_name, album_name, music_num=0):
    if music_num:
        album_dict = {"singer": singer_name, "album": album_name, "music_num": music_num}
    else:
        album_dict = {'singer': singer_name, "album": album_name}

    return album_dict

while True:
    print("\nEnter 'q' to end the program....")
    singer = input("singer name: ")
    if singer == 'q':
        break
    
    album = input("album name: ")
    if album == 'q':
        break

    msg = make_album_1(singer, album)
    print(msg)
