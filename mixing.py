from pydub import AudioSegment


audio1 = AudioSegment.from_wav("melody.wav")
audio2 = AudioSegment.from_wav("recorded.wav")


audio1_volume_db = 15
audio2_volume_db = 0

audio1 = audio1 + audio1_volume_db
audio2 = audio2 + audio2_volume_db

max_len = max(len(audio1), len(audio2))
if len(audio1) < max_len:
    audio1 += AudioSegment.silent(duration=max_len - len(audio1))
if len(audio2) < max_len:
    audio2 += AudioSegment.silent(duration=max_len - len(audio2))

mixed = audio1.overlay(audio2)

mixed.export("mixed.wav", format="wav")
print(" Mixing complete. Saved as 'mixed.wav'")
