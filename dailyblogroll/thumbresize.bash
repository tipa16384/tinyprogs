#!/usr/bin/env bash
set -euo pipefail

src_dir="blogrolls/images"
dst_dir="$src_dir/resized"

mkdir -p "$dst_dir"

# Handle filenames with spaces; match .png and .PNG
find "$src_dir" -maxdepth 1 -type f \( -iname '*.png' \) -print0 |
while IFS= read -r -d '' src; do
  fname="$(basename "$src")"
  dest="$dst_dir/$fname"
  # Force exact 240x160 (ignore aspect ratio)
  convert "$src" -resize 240x160\! "$dest"
done

echo "Done. Resized files are in: $dst_dir"

