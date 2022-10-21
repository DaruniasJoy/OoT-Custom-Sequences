import os

def generate_song_list():
    songs = os.walk('data/Music')

    song_list = ""

    for root, dirs, files in songs:
        level = root.replace('data/Music', '').count(os.sep)
        indent = ' ' * 4 * (level)
        song_list += '{}{}\r\n'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if '.meta' not in f:
                continue
            song_list += '{}{}\r\n'.format(subindent, song_name_from(root, f))

    with open('song_list.txt', 'w') as song_list_file:
        song_list_file.write(song_list)

def song_name_from(root, file):
    path = root + "/" + file
    with open(path, 'r') as meta_file:
        return meta_file.readline().rstrip()


if __name__ == '__main__':
    generate_song_list()
