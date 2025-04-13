import os
import subprocess

def midi_to_wav(midi_path, soundfont_path, output_wav_path):
    if not os.path.exists(midi_path):
        raise FileNotFoundError(f"MIDI file not found: {midi_path}")
    if not os.path.exists(soundfont_path):
        raise FileNotFoundError(f"SoundFont file not found: {soundfont_path}")

    command = [
        "fluidsynth",
        "-ni", soundfont_path,
        midi_path,
        "-F", output_wav_path,
        "-r", "44100"  
    ]

    subprocess.run(command, check=True)
    print(f"Converted '{midi_path}' to '{output_wav_path}'")

midi_to_wav("melody.mid", "FluidR3_GM.sf2", "melody.wav")