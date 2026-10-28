# About

Simple program that randomizes notes in an osu!taiko map. No dependencies required.

This project was inspired by [hamood enjoyer](https://osu.ppy.sh/users/20855973), who wrote a similar Python script and shared it via Discord.

# Usage
> [!WARNING]
> This program can produce uncanny patterns. Use for experimental purposes only.

1. Clone repository:
```bash
git clone https://github.com/somebodythirtythree/TaikoNoteRandomizer.git
```
2. Open your desired beatmap's .osu file.
3. Scroll down to **[HitObjects]**. Copy every single line below **[HitObjects]** and paste it into the file `PASTE NOTES HERE.txt` inside the project directory.
4. Run the script:
```bash
python main.py 
```
5. Once executed successfully, copy everything in `output.txt`.
6. Create a new difficulty for that beatmap and paste those notes into that new difficulty's .osu file.
