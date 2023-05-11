import scipy.io.wavfile
import matplotlib.pyplot as plt

rate, data = scipy.io.wavfile.read('file.wav')
plt.plot(data)
plt.show()
