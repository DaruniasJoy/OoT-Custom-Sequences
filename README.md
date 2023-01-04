# Custom Ocarina of Time Music Sequences
The .zip here contains the resources required for custom music sequences in The Legend of Zelda: Ocarina of Time while using the Ocarina of Time Randomizer.

# Installation
Download [this zip file](https://github.com/DaruniasJoy/OoT-Custom-Sequences/archive/master.zip) and extract it. Then move the contents of the "Music" that was inside that zip file into the "Music" folder in the "data" folder next to the randomizer script. If you are using the bundled download version of the randomizer the folder is located in the "resources/app/python/data" folder next to the executable file. If done correctly, the Music folder should now have several subfolders in it, each with the name of a different game or series.

# Requests
If there is a song you would like converted to AudioSeq format and added to the repository, feel free to request it [here](https://docs.google.com/forms/d/e/1FAIpQLSe17AuRzGGx7WaaX70hggeAYDD-NmXA9rOI2QIKbPCQIhR2tg/viewform). You can also [open an Issue](https://github.com/DaruniasJoy/OoT-Custom-Sequences/issues/new) and request it there.

# Issues with Sequences

Should you find yourself or in a stream that a track is too loud or too quiet, please also feel free to either [open an Issue](https://github.com/DaruniasJoy/OoT-Custom-Sequences/issues/new) or contact us in [Discord](https://discord.gg/EVpd499gkS) in the appropiate channel.

# Customize your own Cosmetic file

To get the song list of your current version of the project you can launch the script `Generate Song List.py`, this one will create a `song_list.txt` file with all song sorted by license and the required key to complete in the cosmetic json file.

```txt
- Music
    - Kingdom Hearts Series
        - Kingdom Hearts
             key: Kingdom Hearts - Dearly Beloved
             key: Kingdom Hearts - Gummi Ship #1
             key: Kingdom Hearts - Hollow Bastion
             key: KH - Dearly Beloved
             key: Kingdom Hearts - Traverse Town
             key: Kingdom Hearts - Dive to the Heart
        - Kingdom Hearts 2
             key: Kingdom Hearts 2 Final Mix - Sora's Theme
             key: Kingdom Hearts II - Sinister Sundown
             key: Kingdom Hearts 2 Final Mix - Cavern of Remembrance
             key: Kingdom Hearts II - The 13th Struggle
    - StarTropics
         key: StarTropics - Miracola Village
         key: Dungeon - StarTropics
...
...
```

# Submissions
The best way to submit your own AudioSeqs is by following the [GitKraken guide on the randomizer's wiki](https://wiki.ootrandomizer.com/index.php?title=GitKraken). As long as the AudioSeq works and doesn't have any objectively bad audio issues it will be merged in.

If you believe a sequence can be better adapted you can either contact the original author and collaborate on improving it to replace the current one, or submit it as a second AudioSeq and meta file with either a number appended to the end (Song Title-2.seq) or a short identifier such as your/your username's initials. (Song Title-dj.seq)

You can also submit a true remix or original creation if you do not wish to recreate a piece of music entirely.

## Preferred locations
When submitting a new song to the repository, you can use the fourth line of the `.meta` file to specify which locations would be appropriate for playing your song. You can do this by writing out a comma-separated list of music groups, such as: `HyruleField,Fields,Outdoors,Overworld`. **We are asking for all new submissions to include this line.** If you do not add it, another contributor may add it for you, using their best judgment.
 
There are four levels of specificity for music groups: **Exact**, **High**, **Mid**, and **Low**. (For fanfares, high and mid specificity are the same group.) In order for our default plando files to work, **you will need to include at least one group for each level of specificity.** Otherwise, your song may be excluded from consideration when shuffling music. (Some groups, such as `ChildDungeon`, may cover multiple levels of specificity.)
 
Some examples of valid location annotations:
- `HyruleField,GerudoValley,Fields,Outdoors,Overworld` (for BGM)
- `ChamberOfTheSages,ChildDungeon,CharacterTheme` (groups can be freely mixed and matched as long as all specificity levels are covered)
- `ItemGet,HeartPieceGet,ItemFanfare,SuccessFanfare,EventFanfare` (for fanfares)
- `DoorOfTime,SongOfTime,BigFanfare,UtilitySong,EventFanfare,SongFanfare` (for ocarina songs or other fanfares)
 
Some examples of invalid location annotations:
- `HyruleField,Market,LonLonRanch` (not all specificity levels are covered)
- `WindmillHut,SongOfStorms,Indoors,SongFanfare` (you should not mix BGM and fanfare locations - your song is either BGM or a fanfare/ocarina song, but not both)
 
We have created a standard list of default music groups that we are recommending for submissions to the repository, which can be found in [this spreadsheet](https://docs.google.com/spreadsheets/d/1EQWuVbshgFJ6wOlPSVCt5OcUpEQjaabOUi7aXCb84i0/edit?usp=sharing). We also have a web tool that will automatically tell you which music groups to include, based on the locations where you want your songs to play, which you can find [here](https://thesounddefense.github.io/musicgroups/).

# DMCA-Critical Sequences
Until further notice Sequences that could trigger DMCA-Strikes on any platform wont be added to the repository.
Copyright Critical Sequences you can share here : [Ganondorfs Organ](https://github.com/GanondorfsOrgan/Ganondorfs-Organ).



# Credits 
* [Spreadsheet](https://docs.google.com/spreadsheets/d/1Yvgjex502cB_dVvvZm0a88aGL4WNFOm-5XvEbZLkWqI/edit)
* Darkangel93x ([Twitch](https://twitch.tv/darkangel93x), [Twitter](https://twitter.com/DarkangelTwitch))
* TrenteR ([Twitch](https://twitch.tv/trenter_tr))
* DeathBasket: the original BotW Hyrule Castle, BotW Kass Theme, Ikana Castle, Groose's Theme, and Snowfield from the Majora's Mask Ranodmizer modified to work properly in Ocarina of Time
* SPTKira: Added Majora's Mask Sequences and Fanfares
* ShockinglySane: Added Gruntilda's Lair and more Banjo Kazooie sequences.
* Doncamilo ([YouTube](https://www.youtube.com/channel/UCie8do7HeS6yB2ngmoau0Nw))
* Kevin R. Midna's Lament arrangement, The Lick (Requiem of Spirit Ver.), untitled original composition
* Delcatty16 ([Twitch](https://twitch.tv/delcatty16)) Dark Cave, Ecruteak City and Hyrule Temple.
* IAmNamedGravy
* NewSoupVi ([Youtube](https://www.youtube.com/user/Timmifutzelchen), [Twitch](https://www.twitch.tv/newsoupvi))
* TheGael95 ([Youtube](https://www.youtube.com/channel/UCiD6DYZSuu7N2302h83pLeQ))
* MissMissingno
* DezZival ([Youtube](https://www.youtube.com/channel/UCcz2H4QpuFSyvgIdxSxYVeg))
* SlyryD 
* MrMario7788 ([Twitch](https://twitch.tv/mrmario7788))
* Nighttime71
* Apasher ([Youtube](https://www.youtube.com/channel/UCvqipEoq2CKQEcP-0MrKtlQ))
* DuffleGamer
* YoshiKyon ([Twitch](https://twitch.tv/yoshikyon), [Twitter](https://twitter.com/yoshikyon))
* FQef ([Twitch](https://twitch.tv/fqef92)) 
* Kirox
* SonicRPika
* Sirius902
* Fish_waffle64
* Bluwiikoon
* PolyGanon ([Twitch](https://twitch.tv/polyganon))
* Liamnajor
* Zeldaboy14
* Dkdavidlp ([Youtube](https://www.youtube.com/channel/UCfmNZCRlAflXmiDu2ENB10w))
* The Sound Defense
* ocdizzle
* Volcove
* Zeraphyr
* Yackole
* Joshua8600 ([YouTube](https://www.youtube.com/Joshua8600), [Twitch](http://twitch.tv/Joshua8600))
* Shijima
* Dominator_101
* 3Pills
* LuigiXHero
* OwlIsNotACat
* Taximadish
* Cuphat
* 
