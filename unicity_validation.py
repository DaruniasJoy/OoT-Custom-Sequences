import os 
import json


def validate_song_name_unicity():
    song = os.walk('data/Music')

    meta_files = [ build_meta_file(location, files) for location, directories, files in song if len(directories) == 0]

    song_details = flatten_list(meta_files)

    duplications = []

    for index, song in enumerate(song_details):
        song_duplicates = compare_song(song, song_details[index::])
        if len(song_duplicates) > 1:
            duplications.append(song_duplicates)

    if len(duplications) == 0:
        print("No duplication")

    for duplication in duplications:
        print(json.dumps(duplication, indent=2))
        print("===")


def build_meta_file(location, files):
    meta_path_list = [ location + "/" + file for file in files if ".meta" in file ]
    return [ song_info_from(meta_file_path) for meta_file_path in meta_path_list ]

def song_info_from(meta_file_path):
    return {
            'path': meta_file_path,
            'song_name': get_registered_song_name(meta_file_path)
            }

def get_registered_song_name(meta_file_path):
    with open(meta_file_path) as meta_file:
        return meta_file.readline().rstrip()

def flatten_list(base_list):
    return [item for sublist in base_list for item in sublist]

def compare_song(base_song, song_list):
    duplicate = []
    for song in song_list:
        if base_song["song_name"] == song["song_name"]:
            duplicate.append(song)

    return duplicate

if __name__ == '__main__':
    validate_song_name_unicity()
    input("Press Enter to quit")
