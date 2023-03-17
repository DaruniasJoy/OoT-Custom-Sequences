This script will automatically generate a ROM for each sequence in the repository. It requires the randomizer itself (you'll want to change RANDO_DIRECTORY at the top if the default doesn't work for you).

BGM sequences will be mapped to Fairy Fountain to play on the file select screen. Fanfare sequences will be mapped to Zelda's Lullaby with an Ocarina and ZL in your inventory to play it quickly.

Make sure you have plenty of free space if you run this for the whole repository because at the current size of the repository it generates 26.5 GB of ROM files.

If you run it a second time after generating all the ROMs, it'll check if there was a ROM generated after the last change to the .meta/.seq files for that track. If so, it'll skip that sequence, allowing this script to be used to update the ones that need it without regenerating over 800 rando ROMs.