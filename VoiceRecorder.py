import sounddevice as sd
from scipy.io.wavfile import write, read
import numpy as np

def audio_record(time_span, rate=44100, output_path="audio_output.wav"):
    print("Audio recording started...")
    recorded_audio = sd.rec(int(time_span * rate), samplerate=rate, channels=2, dtype=np.int16)
    sd.wait()  # Await the completion of the recording
    print("Audio recording finished. Storing the file...")
    write(output_path, rate, recorded_audio)
    print(f"Audio file stored as {output_path}")

def audio_playback(input_path):
    print(f"Initiating playback for {input_path}...")
    rate, audio_data = read(input_path)
    sd.play(audio_data, rate)
    sd.wait()  # Await the completion of the playback
    print("Playback concluded.")

# Example usage:
record_time = 5  # seconds
file_path = "audio_output.wav"

audio_record(record_time, output_path=file_path)
audio_playback(file_path)