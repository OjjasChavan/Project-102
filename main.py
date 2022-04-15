from os import access
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_pic():
    number = random.randint(1, 100)
    image = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = image.read()
        image_name = "img" + str(number) + ".jpg"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("Image saved")

    image.release()
    cv2.destroyAllWindows()

take_pic()

def upload_image(image_name):
    access_token = "sl.BFyKsytnRaEt1YPG-wzL-s4yb1u1nl7nPy8aOIPUrVy83HQ_p-3GPu3ePTuJCVCQ8dDjCEf3j1WJKBkGmJbXGaWDOveEmWfRvkzrm2K-0oUlafU8HzBbocy_1wXx2L_XcosjZ2Y"
    file = image_name
    file_from = file
    file_to = "/" + file
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded!")

def main(): 
    while(True):
        if ((time.time() - start_time) >= 5):
            image_name = take_pic()
            name = take_pic()
            upload_image(image_name)