#!/usr/bin/env python3

# for every PNG file in "/cygdrive/e/Games/PCSX2 1.6.0/snaps", use magick to convert that file to JPG.

import os
import sys
import subprocess

dirname = "/cygdrive/e/Games/PCSX2 1.6.0/snaps"
source_ext = ".png"
dest_ext = ".jpg"

def is_wide(filename):
    width = subprocess.check_output(["magick", "identify", "-format", "%w", filename])
    return int(width) > 1024

def convert_file(dirname, filename, source_ext):
    converted = False
    source = os.path.join(dirname, filename)
    dest = os.path.join(dirname, filename.replace(source_ext, dest_ext))
    # if dest does not exist, convert source to dest
    if not os.path.exists(dest):
        print("converting", source, "to", dest)
        resize = " -resize 1024x1024" if is_wide(source) else ""
        os.system('magick convert "' + source + '"' + resize + ' "' + dest + "\"")
        # delete source
        os.remove(source)
        converted = True
    return converted


def convert_png(dirname, source_ext = ".png", dest_ext = ".jpg"):
    converted = False
    for filename in os.listdir(dirname):
        if filename.endswith(source_ext):
            converted = convert_file(dirname, filename, source_ext) or converted
    if converted:
        print("converted %s files in %s" % (source_ext, dirname))
    else:
        print("no %s files converted in %s" % (source_ext, dirname))


def convert_jpg_file(dirname, filename, dest_ext = ".jpg"):
    converted = False
    source = os.path.join(dirname, filename)
    # if the width is greater than 1024, resize it
    if is_wide(source):
        dest = os.path.join(dirname, filename.replace(
            dest_ext, "_resized" + dest_ext))
        # if dest does not exist, convert source to dest
        if not os.path.exists(dest):
            print("converting", source, "to", dest)
            os.system("magick convert \"" + source +
                      "\" -resize 1024x1024 \"" + dest + "\"")
            # delete source
            os.remove(source)
            converted = True
    return converted


def convert_jpg(dirname, dest_ext = ".jpg"):
    converted = False
    for filename in os.listdir(dirname):
        if filename.endswith(dest_ext):
            converted = convert_jpg_file(dirname, filename, dest_ext) or converted
    if converted:
        print("converted %s files in %s" % (dest_ext, dirname))
    else:
        print("no %s files converted in %s" % (dest_ext, dirname))


if __name__ == "__main__":
    # if there is a command line argument, use it as the directory to convert
    if len(sys.argv) > 1:
        dirname = sys.argv[1]
    convert_png(dirname)
    convert_png(dirname, '.CR2')
    convert_jpg(dirname)
    convert_jpg(dirname, '.JPG')
