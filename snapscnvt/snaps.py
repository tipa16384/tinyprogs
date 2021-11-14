#!/usr/bin/env python3

# for every PNG file in "/cygdrive/e/Games/PCSX2 1.6.0/snaps", use magick to convert that file to JPG.

import os

dirname = "/cygdrive/e/Games/PCSX2 1.6.0/snaps"
source_ext = ".png"
dest_ext = ".jpg"

def convert_file(dirname, filename):
    converted = False
    source = os.path.join(dirname, filename)
    dest = os.path.join(dirname, filename.replace(source_ext, dest_ext))
    # if dest does not exist, convert source to dest
    if not os.path.exists(dest):
        print ("converting", source, "to", dest)
        os.system("magick convert \"" + source + "\" -resize 1024x1024 \"" + dest + "\"")
        converted = True
    return converted

def convert_folder(dirname):
    converted = False
    for filename in os.listdir(dirname):
        if filename.endswith(source_ext):
            converted = convert_file(dirname, filename) or converted
    if converted:
        print ("converted files in", dirname)
    else:
        print ("no files to convert in", dirname)

if __name__ == "__main__":
    convert_folder(dirname)
