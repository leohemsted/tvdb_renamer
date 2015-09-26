# tvdb_renamer
Take data from tvdb.com and rename media files to a reasonable format (that plex can actually identify). Output format is `s##e## - Episode Name.file-format`.

## Usage

Grab script. Create a file **data.tsv** with data lifted straight from www.tvdb.com. Make sure you remove any characters from the episode name that are not legal in a filename (slashes, colons, etc)

Example data from [Rick and Morty Season 1](http://thetvdb.com/?tab=season&seriesid=275274&seasonid=567215&lid=7)
```
1 x 1	Pilot	2013-12-02
1 x 2	Lawnmower Dog	2013-12-09
1 x 3	Anatomy Park	2013-12-16
1 x 4	M. Night Shaym-Aliens!	2014-01-13
1 x 5	Meeseeks and Destroy	2014-01-20
1 x 6	Rick Potion #9	2014-01-27
1 x 7	Raising Gazorpazorp	2014-03-10
1 x 8	Rixty Minutes	2014-03-17
1 x 9	Something Ricked This Way Comes	2014-03-24
1 x 10	Close Rick-Counters of the Rick Kind	2014-04-07
1 x 11	Ricksy Business	2014-04-14
```

then run `python media_renamer.py folder regex [dry_run]` where folder is the path the media is stored in, and regex is a regex used to identify the existing episode numbers. eg:

```
$ python media_renamer.py /q/Videos/TV\ Shows/Rick\ and\ Morty/Season\ 1 "e(\d+)"
Renaming media files in q:\Videos\TV Shows\Rick and Morty\Season 1
rick.and.morty.s01e01-720p.mkv -> s01e01 - Pilot.mkv
rick.and.morty.s01e02-720p.mkv -> s01e02 - Lawnmower Dog.mkv
rick.and.morty.s01e03-720p.mkv -> s01e03 - Anatomy Park.mkv
rick.and.morty.s01e04-720p.mkv -> s01e04 - M. Night Shaym-Aliens!.mkv
rick.and.morty.s01e05-720p.mkv -> s01e05 - Meeseeks and Destroy.mkv
rick.and.morty.s01e06-720p.mkv -> s01e06 - Rick Potion #9.mkv
rick.and.morty.s01e07-720p.mkv -> s01e07 - Raising Gazorpazorp.mkv
rick.and.morty.s01e08-720p.mkv -> s01e08 - Rixty Minutes.mkv
rick.and.morty.s01e09-720p.mkv -> s01e09 - Something Ricked This Way Comes.mkv
rick.and.morty.s01e10-720p.mkv -> s01e10 - Close Rick-Counters of the Rick Kind.mkv
rick.and.morty.s01e11-720p.mkv -> s01e11 - Ricksy Business.mkv
```
