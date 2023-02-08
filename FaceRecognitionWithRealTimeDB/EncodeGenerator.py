import cv2
import face_recognition
import pickle
import os

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0]) #splitting extension from image
    #fileName = f'{folderPath}/{path}'
    #bucket = storage.bucket()
    #blob = bucket.blob(fileName)
    #blob.upload_from_filename(fileName)
    #print(len(imgList))

print(studentIds)

#generating encoding
def findEncodings(imagesList):
    encodeList = []
    #loop through every image and generate encoding
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
# print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown, studentIds] #saving encoding with ids
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")