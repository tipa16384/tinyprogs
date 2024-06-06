#!/usr/bin/env python3

import os
import subprocess
import argparse

magick_cmd = 'convert'

class SnapCnvt:
    def __init__(self, input_folder, output_folder, remove_files=False):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.remove_files = remove_files
        self.resize = True
        self.max_width = 1024
        self.crop = False

    def is_wide(self, path):
        try:
            width = int(subprocess.check_output(["identify", "-format", "%w", path]))
            # log file name and detected width
            # print(f"{path} is {width} wide, max_width is {self.max_width}")
            return width > self.max_width
        except Exception as e:
            print("error getting width of", path, e)
            return False

    def convert_file(self, filename):
        # print("convert_file", self.input_folder, self.output_folder, filename)
        dest_ext = ".jpg"
        source = os.path.join(self.input_folder, filename)
        dest_path = os.path.join(self.input_folder, self.output_folder)
        os.makedirs(dest_path, exist_ok=True)
        dest = os.path.join(dest_path, os.path.splitext(filename)[0] + dest_ext)
        wide = self.is_wide(source)
        if not os.path.exists(dest) or wide:
            print("converting", filename)
            resize = " -resize {w}x{w}".format(w = self.max_width) if (wide and self.resize) else ""
            cropper = " -gravity center -crop 16:10" if self.crop else ""
            # log this
            # print ('magick convert "' + source + '"' + resize + ' "' + dest + "\"")
            try:
                os.system('convert "' + source + '"' + resize + cropper + ' "' + dest + "\"")
                if self.remove_files:
                    print("removing", source)
                    os.remove(source)
            except Exception as e:
                print("error converting", source, "to", dest, e)
        else:
            print("skipping", source)

    def convert_folder(self):
        print (f"converting folder {self.input_folder}")
        for filename in os.listdir(self.input_folder):
            # if this is a folder, skip it
            if os.path.isdir(os.path.join(self.input_folder, filename)):
                continue
            ext = os.path.splitext(filename)[-1].lower()
            if ext in [".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".cr2", ".heic", ".webp", ".svg", ".jfif"]:
                self.convert_file(filename)

def convert_to_linux_path(path: str) -> str:
    # if the first two characters are a DOS-style drive letter, convert them to a linux-style path, starting with /mnt/<drive letter>/
    if len(path) > 2 and path[1] == ':':
        return '/mnt/' + path[0].lower() + path[2:].replace('\\', '/')
    return path

parser = argparse.ArgumentParser(description='Image conversion tool')
parser.add_argument('-if', '--input-folder', type=str, required=True, help='input folder')
parser.add_argument('-of', '--output-folder', type=str, help='output folder')
parser.add_argument('-rm', '--remove-files', action='store_true', help='remove files after conversion')
parser.add_argument('-nr', '--no-resize', action='store_false', help='disable resizing')
# add switch to set max width as -w or --max-width with default 1024
parser.add_argument('-w', '--max-width', type=int, help='max width for images')
# add switch for crop.
parser.add_argument('-c', '--crop', action='store_true', help='crop images to 4:3 aspect ratio')

args = parser.parse_args()

input_folder = convert_to_linux_path(args.input_folder if args.input_folder else "F:\\PS5\\CREATE\\Screenshots\\Unicorn Overlord")
output_folder = args.output_folder if args.output_folder else "converted"

snaps = SnapCnvt(input_folder, output_folder, args.remove_files)
snaps.resize = args.no_resize
snaps.max_width = args.max_width if args.max_width else 1024
# set snaps.crop to args.crop
snaps.crop = args.crop

snaps.convert_folder()

print("done")
