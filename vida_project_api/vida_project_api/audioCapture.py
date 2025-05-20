import pyaudio
import wave
import time
import os

format = pyaudio.paInt16
channel = 1
rate = 44100
recordingDuration = 5
outputFile = "gravacao.wav"

p = pyaudio.PyAudio()

stream = p.open(format=format, 
                channels=channel,
                rate = rate,
                input=True,
                frames_per_buffer=1024)

os.system("clear")
print("Gravando...")

for i in range(5):
    print(f"{i}s")
    time.sleep(1)

frames = []

for _ in range(0, int(rate / 1024 * recordingDuration)):
    data = stream.read(1024)
    frames.append(data)

print("Gravacao finalizada.")

stream.stop_stream()
stream.close()
p.terminate()

with wave.open(outputFile, 'wb') as wf:
    wf.setnchannels(channel)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))