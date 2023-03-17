from __future__ import annotations
import json
import os
import subprocess
import sys


# Specify the full path to your rando directory if necessary.
# Defaults to 3 directories up from current (e.g. this file is in data/Music/OoT-Custom-Sequences inside rando)
RANDO_DIRECTORY = '../../..'


def parse_meta_file(root: str, file: str) -> tuple[str, str, str, list[str]]:
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
    if not os.path.exists('data/Music'):
        raise Exception('No data/Music directory found')
    rando_script_path = os.path.join(RANDO_DIRECTORY, 'OoTRandomizer.py')
    if not os.path.isfile(rando_script_path):
        raise Exception(f'Randomizer not found at path "{rando_script_path}". Please modify "RANDO_DIRECTORY" in this file to point to a valid randomizer directory.')

    if not os.path.exists('Output'):
        os.mkdir('Output')
    songs = os.walk('data/Music', followlinks=True)
    for root, dirs, files in songs:
        root = root.replace('\\', '/')
        for f in files:
            if not f.endswith('.meta'):
                continue
            seq_path = os.path.join(root, f"{f[:-5]}.seq")
            if not os.path.isfile(seq_path):
                print(f'Sequence file "{seq_path}" does not exist.')
                continue

            song_name, instrument_set, seq_type, seq_groups = parse_meta_file(root, f)

            output_folder = f"{root.replace('data/Music', 'Output')}"
            output_base = f"{output_folder}/{f[:-5]}"
            cosmetic_plando_filename = f'{output_base}_cosmetic.json'
            settings_filename = f'{output_base}_settings.json'
            os.makedirs(output_folder, exist_ok=True)

            if os.path.isfile(f"{output_base}.z64"):
                rom_modified = os.path.getmtime(f"{output_base}.z64")
                seq_modified = os.path.getmtime(seq_path)
                meta_modified = os.path.getmtime(os.path.join(root, f))
                if rom_modified > seq_modified and rom_modified > meta_modified:
                    continue

            sequence_slot = "Fairy Fountain"
            if seq_type == "fanfare":
                sequence_slot = "Zelda's Lullaby"

            cosmetic_plando = {
                "bgm": {
                    sequence_slot: song_name,
                },
            }
            with open(f'{cosmetic_plando_filename}', 'w', encoding='utf-8', newline='') as file:
                json.dump(cosmetic_plando, file, indent=4)

            rando_settings = {
                "enable_cosmetic_file": True,
                "cosmetic_file": os.path.abspath(cosmetic_plando_filename),
                "output_dir": os.path.abspath(output_folder),
                "output_file": f[:-5],
                "create_compressed_rom": True,
                "create_spoiler": False,
                "create_cosmetics_log": False,
                "starting_items": {
                    "Ocarina": 1,
                    "Zeldas Lullaby": 1,
                },
            }
            with open(f'{settings_filename}', 'w', encoding='utf-8', newline='') as file:
                json.dump(rando_settings, file, indent=4)

            print(f'Generating ROM for "{output_base.replace("Output/", "")}".')
            subprocess.run([sys.executable, rando_script_path, "--settings", os.path.abspath(settings_filename)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=False, check=True)
            os.remove(settings_filename)
            os.remove(cosmetic_plando_filename)


if __name__ == '__main__':
    main()
