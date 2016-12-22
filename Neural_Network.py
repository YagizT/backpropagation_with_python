import numpy as np
import Functions as f

class NeuralNetwork():
    def __init__(self, layerSizeArray):
        self.layerArray = []
        self.weightArray = []
        for i in range(0, len(layerSizeArray)):
            self.layerArray.append(np.zeros( (1, layerSizeArray[i]), dtype=float))
            if i != 0:
                self.weightArray.append(np.random.random((layerSizeArray[i - 1], layerSizeArray[i])))

        print self.layerArray
        print self.weightArray

    def setInput(self, inputArray):
        if self.layerArray[0].shape == inputArray.shape:
            self.layerArray[0] = inputArray
        else:
            print "error occured"
            exit()

    def fire(self):
        for i in range(0, len(self.weightArray)):
            self.layerArray[i + 1] = np.dot(f.sig(self.layerArray[i]), self.weightArray[i])

    def getOutput(self):
        return self.layerArray[len(self.layerArray) - 1]



a = NeuralNetwork([ 1, 2, 3])
a.setInput(np.array([2.0]).reshape((1,1)))
a.fire()
print "output: " + str(a.getOutput())


