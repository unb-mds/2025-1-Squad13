import pyaudio
import wave
import time
import torchaudio
from pathlib import Path
from speechbrain.inference import SpeakerRecognition
import torch
from datetime import datetime
import warnings
import migration
import io
warnings.filterwarnings("ignore", category=FutureWarning)

# testingVoice = "testingVoice.wav"
# secretVoice = "secretVoice.wav"

#Recording function
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

    print(f"Recording duration: {recordingDuration}s")
    # if(filename == "testingVoice.wav"): print("Testing voice recording")
    # elif(filename == "secretVoice.wav"): print("Secret voice recording")

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
    
    buffer = io.BytesIO()
    with wave.open(buffer, 'wb') as wf:
        wf.setnchannels(channel)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    #audioIput = buffer.getvalue()
    return buffer
    

# #Check if secret .wav recording exists
# arquivo = Path("secretVoice.wav")
# if(not arquivo.exists() and not arquivo.is_file()):
#     recording(secretVoice)

# recording(testingVoice)

#Extract embedding from a .wav audio
def extract_embedding(verification, file_path):
    #signal = verification.load_audio(file_path)

    #transforma a variavel em uma tupla, associando waveform com o tensor do audio e sample_rate com a taxa em hz
    #deve funcionar do msm jeito mas agora sem precisar criar um arquivo com o audio
    waveform, sample_rate = torchaudio.load(file_path)
    signal = waveform
    signal = signal.unsqueeze(0)
    lengths = torch.tensor([1.0])

    embedding = verification.encode_batch(signal, lengths)
    return embedding.squeeze(0)

verification = SpeakerRecognition.from_hparams(
                        source="pretrained_models/spkrec",
                        savedir="pretrained_models/spkrec")

# #Secret embedding
# embedding_path = Path("embeddings/secret_embedding.pt")
# if not embedding_path.exists():
#     secret_embedding = extract_embedding(verification, secretVoice)

#     embedding_path.parent.mkdir(parents=True, exist_ok=True)

#     torch.save(secret_embedding, embedding_path)
# else:
#     secret_embedding = torch.load(embedding_path)

# #Testing voice embedding
# testing_embedding = extract_embedding(verification, testingVoice)

def verify_voice(verification, userEmail):
    newVoice = recording("dá pra tirar o file name eu acho")
    newVoice = extract_embedding(verification, newVoice)
    
    #pega uma serie de vozes desse usuario do banco de dados
    secretVoices = migration.autentication(userEmail)
    
    #acho q o ideal seria pegar uma media de todos os scores
    score = 0
    for v in secretVoices:
        score += verification.similarity(newVoice, v.voice_module)
    score = score/len(secretVoices)
    similarity(score)

def new_secret_voice(verification, userEmail):
   newVoice = recording("dá pra tirar o file name eu acho")
   extract_embedding(verification, newVoice)
   #salva la no banco de dados
   migration.add_new_voice(newVoice, userEmail)
    

# #Verification
# score = verification.similarity(testing_embedding, secret_embedding)

def similarity(score):
    prediction = score > -1.75
    print(f"Score: {score}, Match: {prediction}\n")

    if(prediction):
        print("Valid authentication")
    else:
        print("Invalid voice")

# similarity(score)