#!/bin/bash

# Check if a terminal emulator is available
TERMINAL=$(command -v gnome-terminal || command -v xfce4-terminal || command -v konsole || command -v x-terminal-emulator)

if [ -z "$TERMINAL" ]; then
    echo "No supported terminal emulator found. Please run manually in a terminal."
    exit 1
fi

# Run the Streamlit app in a new terminal and open the browser
$TERMINAL -e "bash -c 'streamlit run mp3_scheduler.py; exec bash'" &

# Wait a few seconds to ensure the app starts
sleep 3

# Open the web browser to the Streamlit app
xdg-open http://localhost:8501
