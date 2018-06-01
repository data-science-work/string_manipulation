import re


def main():
    # TODO: Convert to CLI application
    # TODO: Learn to create args and flags as CLI app
    # TODO: Able to write training data for trex or p2s models
    fc = read_file('./content.txt')
    wp = remove_punctuation(fc)
    write_content_without_punctuation(wp)


def read_file(path):
    """Read content of single file.
    The file's content expected is string

    Args:
        path: {string} absolute path of a give file

    Retruns:
        (string) entire file content
    """

    with open(path, 'r') as fi:
        text = fi.read()
        return text


def remove_punctuation(text):
    """Removes punctuation from string.

    Args:
        text: (string) any given string

    Returns:
        (string) content passed in without punctuation
    """

    return re.sub(r'[^\w\s]', '', text)


def write_content_without_punctuation(text, file_name='new_file'):
    """Writes content to file to relative root path.

    Args:
        text: (string) content to be written to file
        file_name: (string) name for the file to be output, default name `new_ile`.

    Returns:
        None
    """ # noqa

    with open(f'{file_name}.txt', 'w') as fo:
        fo.write(text)


if __name__ == '__main__':
    main()
