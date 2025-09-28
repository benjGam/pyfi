#!/bin/sh
token=$(cat token.txt)

rm -rf ./dist/ *.egg-info/ ./build/ # Clean previous build
python3 -m build # Rebuild
twine check dist/*
twine upload --username __token__ --password $token dist/*