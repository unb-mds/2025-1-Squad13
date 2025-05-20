import pyaudio, wave, time, os

formato = pyaudio.paInt16
canais = 1
taxa = 44100
duracaoSegundos = 5
arquivo_saida = "gravacao.wav"

p = pyaudio.PyAudio()

stream = p.open(format=formato, 
                channels=canais,
                rate = taxa,
                input=True,
                frames_per_buffer=1024)

os.system("clear")
print("Gravando...")

for i in range(5):
    print(f"{i}s")
    time.sleep(1)

frames = []

for _ in range(0, int(taxa / 1024 * duracaoSegundos)):
    data = stream.read(1024)
    frames.append(data)

print("Gravacao finalizada.")

stream.stop_stream()
stream.close()
p.terminate()

with wave.open(arquivo_saida, 'wb') as wf:
    wf.setnchannels(canais)
    wf.setsampwidth(p.get_sample_size(formato))
    wf.setframerate(taxa)
    wf.writeframes(b''.join(frames))