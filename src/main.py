# /bin/python3

import os
import time
import random
# import playsound
from networktables import NetworkTables

# IP of the RoboRIO
ROBO_RIO_IP = "10.34.7.2"

# Name of the table to use in the NetworkTables
SOUND_TABLE_NAME = "Sounds"

# The NetworkTables key of the selector value
SOUND_SELECTOR_KEY = "Selector"

# The NetworkTables key of the play value
SOUND_PLAY_KEY = "Play"

# Extra arguments to give to the `play` command
EXTRA_PLAY_ARGS = ""

sound_id_to_path = [
    "sfx/slip.mp3",
    "sfx/r2d2-scream.mp3"
]

current_sound_id = -1

NetworkTables.initialize(server=ROBO_RIO_IP)

def play_current_sound():
    if current_sound_id == -1:
        print(f"Skipping play bc selector is -1")
    cmd = f"play {EXTRA_PLAY_ARGS} {sound_id_to_path[current_sound_id]}"
    print(f"Playing sound #{current_sound_id}")
    print(f"Running command '{cmd}'")
    os.system(cmd)

def valueChanged(table, key, value, isNew):
    global current_sound_id
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    if key == SOUND_SELECTOR_KEY:
        current_sound_id = int(value)
        print(f"Set selector to {current_sound_id}")
    elif key == SOUND_PLAY_KEY:
        print("Wahoo!")
        play_current_sound()

def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)

NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)


def main():
    print("I'm alive!")
    # print(table.to_bytes())
    sd = NetworkTables.getTable(SOUND_TABLE_NAME)

    sd.addEntryListener(valueChanged)
    # sd.putNumber("Selector",-1)
    # sd.putNumber("Play",0)

    print("Added the entry listener")
    # playsound.playsound("sfx/ding.mp3")
    while True:
        # if random.randint(0,10) == 0:
        #     os.system('play sfx/wilhelm-scream.mp3')
        time.sleep(1)


if __name__ == "__main__":
    main()
