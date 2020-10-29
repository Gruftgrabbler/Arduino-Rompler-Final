This folder contains 1 second 440Hz sine sample
Freq = 440Hz, samplerate = 11050, samples = 11050
Encoding Header: 8BitUnsigned, No twos_complement conversion applied
Encoding WavFile: 16BitPCM

cd python
python reduce_samplerate.py ../samples/sineLong/sine.raw.h 1 -p -t -w ../samples/sineWavetable/writeback.wav -sr 11025

sine_pre.png: Clear sinewave after pt8211
sine_post.png: Distorted sinewave after op amp