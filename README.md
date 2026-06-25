Music Generation using AI (LSTM Neural Network)


This project is an AI-based Music Generation System that uses Deep Learning (LSTM neural networks) to generate new musical compositions from MIDI files.

The model learns musical patterns from classical composers like Mozart, Chopin, Haydn, and Beethoven, and then generates completely new music in MIDI format.

1. Features

   1) Processes MIDI music files
   2) Extracts musical notes and chords using Music21
   3) Trains an LSTM-based Deep Learning model
   4) Generates new musical sequences automatically
   5) Saves output as a playable MIDI file
   6) Supports multiple composer datasets

2. Project Structure
Music-Generation-AI/
extract_notes.py        # Extracts notes from MIDI dataset
train_model.py          # Trains LSTM model on note sequences
 generate_music.py       # Generates new music using trained model
 requirements.txt        # Required Python libraries
   README.md               # Project documentation
   output.mid              # Generated music file (after running)
      
