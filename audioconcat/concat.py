"""
Module with concat logic.
"""

import datetime
import logging
import pathlib
import subprocess
import tempfile

from audioconcat.audio_files import AudioFiles
from audioconcat.file_system import get_leaf_files
from audioconcat.file_system import FolderFiles


logger = logging.getLogger(__name__)


class FfmpegConcat:
    """
    Concat a list of files using FFmpeg.
    """

    def __init__(self):
        # TODO: Make path or command configurable, support for Windows and Linux.
        self.exec = pathlib.Path(r'C:\Programs_unpacked\ffmpeg-win64-static\bin\ffmpeg.exe')

    def concat(self, files, output):
        # using temp dir to enable write and read to a temp file by different processes on some platforms
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_input_path = pathlib.Path(tmp_dir) / 'input.txt'
            with tmp_input_path.open('w') as input_file:
                input_file.writelines(['file \'{}\'\n'.format(str(file.resolve())) for file in files])

            cmd = [str(self.exec), '-nostats', '-loglevel', 'info', '-safe', '0', '-f', 'concat',
                   '-i', str(tmp_input_path.resolve()), '-acodec', 'copy', str(output.resolve())]
            subprocess.check_call(cmd)


def retrieve_and_concat_audio_files(input_dir, output_dir):
    for files in get_leaf_files(input_dir):
        try:
            folder_files = FolderFiles(files)
            logger.debug('folder_files=%s', folder_files)
            concat_audio_files(folder_files, output_dir)
        except:
            logger.exception('Could not concat files: %s', files)


def concat_audio_files(folder_files, output_dir):
    audio_files = AudioFiles(folder_files)
    logger.debug('audio_files=%s', audio_files)
    if len(audio_files.folder_files.extensions) > 1:
        raise RuntimeError('Too many file types in folder: {}'.format(audio_files.folder_files.extensions))

    output_file = output_dir / '{}{}'.format(audio_files.name, next(iter(audio_files.folder_files.extensions)))
    if output_file.exists():
        logger.warning('File already exists: %s. Adding timestamp to name.', output_file)
        time = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
        output_file = output_dir / '{}_{}{}'.format(audio_files.name,
                                                    time,
                                                    next(iter(audio_files.folder_files.extensions)))

    logger.debug('output_file=%s', output_file.resolve())

    ffmpeg = FfmpegConcat()
    ffmpeg.concat(audio_files.folder_files.files, output_file)
