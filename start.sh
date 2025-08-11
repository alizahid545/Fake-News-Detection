#!/bin/bash

echo "========================================"
echo "   Fake News Detection System"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo
echo "Starting the system..."
echo
python3 run.py
