import easygopigo3
import time
import numpy as np
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
mindwaveDataPointReader = MindwaveDataPointReader()

# connect to the mindwave mobile headset
mindwaveDataPointReader.start()

#Instantiate GoPiGo Object
GPG = easygopigo3.EasyGoPiGo3()


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
			if dataPoint > 60:
				GPG.forward()
			else: GPG.stop()

except: 
	KeyboardInterrupt()
	bye = "Goodbye"
	print bye
	GPG.stop()
