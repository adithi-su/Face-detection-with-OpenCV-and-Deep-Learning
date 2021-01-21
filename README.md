# Face-detection-with-OpenCV-and-Deep-Learning

<h4>Install necessary packages:</h4>
 <ol>
   <li> sudo pip install opencv-contrib-python </li>
   <li>(preferably use virtualenv)
   virtualenv cv
   source cv/bin/activate
      pip install opencv-contrib-python   </li>
   <li> pip install imutils </li>
 </ol>

<h4>Contents:</h4>
1. Apply face detection with OpenCV to single images (detect_faces.py)

To execute it, run this command in the terminal:
python detect_faces.py --image people.jpg --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

2. Apply face detection to video, video streams, and webcams (detect_faces_video.py)

To execute it, run this command in the terminal:
python detect_faces_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel
