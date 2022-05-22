"""
General utility methods.
"""


def remove_special_characters(input_str):
    """
    Remove (some) special character from string, e.g. comma or Umlaute.

    :param input_str: String to remove special characters.
    :return: String without special characters.
    """
    replacements = [(',', ''), (';', ''), (':', ''),
                    ('/', ''), ('\\', ''),
                    (' & ', ' '), ('&', ' '), ('?', ''), ('!', ''),
                    ('`', ''), ('´', ''), ('\'', ''), ('"', ''),
                    ('(', ''), (')', ''), ('[', ''), (']', ''), ('{', ''), ('}', ''),
                    ('Ä', 'Ae'), ('ä', 'ae'), ('Ö', 'Oe'), ('ö', 'oe'),  ('Ü', 'Ue'), ('ü', 'ue'), ('ß', 'sz')]

    for replacment in replacements:
        input_str = input_str.replace(replacment[0], replacment[1])

    return input_str.strip()
