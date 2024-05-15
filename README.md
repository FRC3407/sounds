# sounds

sound effects and sound controller for outreach robot (and competition?)

## notes
- If the sound doesn't play, do this in bash: `export AUDIODEV=plughw:CARD=wm8960soundcard`

## NetworkTables protocol
To play sounds using another device like the RoboRIO you communicate through NetworkTables. We use the table named "Sounds" to keep our values. To play a sound you must first select it by setting "Selector" to the sound ID, then you can start the sound by changing `Play`

## cool links
- Python NetworkTables library [robotpy/pynetworktables](https://github.com/robotpy/pynetworktables)
