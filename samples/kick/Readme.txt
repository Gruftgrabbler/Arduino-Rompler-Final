This folder contains the kickdrum sample data
samplerate = 11025, samples = 1440, duration ~= 131ms
Encoding Header: 8BitUnsigned, No twos_complement conversion applied, MONO
Encoding WavFile: 16BitPCM, MONO

python reduce_samplerate.py ../samples/kick/kick.raw.h 1 -plt -c -p -t -w ../samples/kick/writeback.wav -sr 11025
