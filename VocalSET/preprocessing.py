from pydub.silence import split_on_silence
from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_wav("D:\VocalSET\FULL\male11\long_tones\messa\m11_long_messa_o.wav")
chunks = split_on_silence(audio, min_silence_len=200, silence_thresh=-50, keep_silence=100)
print(len(chunks))
for counter, el in enumerate(chunks):
    el.export("D:\VocalSET\\tmp\chunk" + str(counter) + ".wav", format="wav")