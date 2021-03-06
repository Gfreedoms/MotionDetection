import numpy as np
import cv2
import argparse
import datetime
import time
import pygame
import imutils
import warnings
from imutils.object_detection import non_max_suppression
from imutils import paths
import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
#from urllib.request import urlopen
from urllib2 import urlopen
import urllib
import base64
from twilio.rest import Client

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

args = vars(ap.parse_args())

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

camera = cv2.VideoCapture(0)
#camera.set(cv2.CV_CAP_PROP_FPS, 1)
time.sleep(0.25)

avg_frame = None
count = 0
#lastUploaded = datetime.datetime.now()
motionCounter = 0
#first_frame = None

while(camera.isOpened()):
    #frame = np.array
    timestamp = datetime.datetime.now()
    (grabbed, frame) = camera.read()
    text = ""

    if grabbed == False:
        break

    #resize, gray and blur
    resize_frame = imutils.resize(frame, width=500)
    gray_frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if avg_frame is None:
        avg_frame = blur_frame.copy().astype("float")
        continue

    cv2.accumulateWeighted(blur_frame, avg_frame, 0.5)
    frameDelta = cv2.absdiff(blur_frame, cv2.convertScaleAbs(avg_frame))

   
    thresh_frame = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # dilate image and find contours
    erosion = cv2.erode(thresh_frame, None, iterations=1)
    dilate_frame = cv2.dilate(erosion, None, iterations=2)
    (_, contours, _) = cv2.findContours(thresh_frame.copy(),
                                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #contours = contours[0] if imutils.is_cv2() else contours[1]

    for cont in contours:
        if cv2.contourArea(cont) < 100:
            continue

        # compute the bounding box for the contour
        #(x, y, w, h) = cv2.boundingRect(cont)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Motion detected"

    cv2.putText(frame, "WEATHER STATION STATUS: {}".format(text), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    if text == "Motion detected":
        for motion in text:
            motionCounter += 1

            if motionCounter >= 8:
                #print(frame)
                image = "image%d.jpg" %count
                # Conrad, you could do a little preprocessing on "image"
                file = "dummydata/"+image
                cv2.imwrite(file, frame)

            count += 1

        motionCounter = 0
    else:
        motionCounter = 0
           
    filename = "*.jpg"
    path = "dummydata/"+filename
    images = glob.iglob(path)
    for img in images:
        image1 = cv2.imread(img)
        image1 = imutils.resize(image1, width=min(400, image1.shape[1]))
        init_image = image1.copy()

        (rects, weights) = hog.detectMultiScale(
            image1, winStride=(4, 4), padding=(8, 8), scale=1.05)

        for (x, y, w, h) in rects:
            cv2.rectangle(init_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image1, (xA, yA), (xB, yB), (0, 255, 0), 2)
        #cv2.imshow("After NMS", image1)

        if np.any(pick):
            image = os.path.basename(img)
            file = "captured/"+image
            cv2.imwrite(file, image1)
	        
            print("something")    
            try:
                urlopen("https://www.google.com").close()
            except urllib.error.URLError:
                print("internet Not Connected")
                time.sleep(5)
            else:
                print("internet Connected")
                from_addr = "weatherstationsecure@gmail.com"
                to_addr = "weatherstationsecure@gmail.com"

                msg = MIMEMultipart()
                msg['From'] = from_addr
                msg['To'] = to_addr
                msg['Subject'] = "WEATHER STATION INTRUSION NOTIFICATION."

                body = "There has been intrusion detected at the weather station"

                msg.attach(MIMEText(body, 'plain'))

                filename = os.path.basename(img)
                attachment = open("captured/"+filename, "rb")

                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(from_addr, "W1meaict.")
                text = msg.as_string()
                        server.sendmail(from_addr, to_addr, text)
                print("email notification sent")
                        server.quit()
                pygame.mixer.init()
                print("alarm triggered")
                pygame.mixer.music.load("surrender.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.mixer.music.load("armed.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.mixer.music.load("Siren.wav")
                pygame.mixer.music.play()
                time.sleep(5)
                # Play the sounds; these will play simultaneously

                while pygame.mixer.music.get_busy()==True:
                    continue
                
                account = "AC98a70f689d74961cf681d59f16842ddc"
                token = "72996ebbf858d6ce02e6eec18c1abaf8"
                client = Client(account, token)
                message = client.messages.create(to="+256790870109", from_="+15172367545",
                                        body="Hello there this is the integrated version. cheers!")
                print("SMS notification sent")

        else:
            #print("nothing")
            #os.remove(img)
            continue
           
    #cv2.imshow("Security Feed", frame)
    #cv2.imshow("Frame Delta", frameDelta)
    #cv2.imshow("Thresh", thresh_frame)
    #cv2.imshow("gray", gray_frame)
    #cv2.imshow("blur", blur_frame)
    #cv2.imshow("dila", dilate_frame)
    #cv2.imshow("ero", erosion)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    os.remove(img)
for image_in_captured in glob.iglob("captured/*.jpg"):
    os.remove(image_in_captured)
    print("deleting temporarly stored images")
# Release everything if job is finished
camera.release()
cv2.destroyAllWindows()
quit()
