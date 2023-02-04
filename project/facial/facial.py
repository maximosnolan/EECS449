import face_recognition
import os

imagePath = "./images/"
testImagePath = "./testImages/"
encodingList = dict()

def performImageParsing(imagePath):
    dir_list = os.listdir(imagePath)
    for image in dir_list:
        print("Encoding image " + image)
        picture = face_recognition.load_image_file(imagePath + image)
        encodedPicture = face_recognition.face_encodings(picture)
        if len(encodedPicture) == 0:
            print("ERROR: Unable to process face for image " + image)
        else:
            encodingList[image] = encodedPicture


def determineMatch(encodedImageIn):
    #encodedImageIn = face_recognition.load_image_file(imagePath + image)
    print("STARTING: matching process with {} Images".format(len(encodingList)))
    for imageName, encodedPic in encodingList.items():
        result = face_recognition.compare_faces([encodedPic], encodedImageIn)
        print(result)
        print("Seeing if this person is {}".format(imageName))
        if len(result) == 0:
            print("ERROR")
        elif result[0] == True:
            print("This person is " + imageName)
            return


def main():
    performImageParsing(imagePath)
    testImage = face_recognition.load_image_file(imagePath + "golfsteak0.jpg")
    encodedImageIn = face_recognition.face_encodings(testImage)[0]
    determineMatch(encodedImageIn)
    return






#if __name__ == "__main__":
#    main()



# picture = face_recognition.load_image_file(imagePath + "golfsteak0.jpg")
# my_face_encoding = face_recognition.face_encodings(picture)[0]

# unknownFace =  face_recognition.load_image_file(imagePath + "golfsteak2.jpg")
# print(face_recognition.face_encodings(unknownFace))
# unknown_face_encoding = face_recognition.face_encodings(unknownFace)[0]
# results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
# if results[0]:
#    print("SAME PERSON")
# else:
#    print("NOT SAME PERSON")
