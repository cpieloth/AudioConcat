# Getting Started

## Requirements

* Windows (not tested on Linux or MacOS)
* Python 3, tested on v3.10 and v3.11
* FFmpeg
  * default location: `C:\Programs_unpacked\ffmpeg-win64-static\bin\ffmpeg.exe`
  * configure via CLI with `--ffmpeg-exec` or `-e`, or
  * configure via environment variable `FFMPEG_EXEC`
  * tested with `ffmpeg-20200724-21442a8-win64-static.zip`
* Audio files must be sorted into folders, e.g. one folder for each album


## Installation

1. Download *FFmpeg* from [ffmpeg.org](https://ffmpeg.org)
2. Extract it to `C:\Programs_unpacked\ffmpeg-win64-static\bin\ffmpeg.exe`
3. Install python package:

```bash
$ pip install git+https://github.com/cpieloth/AudioConcat.git@master#egg=AudioConcat
```


## Command Line Usage

```bash
# Print help
audioconcat --help

# Print help of the sub command 'concat'
audioconcat concat --help
```
