import os

folderPath = r'data/mix/B/'

fileSequence = 0

for filename in os.listdir(folderPath):
	os.rename(folderPath + filename, folderPath + 'cancerB_' + str(fileSequence) + '.jpg')
	fileSequence +=1