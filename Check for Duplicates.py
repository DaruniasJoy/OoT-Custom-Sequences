import argparse
import json
import os
import sys
import textwrap


def get_duplicate_songs():
    songs = os.walk('data/Music')
    meta_files = [ build_meta_file(location, files) for location, directories, files in songs if len(directories) == 0]
    song_details = flatten_list(meta_files)
    duplications = []

    for index, song in enumerate(song_details):
        song_duplicates = compare_song(song, song_details[index::])
        if len(song_duplicates) > 1:
            duplications.append(song_duplicates)

    return duplications


def validate_song_name_unicity():
    duplications = get_duplicate_songs()

    if len(duplications) == 0:
        print("No duplication")

    for duplication in duplications:
        print(json.dumps(duplication, indent=2))
        print("===")


def build_meta_file(location, files):
    meta_path_list = [ location + "/" + file for file in files if file.endswith(".meta") ]
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


class ArgumentDefaultsHelpFormatter(argparse.RawTextHelpFormatter):

    def _get_help_string(self, action):
        return textwrap.dedent(action.help)


def main():
    parser = argparse.ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--ci', help='Use while running this in a GitHub action.', action='store_true')
    args = parser.parse_args()

    if args.ci:
        duplicates = get_duplicate_songs()
        if duplicates:
            print(f"Duplicate song names found: {len(duplicates)}\n")
            for duplicate in duplicates:
                print(json.dumps(duplicate, indent=2))
            sys.exit(1)
        print("No duplicates found.")
        sys.exit(0)

    validate_song_name_unicity()
    input("Press Enter to quit")


if __name__ == '__main__':
    main()
