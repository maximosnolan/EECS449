#! /usr/bin/python3

import face_recognition as facRec
import os


# Define paths

imagePath = "./images/"
testImagePath = "./testImages/"

encodingList = dict()


# Parse all images w.r.t path
def performImageParsing(imagePath):
    dir_list = os.listdir(imagePath)
    for image in dir_list:
        print("Encoding image " + image)
        picture = facRec.load_image_file(imagePath + image)
        encodedPicture = facRec.face_encodings(picture)
        if len(encodedPicture) == 0:
            print("ERROR: Unable to process face for image {}".format(image))
        else:
            encodingList[image] = encodedPicture[0]


def determineMatch(encodedImageIn):
    print("STARTING: matching process with {} Images".format(len(encodingList)))
    for imageName, encodedPic in encodingList.items():
        result = facRec.compare_faces([encodedPic], encodedImageIn)
        print(result)
        print("Seeing if this person is {}".format(imageName))
        if len(result) == 0:
            print("ERROR")
        elif result[0] == True:
            print("This person is " + imageName)
            return


def parseTestImage(imageName):
    testImage = facRec.load_image_file(testImagePath + imageName)
    encodedImageIn = facRec.face_encodings(testImage)
    if len(encodedImageIn) == 0:
        return nil
    return encodedImageIn[0]


def main():
    performImageParsing(imagePath)
    encodedImageIn = parseTestImage("maximostest1.jpg")
    determineMatch(encodedImageIn)
    return

if __name__ == "__main__":
    main()
