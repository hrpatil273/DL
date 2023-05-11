import os
import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from featureextraction import extract_features
# from speakerfeatures import extract_features
import warnings

warnings.filterwarnings("ignore")
import time

source = "SampleData/"

# path where training speakers will be saved
modelpath = "Speakers_models/"

gmm_files = [os.path.join(modelpath, fname) for fname in
             os.listdir(modelpath) if fname.endswith('.gmm')]

# Load the Gaussian gender Models
models = [cPickle.load(open(fname, 'rb')) for fname in gmm_files]
speakers = [fname.split("/")[-1].split(".gmm")[0] for fname
            in gmm_files]
error = 0
total_sample = 0.0

print("Enter the File name from Test Audio Sample Collection :")
path = input().strip()
print("Testing Audio : ", path)
sr, audio = read(source + path)
vector = extract_features(audio, sr)

log_likelihood = np.zeros(len(models))

for i in range(len(models)):
    gmm = models[i]  # checking with each model one by one
    scores = np.array(gmm.score(vector))
    log_likelihood[i] = scores.sum()

winner = np.argmax(log_likelihood)
if log_likelihood[winner] < -20:
    print("\tUnable to identify")
else:
    print("\tdetected as - ", speakers[winner])
    #print("\tpercentage - ", log_likelihood[winner])
    #print("\tpercentage - ", winner)
    time.sleep(1.0)
    import speech_recognition as sr
    r = sr.Recognizer()
    audio = source + path
    with sr.AudioFile(audio) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print(speakers[winner] + " :- " + text)
        text_file = open("sample.txt", "w")
        n = text_file.write(speakers[winner] + " :- " + text)
        text_file.close()

    except Exception as e:
        print(e)
    print("Hurrey ! Speaker identified. Mission Accomplished Successfully. ")