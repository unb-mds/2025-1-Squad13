import pyaudio
import wave
import time
import os
import torchaudio
from pathlib import Path
from speechbrain.inference import SpeakerRecognition

testingVoice = "testingVoice.wav"
secretVoice = "secretVoice.wav"

def recording(filename):
    format = pyaudio.paInt16
    channel = 1
    rate = 44100
    recordingDuration = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=format, 
                    channels=channel,
                    rate = rate,
                    input=True,
                    frames_per_buffer=1024)

    frames = []

    os.system("clear")

    print(f"Recording duration: {recordingDuration}s")
    if(filename == "testingVoice.wav"): print("Recording voice testing")
    elif(filename == "secretVoice.wav"): print("Recording secret voice")

    aux = 0
    for i in range(0, int(rate / 1024 * recordingDuration)):
        data = stream.read(1024)
        frames.append(data)
        if int(i % ((rate / 1024 * recordingDuration)/recordingDuration)) == 0:
            print(f"{aux}s")
            aux+=1

    print("Finish recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channel)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

arquivo = Path("secretVoice.wav")
if(not arquivo.exists() and not arquivo.is_file()):
    recording(secretVoice)

recording(testingVoice)

verification = SpeakerRecognition.from_hparams(
                        source="speechbrain/spkrec-ecapa-voxceleb",
                        savedir="pretrained_models/spkrec")

score, prediction = verification.verify_files(testingVoice, secretVoice)
print(f"Score: {score}, Match: {prediction}")