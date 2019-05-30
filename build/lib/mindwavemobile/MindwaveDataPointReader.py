from .MindwaveMobileRawReader import MindwaveMobileRawReader
import struct
import collections
import sys

from .MindwavePacketPayloadParser import MindwavePacketPayloadParser

class MindwaveDataPointReader:
    def __init__(self, address=None):
        self._mindwaveMobileRawReader = MindwaveMobileRawReader(address=address)
        self._dataPointQueue = collections.deque()

    def start(self):
        self._mindwaveMobileRawReader.connectToMindWaveMobile()

    def isConnected(self):
        return self._mindwaveMobileRawReader.isConnected()

    def readNextDataPoint(self):
        if (not self._moreDataPointsInQueue()):
	    # print("Queue is empty, loading new point...")
            self._putNextDataPointsInQueue()
	    # print("Queue successfully refilled")
        return self._getDataPointFromQueue()

    def _moreDataPointsInQueue(self):
        return len(self._dataPointQueue) > 0
    
    def _getDataPointFromQueue(self):
        return self._dataPointQueue.pop();
    
    def _putNextDataPointsInQueue(self):
        dataPoints = self._readDataPointsFromOnePacket()
        self._dataPointQueue.extend(dataPoints)
    
    def _readDataPointsFromOnePacket(self):
        self._goToStartOfNextPacket()
        payloadBytes, checkSum = self._readOnePacket()
        if (not self._checkSumIsOk(payloadBytes, checkSum)):
            print("checksum of packet was not correct, discarding packet...")
            return self._readDataPointsFromOnePacket();
        else:
            dataPoints = self._readDataPointsFromPayload(payloadBytes)
        self._mindwaveMobileRawReader.clearAlreadyReadBuffer()
        return dataPoints;
        
    def _goToStartOfNextPacket(self):
	loops = 0
        while(True):
	# while (loops < 3):
	    # print("Going to start of next packet...")
            byte = self._mindwaveMobileRawReader.getByte()
	    # print("Data Byte: %x",byte )
	    loops += 1
            if (byte == MindwaveMobileRawReader.START_OF_PACKET_BYTE):  # need two of these bytes at the start..
		# print("Met first if condition")
                byte = self._mindwaveMobileRawReader.getByte()
		# print("First if branch completed")
                if (byte == MindwaveMobileRawReader.START_OF_PACKET_BYTE):
		    # print("Met second if condition")
                    # now at the start of the packet..
                    return;

    def _readOnePacket(self):
            payloadLength = self._readPayloadLength();
            payloadBytes, checkSum = self._readPacket(payloadLength);
            return payloadBytes, checkSum
    
    def _readPayloadLength(self):
        payloadLength = self._mindwaveMobileRawReader.getByte()
        return payloadLength

    def _readPacket(self, payloadLength):
        payloadBytes = self._mindwaveMobileRawReader.getBytes(payloadLength)
        checkSum = self._mindwaveMobileRawReader.getByte()
        return payloadBytes, checkSum

    def _checkSumIsOk(self, payloadBytes, checkSum):
        sumOfPayload = sum(payloadBytes)
        lastEightBits = sumOfPayload % 256
        invertedLastEightBits = self._computeOnesComplement(lastEightBits) #1's complement!
        return invertedLastEightBits == checkSum;
    
    def _computeOnesComplement(self, lastEightBits):
        return ~lastEightBits + 256
        
    def _readDataPointsFromPayload(self, payloadBytes):
        payloadParser = MindwavePacketPayloadParser(payloadBytes)
        return payloadParser.parseDataPoints();
    
    
    
    
