#!/usr/bin/env python3

# for every PNG file in "/cygdrive/e/Games/PCSX2 1.6.0/snaps", use magick to convert that file to JPG.

import os

dirname = "/cygdrive/e/Games/PCSX2 1.6.0/snaps"
source_ext = ".png"
dest_ext = ".jpg"

def convert_file(dirname, filename):
    source = os.path.join(dirname, filename)
    dest = os.path.join(dirname, filename.replace(source_ext, dest_ext))
    os.system("magick convert \"" + source + "\" -resize 1024x1024 \"" + dest + "\"")

def convert_folder(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith(source_ext):
            convert_file(dirname, filename)

if __name__ == "__main__":
    convert_folder(dirname)
