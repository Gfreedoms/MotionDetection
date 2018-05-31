import cv2
import datetime
import imutils
import os
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
from urllib.request import urlopen
import urllib
import time
import base64

status = "on"
while True:
    if status == "on":
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        lastUploaded = datetime.datetime.now()
        filename = "*.jpg"
        path = "dummydata/"+filename
        images = glob.iglob(path)

        for img in images:
            timestamp = datetime.datetime.now()
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
            
            '''if (timestamp - lastUploaded).seconds >= 120.0:
                if np.any(pick):
                    image = os.path.basename(img)
                    file = "captured/"+image
                    cv2.imwrite(file, image1)
                    print("something")    
                    try:
                        urlopen("http://www.google.com").close()
                    except urllib.error.URLError:
                        print("Not Connected")
                        time.sleep(5)
                    else:
                        print("Connected")
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
                        server.quit()

                else:
                    print("nothing")
                    os.remove(img)
                    continue'''

            cv2.imshow("After NMS", image1)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            #os.remove(img)
        for image_in_captured in glob.iglob("captured/*.jpg"):
            os.remove(image_in_captured)
    else:
        continue
cv2.destroyAllWindows()
