import json
import os
import traceback

# Parts of this shamelessly taken from Generate Song List.py.

def initialGroupDict():
    return {
        "bgm": {
            "HyruleField": createDictEntry(["exact"]),
            "LostWoods": createDictEntry(["exact"]),
            "GerudoValley": createDictEntry(["exact"]),
            "Market": createDictEntry(["exact"]),
            "KakarikoChild": createDictEntry(["exact"]),
            "KakarikoAdult": createDictEntry(["exact"]),
            "LonLonRanch": createDictEntry(["exact"]),
            "KokiriForest": createDictEntry(["exact"]),
            "GoronCity": createDictEntry(["exact"]),
            "ZorasDomain": createDictEntry(["exact"]),
            "CastleCourtyard": createDictEntry(["exact"]),
            "HorseRace": createDictEntry(["exact"]),
            "Mini-game": createDictEntry(["exact"]),
            "ShootingGallery": createDictEntry(["exact"]),
            "FairyFountain": createDictEntry(["exact"]),
            "TempleOfTime": createDictEntry(["exact"]),
            "ChamberOfTheSages": createDictEntry(["exact"]),
            "House": createDictEntry(["exact", "high"]),
            "Shop": createDictEntry(["exact"]),
            "PotionShop": createDictEntry(["exact"]),
            "WindmillHut": createDictEntry(["exact", "high"]),
            "InsideDekuTree": createDictEntry(["exact"]),
            "DodongosCavern": createDictEntry(["exact"]),
            "JabuJabu": createDictEntry(["exact"]),
            "ForestTemple": createDictEntry(["exact"]),
            "FireTemple": createDictEntry(["exact"]),
            "IceCavern": createDictEntry(["exact"]),
            "WaterTemple": createDictEntry(["exact"]),
            "SpiritTemple": createDictEntry(["exact"]),
            "ShadowTemple": createDictEntry(["exact"]),
            "CastleUnderground": createDictEntry(["exact"]),
            "CastleEscape": createDictEntry(["exact"]),
            "Battle": createDictEntry(["exact"]),
            "MinibossBattle": createDictEntry(["exact"]),
            "BossBattle": createDictEntry(["exact"]),
            "FireBoss": createDictEntry(["exact"]),
            "GanondorfBattle": createDictEntry(["exact"]),
            "GanonBattle": createDictEntry(["exact"]),
            "TitleTheme": createDictEntry(["exact"]),
            "ZeldaTheme": createDictEntry(["exact"]),
            "SheikTheme": createDictEntry(["exact"]),
            "DekuTree": createDictEntry(["exact"]),
            "KaeporaGaebora": createDictEntry(["exact"]),
            "FairyFlying": createDictEntry(["exact"]),
            "GanondorfTheme": createDictEntry(["exact"]),
            "KotakeAndKoume": createDictEntry(["exact"]),
            "IngoTheme": createDictEntry(["exact"]),
            "Fields": createDictEntry(["high"], 3),
            "Town": createDictEntry(["high"], 8),
            "Fun": createDictEntry(["high"], 3),
            "MagicalPlace": createDictEntry(["high"], 3),
            "SalesArea": createDictEntry(["high"], 2),
            "ChildDungeon": createDictEntry(["high", "mid"], 3),
            "AncientDungeon": createDictEntry(["high"], 2),
            "MysticalDungeon": createDictEntry(["high"], 3),
            "SpookyDungeon": createDictEntry(["high"], 3),
            "SmallFight": createDictEntry(["high", "mid"], 2),
            "BossFight": createDictEntry(["high"], 2),
            "FinalFight": createDictEntry(["high"], 2),
            "HeroTheme": createDictEntry(["high", "mid"], 6),
            "VillainTheme": createDictEntry(["high", "mid"], 3),
            "Outdoors": createDictEntry(["mid"], 13),
            "Indoors": createDictEntry(["mid"], 8),
            "AdultDungeon": createDictEntry(["mid"], 8),
            "BigFight": createDictEntry(["mid"], 4),
            "Overworld": createDictEntry(["low"], 21),
            "Dungeon": createDictEntry(["low"], 11),
            "Fight": createDictEntry(["low"], 6),
            "CharacterTheme": createDictEntry(["low"], 9)
        },
        "fanfare": {
            "ItemGet": createDictEntry(["exact"]),
            "HeartContainerGet": createDictEntry(["exact"]),
            "SpiritStoneGet": createDictEntry(["exact"]),
            "HeartPieceGet": createDictEntry(["exact"]),
            "MedallionGet": createDictEntry(["exact"]),
            "LearnSong": createDictEntry(["exact"]),
            "BossDefeated": createDictEntry(["exact"]),
            "EponaRaceGoal": createDictEntry(["exact"]),
            "EscapeFromRanch": createDictEntry(["exact"]),
            "TreasureChest": createDictEntry(["exact"]),
            "MasterSword": createDictEntry(["exact"]),
            "DoorOfTime": createDictEntry(["exact"]),
            "ZeldaTurnsAround": createDictEntry(["exact", "high", "mid"]),
            "GanondorfAppears": createDictEntry(["exact", "high", "mid"]),
            "GameOver": createDictEntry(["exact", "high", "mid"]),
            "PreludeOfLight": createDictEntry(["exact"]),
            "BoleroOfFire": createDictEntry(["exact"]),
            "MinuetOfForest": createDictEntry(["exact"]),
            "SerenadeOfWater": createDictEntry(["exact"]),
            "RequiemOfSpirit": createDictEntry(["exact"]),
            "NocturneOfShadow": createDictEntry(["exact"]),
            "ZeldasLullaby": createDictEntry(["exact"]),
            "EponasSong": createDictEntry(["exact"]),
            "SariasSong": createDictEntry(["exact"]),
            "SunsSong": createDictEntry(["exact"]),
            "SongOfTime": createDictEntry(["exact"]),
            "SongOfStorms": createDictEntry(["exact"]),
            "ItemFanfare": createDictEntry(["high", "mid"], 6),
            "SuccessFanfare": createDictEntry(["high", "mid"], 3),
            "BigFanfare": createDictEntry(["high", "mid"], 3),
            "WarpSong": createDictEntry(["high", "mid"], 6),
            "UtilitySong": createDictEntry(["high", "mid"], 6),
            "EventFanfare": createDictEntry(["low"], 15),
            "SongFanfare": createDictEntry(["low"], 12)
        }
    }

