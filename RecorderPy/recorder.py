import pyaudio 
import wave
import os

save_path = 'C:/Users/Jaskaran/gesture/data/clean/'

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)


frames = []
try:
    print("Recording Started:")
    while True:
        data=stream.read(1024)
        frames.append(data)

except KeyboardInterrupt:
    print("Recording Ended")
    pass 

stream.stop_stream()
stream.close()
audio.terminate()
i=0
completeName = os.path.join(save_path, f"sample_recording{i}.wav")
#a = f"{save_path}sample_recording{i}.wav"
#print(a)
while os.path.exists(f"{save_path}sample_recording{i}.wav"):
    i += 1
#sound_file = wave.open(a, "wb")
sound_file = wave.open(f"{save_path}sample_recording{i}.wav", "wb")
#f"{save_path}+"/"+"sample_recording"+{i}+".wav""
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(16000)
sound_file.writeframes(b''.join(frames))
sound_file.close()

