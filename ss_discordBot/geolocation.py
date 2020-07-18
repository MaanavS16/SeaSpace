import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from numpy import unravel_index
from opencage.geocoder import OpenCageGeocode

#define distance
def euclideanDistanceSquared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

#convert between array position and real-life coordinates
def xyToij(x,y):
    i = 450 - round(5*y)
    j = round(5*x) + 900
    return(i,j)

def ijToxy(i,j):
    x = (j/5) - 180
    y = 90 - (i/5)
    return(x,y)

class Geolocate:
    def __init__(self, geocodeToken, blackThreshold=1):
        # save API key as instance variable
        self.geocoder = OpenCageGeocode(str(geocodeToken))

        # load map as np array
        equirectangularMap = Image.open('equirectangularMap.png').convert('L')
        self.npMap = np.array(equirectangularMap)

        # convert grayscale value into binary state (land or water)
        for i in range(0, self.npMap.shape[0]):
            for j in range(0, self.npMap.shape[1]):
                if self.npMap[i, j] >= blackThreshold:
                    self.npMap[i, j] = 1
                else:
                    self.npMap[i, j] = 0

    def getCoordFromLoc(self, location):
        try:
            locData = self.geocoder.geocode(location)
            return (locData[0]['geometry']['lng'], locData[0]['geometry']['lat'])
        except:
            return 'error'

    def getLocFromCoord(self, x, y):
        try:
            locData = self.geocoder.reverse_geocode(y, x)
            print(locData[0].get('formatted'))
            return locData[0].get('formatted')
        except:
            return 'error'

    def getMap(self, viewGraph=False, points=[(0,0)]):
        if viewGraph:
            plt.imshow(self.npMap, cmap=plt.cm.binary)
            for p in points:
                i, j = xyToij(*p)
                plt.scatter(j, i)
            plt.show()
        return self.npMap

    def isLand(self, x, y):
        #find array position from location and check if k=1 (isLand?)
        i,j = xyToij(x,y)
        if self.npMap[i, j] == 1:
            return True
        else:
            return False

    def findClosestOcean(self, x, y):
        if self.isLand(x,y):
            minDistanceIndexPair = [x**2 + y**2, (0,0)]
            for i in range(0, self.npMap.shape[0]):
                for j in range(0, self.npMap.shape[1]):
                    #check if new coordinate is ocean and is closer to the target than the previous closest
                    if self.npMap[i,j] == 0 and euclideanDistanceSquared((x,y), ijToxy(i,j)) < minDistanceIndexPair[0]:
                        minDistanceIndexPair[0] = euclideanDistanceSquared((x,y), ijToxy(i,j))
                        minDistanceIndexPair[1] = (i,j)
            return(ijToxy(*minDistanceIndexPair[1]))
        else:
            return (x,y)

'''
testObj = Geolocate('0df011b3334448e8ae04f411333105e2')
testCoordinate = (86.9250, 27.9881)

print('On land?: ' + str(testObj.isLand(*testCoordinate)))
oceanCoordinate = testObj.findClosestOcean(*testCoordinate)
print('Nearest Ocean Coordinates: ' + str(oceanCoordinate))
testObj.getMap(viewGraph=True, points=[testCoordinate, oceanCoordinate])
'''
