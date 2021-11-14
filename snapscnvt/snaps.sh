# for every PNG file in "/cygdrive/e/Games/PCSX2 1.6.0/snaps", use magick to convert that file to JPG.

cd "/cygdrive/e/Games/PCSX2 1.6.0/snaps"

for f in `ls -1 *.png`
do
  j=`basename $f .png`.jpg
  if [ ! -f "$j" ]
  then
    echo converting $f to $j
    magick $f -resize 1024x1024 $j
  fi
done
