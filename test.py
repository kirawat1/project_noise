# นำเข้าไลบรารี Pandas
import pandas as pd

# สร้าง DataFrame จากรายการข้อมูล
data = {
    'ชื่อ': ['John', 'Alice', 'Bob', 'David'],
    'อายุ': [28, 24, 22, 30],
    'เงินเดือน': [45000, 38000, 32000, 51000]
}

df = pd.DataFrame(data)

# แสดงข้อมูลใน DataFrame
print(df)

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# กำหนด path ของไฟล์เสียง
audio_file = 'D:\\CS\\Project_\\testttt\\1-137-A-32.wav'

# โหลดไฟล์เสียง

y, sr = librosa.load(audio_file)

# แสดงกราฟ waveform ของเสียง
plt.figure(figsize=(12, 8))
librosa.display.waveshow(y, sr=sr, color=None)
plt.title('Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

# คำนวณและแสดง spectrogram
D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
plt.figure(figsize=(12, 8))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()

