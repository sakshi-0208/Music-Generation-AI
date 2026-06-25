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

2. Technologies Used
   
   1) Python 
   2) TensorFlow / Keras 
   3) Music21 
   4) NumPy 
   5) LSTM Neural Networks

3. Dataset

   The project uses a collection of MIDI files from classical composers such as Mozart, Chopin,        Haydn, and Beethoven.
   The dataset is organized into folders, and all .mid files are automatically loaded from             subfolders for training.

4. Install all required libraries using:

   pip install -r requirements.txt

   Main libraries used:

    numpy,
    tensorflow,
    music21
  
6. How to Run

   Run the following commands step by step:

   1) python extract_notes.py
      Extracts notes from MIDI files and creates notes.pkl

   2) python train_model.py
      Trains LSTM model and saves it as music_model.h5

   3) python generate_music.py
      Generates new music and saves output as output.mid

7. How It Works
   1) MIDI files are converted into note sequences
   2) LSTM neural network learns musical patterns
   3) Model predicts next notes in sequence
   4) Generated notes are converted back into MIDI format
   5) Final output is saved as AI-generated music (output.mid)
  
Author:
Sakshi Bondre
