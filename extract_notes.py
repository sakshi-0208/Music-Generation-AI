import os
import pickle
from music21 import converter, instrument, note, chord

notes = []

# Read all MIDI files from all subfolders
for root, dirs, files in os.walk("dataset"):
    for file in files:
        if file.endswith(".mid"):
            file_path = os.path.join(root, file)
            print("Parsing:", file_path)

            midi = converter.parse(file_path)

            notes_to_parse = None
            try:
                parts = instrument.partitionByInstrument(midi)
                notes_to_parse = parts.parts[0].recurse()
            except:
                notes_to_parse = midi.flat.notes

            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

# Save notes
with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("✅ Notes extracted successfully!")
print("Total notes:", len(notes))