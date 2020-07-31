# Getting Started

## Requirements

* Windows (Linux or MacOS requires manual changes)
* Python 3.4 or later
* FFmpeg, located at `C:\Programs_unpacked\ffmpeg-win64-static\bin\ffmpeg.exe`
  * `audioconcat.concat.FfmpegConcat.exec` must be modified for non-Windows operating systems
  * tested with `ffmpeg-20200724-21442a8-win64-static.zip`
* Audio files must be sorted into folders, e.g. one folder for each album


## Installation

1. Download *FFmpeg* from [ffmpeg.org](https://ffmpeg.org)
2. Extract it to `C:\Programs_unpacked\ffmpeg-win64-static\bin\ffmpeg.exe`
3. Install python package:

```bash
$ pip install git+git://github.com/cpieloth/AudioConcat@master#egg=AudioConcat
```


## Command Line Usage

```bash
# Print help
audioconcat --help

# Print help of the sub command 'concat'
audioconcat concat --help
```
