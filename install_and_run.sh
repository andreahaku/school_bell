#!/bin/bash

# Define required packages
REQUIRED_PACKAGES=("python3" "pip" "ffmpeg")
PYTHON_PACKAGES=("streamlit" "pydub")

# Function to check and install system dependencies
echo "Checking system dependencies..."
for pkg in "${REQUIRED_PACKAGES[@]}"; do
    if ! command -v $pkg &> /dev/null; then
        echo "$pkg not found, installing..."
        if [[ "$pkg" == "ffmpeg" ]]; then
            sudo apt update && sudo apt install -y ffmpeg
        else
            sudo apt update && sudo apt install -y $pkg
        fi
    else
        echo "$pkg is already installed."
    fi
done

echo "Checking Python dependencies..."
# Install required Python packages system-wide
for pkg in "${PYTHON_PACKAGES[@]}"; do
    if ! pip show $pkg &> /dev/null; then
        echo "$pkg not found, installing..."
        pip install --upgrade $pkg
    else
        echo "$pkg is already installed."
    fi
done

# Run the application
echo "Starting MP3 Scheduler..."
streamlit run mp3_scheduler.py