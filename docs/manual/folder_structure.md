# Folder Structure

All files of one folder are concatenated to a single file.
The file name is generated using the ID3 meta information *artist* and *album*, as a fallback the folder name is used.

**Example**

The following folder structure:

```
music\children\hänsel & gretel\
music\children\hänsel & gretel\track_01.mp3
music\children\hänsel & gretel\track_02.mp3
music\children\hänsel & gretel\track_03.mp3
music\rock\
music\rock\famous artist\best of\track_01.mp3
music\rock\famous artist\best of\track_02.mp3
```

results in this output:

```
haensel gretel.mp3
famous artist - best of.mp3
```

The origin files of `haensel & gretel.mp3` does not contain ID3 meta information. In addition some special characters are replace or removed.
