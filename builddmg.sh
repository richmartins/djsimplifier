#!/bin/sh
# from : https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/
# slightly modified


# Check if name provided as param
if [ -z $1 ]; then echo "error please provide dmg name"; exit 1; fi

# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/$1.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/$1.dmg" && rm "dist/$1.dmg"
create-dmg \
  --volname "$1" \
  --volicon "img/$1.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "$1.app" 175 120 \
  --hide-extension "$1.app" \
  --app-drop-link 425 120 \
  "dist/$1.dmg" \
  "dist/dmg/"