import os
import sys

# File to store the current resolution state
state_file = "resolution_state.txt"

# Resolutions you want to toggle between
resolution_16_9 = 'qres.exe /x 1920 /y 1080 /r:360'
resolution_4_3 = 'qres.exe /x 1568 /y 1080 /r:360'

def get_current_state():
    if os.path.exists(state_file):
        with open(state_file, 'r') as file:
            return file.read().strip()
    return "16:9"  # Default resolution if file does not exist

def save_current_state(state):
    with open(state_file, 'w') as file:
        file.write(state)

def toggle_resolution():
    current_state = get_current_state()

    if current_state == "16:9":
        # Switch to 4:3 resolution
        os.system(resolution_4_3)
        save_current_state("4:3")
    else:
        # Switch to 16:9 resolution
        os.system(resolution_16_9)
        save_current_state("16:9")

if __name__ == "__main__":
    toggle_resolution()
