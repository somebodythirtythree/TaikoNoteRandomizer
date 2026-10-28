# About

Simple program that randomizes notes in an osu!taiko map. No dependencies required.

This project was inspired by [hamood enjoyer](https://osu.ppy.sh/users/20855973), who wrote a similar Python script and shared it via Discord.

# How to use this program

1. Open your desired beatmap's .osu file.
2. Scroll down to **[HitObjects]**. Copy every single line below **[HitObjects]** and paste it into the file `PASTE NOTES HERE.txt` inside the project directory.
3. Run `main.py` in your IDE or terminal.
4. Wait for the program to execute. When done, it will print "Done" and paste the generated notes into `output.txt`.
5. Copy everything inside `output.txt`.
6. Create a new difficulty for that beatmap and paste those notes into that new difficulty's .osu file.
