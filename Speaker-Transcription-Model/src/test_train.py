import glob
for file in glob.iglob('trainingData/**/*.wav', recursive=True):
    # print(file.split("\\")[1]+'\\'+file.split("\\")[2])
    print(file.replace("trainingData\\","",1))