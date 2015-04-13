""" Sorts the loose files in a given directory into folders based on the file type.
"""

import os
import sys
import shutil

# Add the directory you want to sort here
BASE_DIR = ''


class MyDict(dict):
    """Allows a dictionary entry to reference another entry in the same dictionary."""
    def __getitem__(self, item):
        return dict.__getitem__(self, item) % self

# Defines the sub-folders items are to be sorted into
path = MyDict({
    'base': BASE_DIR,
    # Entertainment
    'entertainment': '%(base)s\\Entertainment',
    'film': '%(entertainment)s\\Film',
    'music': '%s(entertainment)s\\Music',
    # Software
    'software': '%(base)s\\Software',
    'installer': '%s(software)s\\Installers',
    # Documents
    'document': '%(base)s\\Documents',
    # Images
    'image': '%(base)s\\Images'
})

# Defines which path file types should be moved to
types = {
    # Software
    'exe': 'installer',
    'msi': 'installer',

    # Film
    'mp4': 'film',

    # Music
    'mp3': 'music',

    # Document
    'pdf': 'document',
    'djvu': 'document',

    # Image
    'jpg': 'image',
    'png': 'image',
    'psd': 'image',
    'tif': 'image',
    'tiff': 'image'
}


def main():
    files = [f for f in os.listdir(path['base']) if os.path.isfile(os.path.join(path['base'], f))]

    for file in files:
        extension = file.split('.')[-1]
        file_type = types.get(extension, None)

        if file_type:
            new_file_path = path[file_type]
            make_dir(new_file_path)
            shutil.move(os.path.join(path['base'], file), os.path.join(new_file_path, file))


def make_dir(d):
    """Creates a new directory if one does not already exist."""
    if not os.path.exists(d):
        os.makedirs(d)

if __name__ == '__main__':
    sys.exit(main())