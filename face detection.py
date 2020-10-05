

         import cv2         


                                                                                              #importing the library
  address = r"c:/users/saicharan/Desktop/haarcascade_frontalface_default.xml"


         classifier = cv2.CascadeClassifier(address)



   cap = cv2.VideoCapture(0)                                                                                                       #setting the web camera

   while True:                                                                                                            #starting the loop
       ret,frame = cap.read()                                                                                                       #reading the frames
    
   
    
   
    bb = classifier.detectMultiScale(frame,1.2,4)                                                                                                       #detecting the faces
    
       
    for (x,y,w,h) in bb:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,225,225),2)                                                                                                        #drawing the boundary boxes
        cv2.imshow('detected',frame)
        
    if cv2.waitKey(1) == ord('q'):                                                                                                        #ending the loop
        break
    
    cap.release()                                                                                                             #releasing the camera
    cv2.destroyAllWindows() 






                                                                                                      #closing all the windows