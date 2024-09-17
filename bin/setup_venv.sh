#!/bin/bash

# install if not present
sudo apt install python3-venv

# Name of the venv
VENV_NAME=venv

# Python version
PYTHON_VERSION=python3
echo "Python version is: $PYTHON_VERSION"

# Project directory
DIR="/home/ubuntu/system-info-collector"

# Requirements file
REQUIREMENTS=requirements.txt

# Check for prerequisites python3, pip and venv module
if ! command -v $PYTHON_VERSION &> /dev/null
then
    echo "$PYTHON_VERSION could not be found."
    exit 1
fi
$PYTHON_VERSION -m pip --version > /dev/null 2>&1 || {
    echo "pip for $PYTHON_VERSION could not be found."
    exit 1
}
$PYTHON_VERSION -c "import venv" > /dev/null 2>&1 || {
    echo "venv module for $PYTHON_VERSION could not be found."
    exit 1
}

# Check if the directory exists
if [ ! -d "$DIR" ]; then
  echo "Directory $DIR does not exist. Stopping execution."
  exit 1
fi

# Navigate to project directory
cd "$DIR" || {
  echo "Cannot navigate to directory $DIR. Stopping execution."
  exit 1
}

# check if requirements file exists
if [ ! -f "$REQUIREMENTS" ]; then
    echo "Requirements file not found!"
    exit 1
fi

# Create a new venv if it doesn't exist
if [ ! -d "$VENV_NAME" ]; then
    $PYTHON_VERSION -m venv $VENV_NAME
fi

# activate the venv
source $VENV_NAME/bin/activate

# Update pip to the latest version
$PYTHON_VERSION -m pip install --upgrade pip

# update the requirements
$PYTHON_VERSION -m pip install -r $REQUIREMENTS --upgrade

echo "Setup (or update) completed."