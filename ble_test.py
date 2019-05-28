import numpy as np
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
mindwaveDataPointReader = MindwaveDataPointReader()

# connect to the mindwave mobile headset
mindwaveDataPointReader.start()

# read one data point, data point types are specified in MindwaveDataPoints.py
i = 0

meditationList = []

try:
    while(True):
            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            # print dataPoint.__class__.__name__

            # classes: AttentionDataPoint, MeditationDataPoint, RawDataPoint
            #   EEGPowersDataPoint: delta, theta, lowAlpha, highAlpha, 
            #      lowBeta, highBeta, lowGamma, midGamma
            if dataPoint.__class__.__name__ == 'AttentionDataPoint':
                #if (dataPoint > 75):
                    #print('***'),

                #print "i: ", dataPoint
                i += 1

            if dataPoint.__class__.__name__ == 'MeditationDataPoint':

                #print (dataPoint)
		a = int(str(dataPoint))
		print(a)
		#meditationList.append( int(dataPoint) )
		

except KeyboardInterrupt:

    print 'Exited Program'
    mdarray = np.array(meditationList)

    #print 'Meditation std: ', mdarray.std()
    #print 'Meditation avg: ', mdarray.mean()
    #print 'Meditation median: ', mdarray.median()


