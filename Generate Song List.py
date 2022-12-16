import json
import os
import traceback


def generate_song_list():
    if not os.path.exists('data/Music'):
        print('No data/Music directory found')
        return False

    songs = os.walk('data/Music')

    song_list = ""
    groups = {'_$ungrouped_songs$_': []}

    for root, dirs, files in songs:
        level = root.replace('data/Music', '').count(os.sep)
        indent = ' ' * 4 * level
        song_list += f'{indent}- {os.path.basename(root)}\n'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.endswith('.meta'):
                continue
            song_name, instrument_set, seq_type, seq_groups = parse_meta_file(root, f)
            song_list += f'{subindent}key: {song_name}\n'
            for group in seq_groups:
                if group not in groups:
                    groups[group] = []
                groups[group].append(song_name)
            if not seq_groups:
                groups['_$ungrouped_songs$_'].append(song_name)

    try:
        create_song_list_file(song_list, groups)
    except Exception as e:
        print("An error occured creating song list")
        print(traceback.format_exc())
        return False

    return True


def create_song_list_file(song_list, groups):
    with open('song_list.txt', 'w', encoding='utf-8') as song_list_file:
        song_list_file.write(song_list)

    if groups:
        with open('groups_list.json', 'w', encoding='utf-8') as groups_file:
            json_output = {'groups': groups, 'ungrouped_songs': groups.pop('_$ungrouped_songs$_')}
            if not json_output['ungrouped_songs']:
                del json_output['ungrouped_songs']
            json.dump(json_output, groups_file, indent=4, ensure_ascii=False, sort_keys=True)


def parse_meta_file(root, file):
    path = root + "/" + file
    with open(path, 'r', encoding='utf-8') as meta_file:
        lines = meta_file.readlines()

    # Strip newline(s)
    lines = [line.rstrip() for line in lines]
    song_name = lines[0]
    instrument_set = lines[1]
    seq_type = lines[2] if len(lines) >= 3 else 'bgm'
    groups = [g.strip() for g in lines[3].split(',')] if len(lines) >= 4 else []

    return song_name, instrument_set, seq_type, groups


def main():
    song_list_generated = generate_song_list()

    if song_list_generated:
        print("song_list.txt file successfully created!")
        print("Have fun customizing your randomizer! :)")
        print("")
    else:
        print("An error occured generating your song list")
    input("Press enter to quit.")


if __name__ == '__main__':
    main()
