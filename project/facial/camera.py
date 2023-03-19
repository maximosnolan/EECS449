import cv2
import keyboard
import os


def getCapture(im_num):
    """
    Captures an image on the computer's camera
    :param      im_num: Path to the image to encode
    :return:
    """
    cam = cv2.VideoCapture()
    result, image = cam.read()

    if result:
        cv2.imshow("temp", image)
  
        # saving image in local storage
        cv2.imwrite("temp_{}.png".format(im_num), image)

        # If keyboard interrupt occurs, destroy image 
        # window
        cv2.waitKey(0)
        cv2.destroyWindow("temp")
    else:
        print("No image available, camera has issues")


def main():
    """
    Driver for camera to run until exit command hit.
    :return:
    """
    im_num = 1
    while True:
        key_input = input("Press 'c' for capture, 'x' to exit")
        if key_input == 'c':
            getCapture(im_num)
            im_num += 1
        elif key_input == 'x':
            break
        else:
            print("Invalid!")

        

if __name__ == "__main__":
    main()