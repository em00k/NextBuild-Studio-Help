#!/bin/bash

set -e

paths=(
	"/home/usb/Applications/NextBuildStudio/resources/app/extensions/em00k.nextbuild-viewers/"
	"/home/usb/.nextbuild-studio/extensions/em00k.nextbuild-viewers-0.9.52/"
	"/home/usb/Documents/GitHub/nextbuild-viewers-linux/"
	)


for f in "${paths[@]}"; do 
		
	# Copy the jsonfiles to the live directory
	cp -r jsonfiles/keywords.json $f/data/
	cp -r jsonfiles/nextbuild_constants.json $f/data/
	cp -r jsonfiles/nextbuild_snippets.json $f/snippets/
done 

	

