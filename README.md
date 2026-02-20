# About this program

This simple program reads a file containing osu!taiko note objects [(see this link for reference on hit object syntax)](https://osu.ppy.sh/wiki/en/Client/File_formats/osu_(file_format)#hit-objects), and then writes new notes that have randomized hitsounds.

# How to use this program

1. Open your desired beatmap's .osu file.
2. Scroll down to **[HitObjects]**. Copy every single line below **[HitObjects]** and paste it into the file `PASTE NOTES HERE.txt` inside the project directory.
3. Run `main.py` in your IDE or terminal.
4. Wait for the program to execute. When done, it will print "Done" and paste the generated notes into `output.txt`.
5. Copy everything inside `output.txt`.
6. Create a new difficulty for that beatmap and paste those notes into that new difficulty's .osu file.
