#!/bin/bash

# Exit in case of error
set -e

# Clear previous builds
echo "Removing old build artifacts..."
rm -rf dist/ build/ *.egg-info

# Build the package
echo "Building the package..."
python setup.py sdist bdist_wheel

# Upload the package to PyPI
echo "Uploading the package to PyPI..."
twine upload dist/*

echo "Deployment to PyPI completed successfully."
