#!/bin/sh
# Build the site (outputs into .build directory)
cactus build -v

# Rename the ".build" directory to "build" (Netlify seems to have problems with
# the leading dot in the name)
mv .build build

# Copy redirect configuration to build directory
cp _redirects build/
