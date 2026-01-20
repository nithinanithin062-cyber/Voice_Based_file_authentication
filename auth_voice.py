import sounddevice as sd
import librosa
import numpy as np
from scipy.io.wavfile import write
fs=44100
seconds=8
print("starts autenication")
audio=sd.rec(int(seconds*fs),samplerate=fs,channels=1)
sd.wait()
write("test_voice.wav",fs,audio)

fixed_y,fixed_sr=librosa.load("fixed_voice.wav")
test_y,test_sr=librosa.load("test_voice.wav")
fixed_zcr=np.mean(librosa.feature.zero_crossing_rate(fixed_y))

test_zcr=np.mean(librosa.feature.zero_crossing_rate(test_y))
fixed_sc=np.mean(librosa.feature.spectral_centroid(y=fixed_y,sr=fixed_sr))

test_sc=np.mean(librosa.feature.spectral_centroid(y=test_y,sr=test_sr))
zcr_diff=abs(fixed_zcr-test_zcr)
sc_diff=abs(fixed_sc-test_sc)
if zcr_diff<0.02 and sc_diff<300:
    print("VOICE MATCHED")
    with open("protected_file.txt","r")as f:
        print(f.read())
else:
    print("NO MATCH ")
    print("failured to open the file")