from scipy.io import wavfile
import noisereduce as nr
import os
# load data
read_path = 'C:/Users/Jaskaran/gesture/data/clean/'
i =0
while os.path.exists(f"{read_path}sample_recording{i}.wav"):
    i += 1
i-=1
print("File read:", f"{read_path}sample_recording{i}.wav")
rate, data = wavfile.read(f"{read_path}sample_recording{i}.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write(f"{read_path}samplend_recording{i}.wav", rate, reduced_noise)

print("New audio file generated: ",f"{read_path}samplend_recording{i}.wav")