def createDictEntry(specificityLevels, subgroupCount=1):
    return {
        "specificityLevels": specificityLevels,
        "songCount": 0,
        "subgroupCount": subgroupCount
    }

def checkGroupUsage():
    if not os.path.exists('data/Music'):
        print("No data/Music directory found.")
        return False

    invalidData = {
        "bgm": {
            "noGroupSongs": [],
            "invalidGroupSongs": [],
            "nonStandardGroups": {}
        },
        "fanfare": {
            "noGroupSongs": [],
            "invalidGroupSongs": [],
            "nonStandardGroups": {}
        }
    }

    fullGroups = initialGroupDict()

    songs = os.walk('data/Music')

    for root, dirs, files in songs:
        for f in files:
            if not f.endswith('.meta'):
                continue
            songName, instrumentSet, seqType, seqGroups = parse_meta_file(root, f)
            oppositeSeqType = "fanfare" if seqType == "bgm" else "bgm"

            exactFound = highFound = midFound = lowFound = invalidGroups = False
            groupSet = set()

            # If this song has no groups, note that.
            if len(seqGroups) < 1:
                invalidData[seqType]["noGroupSongs"].append(songName)
                continue
            # Check all of the groups assigned to this song.
            for seqGroup in seqGroups:
                if seqGroup in fullGroups[seqType]:
                    # If this group was already seen, that's an error.
                    if seqGroup in groupSet:
                        invalidGroups = True
                        continue
                    # Increase the usages of this group by 1.
                    groupEntry = fullGroups[seqType][seqGroup]
                    groupEntry["songCount"] += 1
                    groupSet.add(seqGroup)

                    # Check the specificity levels.
                    if "exact" in groupEntry["specificityLevels"]:
                        exactFound = True
                    if "high" in groupEntry["specificityLevels"]:
                        highFound = True
                    if "mid" in groupEntry["specificityLevels"]:
                        midFound = True
                    if "low" in groupEntry["specificityLevels"]:
                        lowFound = True
                elif seqGroup in fullGroups[oppositeSeqType]:
                    # This song is using a group of the wrong type.
                    invalidGroups = True
                else:
                    # This song is using a group that is not pre-defined (a typo, maybe?)
                    invalidGroups = True
                    if seqGroup in invalidData[seqType]["nonStandardGroups"]:
                        invalidData[seqType]["nonStandardGroups"][seqGroup].append(songName)
                    else:
                        invalidData[seqType]["nonStandardGroups"][seqGroup] = [songName]

            # Make sure we have all specificity levels.
            if not exactFound or not highFound or not midFound or not lowFound:
                invalidGroups = True
            # If the song is invalid for some reason, mark it.
            if invalidGroups:
                invalidData[seqType]["invalidGroupSongs"].append(songName)
    
    # We've collected all of our data. Now we need to write it out.
    try:
        createGroupInfoFile(fullGroups, invalidData)
    except Exception as e:
        print("An error occurred while writing out group_info.txt.")
        print(e)
        print(traceback.format_exc())
        return False

    return True

