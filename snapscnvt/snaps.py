#!/usr/bin/env python3

from dircnv import cnv_win_to_cyg_path
import os
import sys
import subprocess

dirname = "/cygdrive/e/Games/PCSX2 1.6.0/snaps"

def is_wide(path):
    width = subprocess.check_output(["magick", "identify", "-format", "%w", path])
    return int(width) > 1024

def convert_file(dirname, filename, source_ext):
    dest_ext = ".jpg"
    source = os.path.join(dirname, filename)
    dest = os.path.join(dirname, filename.replace(source_ext, dest_ext))
    # if dest does not exist, convert source to dest
    wide = is_wide(source)
    if not os.path.exists(dest) or wide:
        print("converting", source, "to", dest)
        resize = " -resize 1024x1024" if wide else ""
        os.system('magick convert "' + source + '"' + resize + ' "' + dest + "\"")
        # delete source
        os.remove(source)

def convert_folder(dirname):
    print (f"converting folder {dirname}")
    for filename in os.listdir(dirname):
        ext = os.path.splitext(filename)[1]
        if ext in [".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".CR2", ".JPG"]:
            convert_file(dirname, filename, ext)

if __name__ == "__main__":
    # if there is a command line argument, use it as the directory to convert
    if len(sys.argv) > 1:
        dirname = cnv_win_to_cyg_path(sys.argv[1])
    convert_folder(dirname)
    print("done")
