import pandas as pd
import os
import cv2
from datetime import datetime
import time

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

#GET CURRENT DIRECTORY PATH
myDirectory = os.path.join(os.getcwd(), 'DataCollected')
print(myDirectory)

# CREATE A NEW FOLDER BASED ON THE PREVIOUS FOLDER COUNT
while os.path.exists(os.path.join(myDirectory,"IMG{str(countFolder)}")):
        countFolder += 1
newPath = myDirectory +"/IMG"+str(countFolder)
os.makedirs(newPath)

# SAVE IMAGES IN THE FOLDER
def saveData(img,steering):
    global imgList, steeringList
    now = datetime.now()
    timestamp =  str(time.mktime(now.timetuple()) + now.microsecond/1e6)
    #print("timestamp =", timestamp)
    fileName = os.path.join(newPath,"Image_ %s .jpg" %(timestamp))
    cv2.imwrite(fileName, img)
    imgList.append(fileName)
    steeringList.append(steering)

# SAVE LOG FILE WHEN THE SESSION ENDS
def saveLog():
    global imgList, steeringList
    rawData = {'Image': imgList,
                'Steering': steeringList}
    df = pd.DataFrame(rawData)
    df.to_csv(os.path.join(myDirectory,"log_ %s .csv" %(str(countFolder))), index=False, header=False)
    print('Log Saved')
    print('Total Images: ',len(imgList))

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    for x in range(10):
        _, img = cap.read()
        saveData(img, 0.5)
        cv2.waitKey(1)
        cv2.imshow("Image", img)
    saveLog()