def parse_meta_file(root, file):
    path = f'{root}/{file}'
    with open(path, 'r', encoding='utf-8') as meta_file:
        lines = meta_file.readlines()
    
    # Strip newline(s)
    lines = [line.rstrip() for line in lines]
    song_name = lines[0]
    instrument_set = lines[1]
    seq_type = lines[2].lower() if len(lines) >= 3 else "bgm"
    groups = [g.strip() for g in lines[3].split(',')] if len(lines) >= 4 else []

    return song_name, instrument_set, seq_type, groups

def createGroupInfoFile(fullGroupData, invalidData):
    insufficientSongs = {
        "bgm": [],
        "fanfare": []
    }
    with open('group_info.txt', 'w', encoding='utf-8') as groupInfoFile:
        for category, categoryData in fullGroupData.items():
            if category == "bgm":
                groupInfoFile.write("========\n")
                groupInfoFile.write("BGM info\n")
                groupInfoFile.write("========\n\n")
            else:
                groupInfoFile.write("============\n")
                groupInfoFile.write("Fanfare info\n")
                groupInfoFile.write("============\n\n")
            for groupName, groupInfo in categoryData.items():
                songCount = groupInfo["songCount"]
                subgroupCount = groupInfo["subgroupCount"]
                countString = f'{groupName}: {songCount} songs ({subgroupCount} needed for coverage)'
                if subgroupCount > songCount:
                    insufficientSongs[category].append(countString)
                groupInfoFile.write(f'{countString}\n')
            groupInfoFile.write("\n")

            # If there are any groups with insufficient coverage, say so here.
            if len(insufficientSongs[category]) > 0:
                groupInfoFile.write("The following groups do not have enough coverage:\n")
                for groupLine in insufficientSongs[category]:
                    groupInfoFile.write(f'\t{groupLine}\n')
                groupInfoFile.write("\n")

            # If any non-standard groups were found, list them here.
            if len(invalidData[category]["nonStandardGroups"]) > 0:
                groupInfoFile.write("The following non-standard groups were found in these songs:\n")
                for groupName, songList in invalidData[category]["nonStandardGroups"].items():
                    groupInfoFile.write(f'\t{groupName}\n')
                    for songName in songList:
                        groupInfoFile.write(f'\t-\t{songName}\n')
                groupInfoFile.write("\n")

            # If there are any songs with invalid group data, say so here.
            if len(invalidData[category]["invalidGroupSongs"]) > 0:
                groupInfoFile.write("The following songs have invalid group data:\n")
                for invalidGroupLine in invalidData[category]["invalidGroupSongs"]:
                    groupInfoFile.write(f'\t{invalidGroupLine}\n')
                groupInfoFile.write("\n")

            # If there are any songs with no group data, say so here.
            if len(invalidData[category]["noGroupSongs"]) > 0:
                groupInfoFile.write("The following songs have no group data:\n")
                for noGroupLine in invalidData[category]["noGroupSongs"]:
                    groupInfoFile.write(f'\t{noGroupLine}\n')
                groupInfoFile.write("\n")

def main():
    validationComplete = checkGroupUsage()

    if validationComplete:
        print("group_info.txt successfully generated.\n")
    else:
        print("Error generating group_info.txt.\n")
    input("Press enter to quit.")

if __name__ == '__main__':
    main()