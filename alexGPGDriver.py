import easygopigo3
import time
import numpy as np
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
mindwaveDataPointReader = MindwaveDataPointReader()

# connect to the mindwave mobile headset
mindwaveDataPointReader.start()

#Instantiate GoPiGo Object
GPG = easygopigo3.EasyGoPiGo3()

#sliding window for dynamic threshold
arr = [0,0,0,0,0]
sW = np.array(arr)

#control loop for pi
try:
	while(True):
		dataPoint = mindwaveDataPointReader.readNextDataPoint()
		# print dataPoint.__class__.__name__

	        # classes: AttentionDataPoint, MeditationDataPoint, RawDataPoint
        	#   EEGPowersDataPoint: delta, theta, lowAlpha, highAlpha,
            	#      lowBeta, highBeta, lowGamma, midGamma
		#if dataPoint.__class__.__name__ == 'AttentionDataPoint':
                #if (dataPoint > 75):
                    #print('***'),



                if dataPoint.__class__.__name__ == 'AttentionDataPoint':
			print dataPoint
			dataPoint = int(str(dataPoint))
			threshold = 0
			#update sliding window
			sW[0] = sW[1]
			sW[1] = sW[2]
			sW[2] = sW[3]
			sW[3] = sW[4]
			sW[4] = dataPoint

			#update threshold
			if np.var(sW) > 10:
				threshold = 1

			#Tell it to start or stop
			if threshold:
				GPG.forward()
			else: GPG.stop()

except: 
	KeyboardInterrupt()
	bye = "Goodbye"
	print bye
	GPG.stop()
