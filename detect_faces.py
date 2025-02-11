import numpy as np
import argparse
import cv2

#argument parse 
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
ap.add_argument("-p","--prototxt",required=True,help="path to Caffe 'deploy' prototxt file") #.prototxt file(s) define the model architecture(i.e the layers themselves)
ap.add_argument("-m","--model",required=True,help="path to Caffe pre-trained model") #.caffemodel file contains the weight for ths actual layers
ap.add_argument("-c","--confidence",type=float,default=0.5,help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# Caffe is a deep learning framework made with expression, speed, and modularity in mind. OpenCV supports Caffe
# Blob is a library for computer vision to detect connected regions in binary digital images. 
# in simple terms, a blob is just a (potential collection) of image(s) with the same spatial dimensions (i.e., width and height), same depth(number of channels), that have all been preprocessed in the same manner.
# dnn - openCV's deep neural network module

# load serailized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# load the input image and construct an input blob for the image by resizing to a fixed 300x300 pixels and then normalizing
image = cv2.imread(args["image"])
(h,w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)), 1.0, (300,300), (104.0,177.0,123.0) )
# dnn.bolbFromImage takes care of preprocessing which includes setting blob dimensions and normalization.
# dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB = True )  
# mean in this case is  3-tuple RGB 

# pass the blob through the network and obtain the detections and predictions
print("[INFO computing object detections...")
net.setInput(blob)
detections = net.forward()

# loop over detections 
for i in range(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated with the prediction
    confidence = detections[0, 0, i, 2]

    #filter out weak detections by ensuring the confidence is greater than the minimum confidence
    if confidence > args["confidence"]:       
        # compute the (x,y) coordinates of the bounding box for the object 
        box  = detections[0, 0, i, 3:7] * np.array( [w,h,w,h] )
        (startX, startY, endX, endY) = box.astype("int")

        # draw the bounding box of the face along with associated probability 
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY-10 > 10 else startY+10
        cv2.rectangle(image, (startX, startY), (endX, endY), (0,0,255), 2)
        cv2.putText(image, text, (startX,y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0,0,255), 2)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
