#!/bin/bash

# Name of the venv
VENV_NAME=venv

# Python version
PYTHON_VERSION=python3
echo "Python version is: $PYTHON_VERSION"

# Project directory
DIR="/home/ubuntu/system-info-collector"

# Collect script's path
COLLECT_SCRIPT="main.py"

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

# Check if the venv exists
if [ -d "$VENV_NAME" ]; then
    if [ ! -f "$VENV_NAME/bin/activate" ]; then
        echo "Activation script does not exist within the virtual environment. Stopping execution."
        exit 1
    fi
    # Activate the venv
    source $VENV_NAME/bin/activate
    # Validate that python is there
    if ! command -v $PYTHON_VERSION &> /dev/null; then
        echo "The required Python version doesn't exist in the virtual environment. Stopping execution."
        exit 1
    else
        echo "Virtual environment activated successfully."
    fi
else
    echo "Virtual environment doesn't exist. Stopping execution."
    exit 1
fi



# Check if the collect script exists
if [ ! -f "$COLLECT_SCRIPT" ]; then
  echo "Collect script $COLLECT_SCRIPT does not exist. Stopping execution."
  exit 1
fi

# Start collecting info
$PYTHON_VERSION $COLLECT_SCRIPT
COLLECT_SCRIPT_EXIT_CODE=$?
if [ $COLLECT_SCRIPT_EXIT_CODE -ne 0 ]; then
    echo "Failed to execute collect with exit code $COLLECT_SCRIPT_EXIT_CODE. Stopping execution."
    exit 1
else
    echo "Collect executed successfully."
fi