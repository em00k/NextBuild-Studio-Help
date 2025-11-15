#!/bin/bash

DESTINATION_DIR="/home/user/Applications/NextBuildStudio/resources/app/extensions/em00k.nextbuild-viewers"

# Copy the jsonfiles to the live directory
cp -r ../jsonfiles/keywords.json $DESTINATION_DIR/data/
cp -r ../jsonfiles/nextbuild_constants.json $DESTINATION_DIR/data/
cp -r ../jsonfiles/nextbuild_snippets.json $DESTINATION_DIR/snippets/nextbuild.json

# cp -r ../jsonfiles/keywords.json $DESTINATION_DIR/data/
# cp -r ../jsonfiles/nextbuild_constants.json $DESTINATION_DIR/data/
# cp -r ../jsonfiles/nextbuild_snippets.json $DESTINATION_DIR/snippets/
