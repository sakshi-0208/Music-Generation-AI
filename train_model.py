import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Activation
from tensorflow.keras.utils import to_categorical

# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))
n_vocab = len(pitchnames)

note_to_int = {note: num for num, note in enumerate(pitchnames)}

sequence_length = 100

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in seq_in])
    network_output.append(note_to_int[seq_out])

n_patterns = len(network_input)

X = np.reshape(network_input, (n_patterns, sequence_length, 1))
X = X / float(n_vocab)

y = to_categorical(network_output)

# Model
model = Sequential()
model.add(LSTM(256, return_sequences=True, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.3))
model.add(LSTM(256))
model.add(Dense(128))
model.add(Dropout(0.3))
model.add(Dense(n_vocab))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train
model.fit(X, y, epochs=15, batch_size=64)

model.save("music_model.h5")

print("Model trained successfully!")