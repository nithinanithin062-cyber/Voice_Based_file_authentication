import sounddevice as sd
from scipy.io.wavfile import write
fs= 44100
seconds=8
print("Registered voice")
audio=sd.rec(int(seconds*fs) ,samplerate=fs,channels=1)
sd.wait()
write("fixed_voice.wav",fs,audio)
print("stored voice")
