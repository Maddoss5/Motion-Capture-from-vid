import cv2

from cvzone.PoseModule import  PoseDetector

cap=cv2.VideoCapture('cm1.mp4')



detector= PoseDetector()



f1 = open('animation.txt', 'w')

frames =0
totframes=0
while True:
    success, img= cap.read()
    if success:
        totframes=totframes+1
        img=detector.findPose(img)
        land,boxinfo=detector.findPosition(img)



        if boxinfo:
            for ha in land:
                f1.write(str(ha[1]))
                f1.write(",")
                f1.write(str(img.shape[0]-ha[2]))
                f1.write(",")
                f1.write(str(ha[3]))
                f1.write(",")
            frames=frames+1




        cv2.imshow("Image",img)
        cv2.waitKey(1)
    else:
        break


f1.close()
print("Total frames captured are ",frames)
print("Total frames in the video are ",totframes)
