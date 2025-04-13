# Assignment1_Group12
🎧🧠 Audio Codec Project – Modular Hearing Aid Compression
🎯 Project Description
This project was developed as part of a course assignment on audio compression and perceptual signal processing. Our team selected the Modular Hearing Aid Codec, simulating WDRC (Wide Dynamic Range Compression) behavior, to implement and evaluate compression techniques targeted at speech clarity enhancement, commonly used in assistive listening devices.

📋 Tasks Completed
✅ Audio Recording
A 3–4 minute voice recording was produced where each team member:

Introduced themselves with name and student ID

Described their assigned responsibilities and contributions to the project

✅ Signal Analysis using MATLAB
The raw waveform of the recorded audio was analyzed using MATLAB.

The time-domain waveform and frequency spectrum were plotted.

Observations were made about energy concentration in speech-dominant bands (e.g., 300 Hz – 3 kHz).

✅ Audio Compression (Modular Hearing Aid – WDRC)
A custom compression algorithm was implemented in MATLAB using the WDRC model with soft-knee transition.

Audio was compressed based on:

Compression Ratio

Attack and Release Time

Dynamic range kneepoints

Output was saved in .wav format for high fidelity.

✅ Quality Comparison with MP3
The same recording was compressed using the MP3 format via FFmpeg.

A custom calc_psnr.m function was written to compute PSNR (Peak Signal-to-Noise Ratio) between the original and each compressed version.

Results showed that WDRC maintained higher PSNR (~32.5 dB) compared to MP3 (~25.6 dB), reflecting better preservation of waveform fidelity.

✅ MIDI Music Integration (Optional)
A simple MIDI track was optionally generated to match the duration of the spoken audio.

The MIDI background and compressed voice audio were mixed to simulate an assistive listening experience with background music.

