import logging
import tinytag


logger = logging.getLogger(__name__)


def check_and_get_album_from_id3(files):
    if not files:
        raise ValueError('Files must not be empty!')

    head, *tail = files
    tag = tinytag.TinyTag.get(head)
    album = tag.album

    if not tail:
        return album

    tail_album = check_and_get_album_from_id3(tail)
    if album == tail_album:
        return album
    else:
        raise RuntimeError('Album differs: {} != {}'.format(album, tail_album))


def check_and_get_artist_from_id3(files):
    if not files:
        raise ValueError('Files must not be empty!')

    head, *tail = files
    tag = tinytag.TinyTag.get(head)
    artist = tag.artist

    if not tail:
        return artist

    tail_artist = check_and_get_artist_from_id3(tail)
    if artist == tail_artist:
        return artist
    else:
        raise RuntimeError('Artist differs: {} != {}'.format(artist, tail_artist))


class AudioFiles:

    def __init__(self, folder_files):
        self.folder_files = folder_files

    @property
    def name(self):
        from audioconcat.util import remove_special_characters

        artist = None
        try:
            artist = check_and_get_artist_from_id3(self.folder_files.files)
        except Exception as ex:
            logger.warning('Can not use artist for name, reason: %s', ex)

        try:
            album = check_and_get_album_from_id3(self.folder_files.files)
        except Exception as ex:
            logger.warning('Can not use album for name, reason: %s Try to use folder name.', ex)
            album = self.folder_files.name

        if artist and album:
            return '{} - {}'.format(remove_special_characters(artist), remove_special_characters(album))
        else:
            return '{}'.format(remove_special_characters(album))

    def __str__(self):
        return '{}: name={}, folder_files={}'.format(self.__class__.__name__, self.name, self.folder_files)
