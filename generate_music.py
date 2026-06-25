import numpy as np
import pickle
import random
from music21 import instrument, note, stream, chord
from tensorflow.keras.models import load_model

model = load_model("music_model.h5")

with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))
note_to_int = {note: num for num, note in enumerate(pitchnames)}
int_to_note = {num: note for num, note in enumerate(pitchnames)}

sequence_length = 100

start = random.randint(0, len(notes) - sequence_length)
pattern = notes[start:start + sequence_length]

output_notes = []

for i in range(200):
    input_seq = [note_to_int[n] for n in pattern]
    input_seq = np.reshape(input_seq, (1, len(input_seq), 1))
    input_seq = input_seq / float(len(pitchnames))

    prediction = model.predict(input_seq, verbose=0)
    index = np.argmax(prediction)

    result = int_to_note[index]
    output_notes.append(result)

    pattern.append(result)
    pattern = pattern[1:]

print("Generated notes:")
print(output_notes[:50])

offset = 0
output_stream = stream.Stream()

for pattern in output_notes:

    if '.' in pattern or pattern.isdigit():

        notes_in_chord = pattern.split('.')

        chord_notes = []

        for current_note in notes_in_chord:
            try:
                new_note = note.Note(int(current_note))
                chord_notes.append(new_note)
            except:
                pass

        if len(chord_notes) > 0:
            new_chord = chord.Chord(chord_notes)
            new_chord.offset = offset
            output_stream.append(new_chord)

    # Single note
    else:
        try:
            new_note = note.Note(pattern)
            new_note.offset = offset
            output_stream.append(new_note)
        except:
            pass

    offset += 0.5

output_stream.write('midi', fp='output.mid')

print("Music generated: output.mid")