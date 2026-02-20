# x,y,time,type,hitSound,objectParams,hitSample
import random
note_list = []  # list of notes
notes = ['d', 'k']  # Don or kat?
def main():
    global note_list
    with open("PASTE NOTES HERE.txt", 'r') as f1:
        for note in f1:
            note = note.split(',')
            if random.choice(notes) == 'd':
                note[4] = '0'
                note_list.append(','.join(note))
            else:
                note[4] = '8'
                note_list.append(','.join(note))

    with open("output.txt", 'w') as f2:
        for note in note_list:
            f2.write(f"{note}")
        print("Done")


if __name__ == '__main__':
    main()
