This folder contains a single cycle sine waveform generated with audacity
Freq = 440Hz, Samplerate = 22050, Samples = 50
Encoding Header: 8BitUnsigned, No twos_complement conversion applied
Encoding WavFile: 16BitPCM

cd py
python reduce_samplerate.py ../samples/sineWavetable/sine.raw.h 1 -p -t -c -plt -w ../samples/sineWavetable/writeback.wav -sr 22050