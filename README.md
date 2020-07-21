# turbine
Wind-controlled sample playback code for AG.

16 reed switches connected to RPi GPIO. When a switch is high, an OSC message is sent to Sonic Pi to trigger sample playback associated with the current wind direction.