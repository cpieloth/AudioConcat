"""
Module with concat logic.
"""

import datetime
import logging
import pathlib
import subprocess


logger = logging.getLogger(__name__)


class FfmpegConcat:

    def __init__(self):
        # TODO: Make path or command configurable, support for Windows and Linux.
        self.exec = pathlib.Path(r'C:\Programs_unpacked\ffmpeg-win64-static\bin\ffmpeg.exe')

    def concat(self, files, output):
        import tempfile

        with tempfile.TemporaryDirectory() as td:
            f_name = pathlib.Path(td) / 'input.txt'
            with f_name.open('w') as fh:
                fh.writelines(['file \'{}\'\n'.format(str(file.resolve())) for file in files])

            cmd = [str(self.exec), '-nostats', '-loglevel',  'info', '-safe', '0', '-f', 'concat',
                   '-i', str(f_name.resolve()), '-acodec', 'copy', str(output.resolve())]
            subprocess.check_call(cmd)


def retrieve_and_concat_audio_files(input_dir, output_dir):
    from audioconcat.file_system import get_leaf_files
    from audioconcat.file_system import FolderFiles

    for files in get_leaf_files(input_dir):
        try:
            folder_files = FolderFiles(files)
            logger.debug('folder_files=%s', folder_files)
            concat_audio_files(folder_files, output_dir)
        except:
            logger.exception('Could not concat files: %s', files)


def concat_audio_files(folder_files, output_dir):
    from audioconcat.audio_files import AudioFiles

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
