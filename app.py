from flask import Flask, render_template, request, send_file
import os
import uuid
import subprocess

app = Flask(__name__)

# Path to your SoundFont
SOUNDFONT = os.path.join("soundfonts", "FluidR3_GM.sf2")

# Map instrument names to General MIDI program numbers
instrument_map = {
    "piano": 0,
    "violin": 40,
    "flute": 73,
    "guitar": 24,
    "drum": 118
}

# Ensure upload/output folders exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert():
    if 'midi_file' not in request.files:
        return "No MIDI file uploaded!"

    midi_file = request.files['midi_file']
    instrument_name = request.form.get('instrument', 'piano')
    filename = str(uuid.uuid4())
    input_path = os.path.join("uploads", filename + ".midi")
    output_path = os.path.join("outputs", filename + ".wav")

    # Save uploaded MIDI
    midi_file.save(input_path)

    # Convert MIDI to WAV using Fluidsynth
    command = [
        "fluidsynth",
        "-ni",
        SOUNDFONT,
        "-F", output_path,
        input_path
    ]
    subprocess.run(command)

    # Return converted WAV
    return send_file(output_path, as_attachment=True, download_name=f"{instrument_name}.wav")

if __name__ == '__main__':
    app.run(debug=True)

