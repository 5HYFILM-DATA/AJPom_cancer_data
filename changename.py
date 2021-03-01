import os

folderPath = r'data/mix/normal/'

fileSequence = 0

for filename in os.listdir(folderPath):
	os.rename(folderPath + filename, folderPath + 'normal_' + str(fileSequence) + '.jpg')
	fileSequence +=1