import os
import traceback

def generate_song_list():
    if not os.path.exists('data/Music'):
        print('No data/Music directory found')
        return False

    songs = os.walk('data/Music')

    song_list = ""

    for root, dirs, files in songs:
        level = root.replace('data/Music', '').count(os.sep)
        indent = ' ' * 4 * (level)
        song_list += '{}- {}\r\n'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if '.meta' not in f:
                continue
            song_list += '{} key: {}\r\n'.format(subindent, song_name_from(root, f))

    try:
        create_song_list_file(song_list)
    except Exception as e:
        print("An error occured creating song list")
        print(traceback.format_exc())
        return False

    return True

def create_song_list_file(song_list):
    with open('song_list.txt', 'w', encoding='utf-8') as song_list_file:
        song_list_file.write(song_list)

def song_name_from(root, file):
    path = root + "/" + file
    with open(path, 'r') as meta_file:
        return meta_file.readline().rstrip()


if __name__ == '__main__':
    song_list_generated = generate_song_list()
    
    if song_list_generated:
        print("song_list.txt file successfully created!")
        print("Have fun customizing your randomizer! :)")
        print("")
    else:
        print("An error occured generating your song list")
    input("Press enter to quit")

