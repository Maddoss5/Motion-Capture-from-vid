# Motion-Capture-from-vid
Grabs the human body  movement from a given video and creates a 33 node animation based on that 

# Libraries required
OpenCv

# Functioning
Program takes a video detect the human movement from it and places landmarks on it . There are 33 landmarks based on this image 

Full body landmarks
![pose_tracking_full_body_landmarks](https://user-images.githubusercontent.com/111579172/185634733-cc702089-e2c7-498e-8ff4-f3485dc346be.png)

When running the video it detects these landmarks and how they move and we capture these landmarks and export it to a text file .
These landmarks are nodes in a 3d animation software . If no landmark is detected we just skip it . 

Program detecting the landmarks 
![Screenshot (8)](https://user-images.githubusercontent.com/111579172/185634994-e778a207-573d-4f99-9f22-d9a425fd51c0.png)

After writing the file for animation , we use a function of 33 variables in script for software like blender/maya/unreal engine/unity etc. Note- Some softwares take Y axis from top to bottom and others bottom to top .


The python script for these 3d animation software should be fairly easy and should follow-

$x$=getnodelocation(node number y)

nodelocation for y= $x$ 
