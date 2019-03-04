import cv2

#img diff function
def diffimg(a,b,c):

    #Calculates the per-element absolute difference
    #between two arrays or between an array and a scalar.

    t0 =cv2.absdiff(a,b)
    t1 =cv2.absdiff(b,c)

    #and = 1 when 1&1 rest =0
    #Calculates the per-element bit-wise
    #conjunction of two arrays or an array and a scalar.

    t3 =cv2.bitwise_and(t0,t1)
    return t3

    
cap=cv2.VideoCapture(0)
#capture from cam
t=cap.read()[1] #1st element in the array
tp=cap.read()[1]
tpp=cap.read()[1]

#recolour the captured img
t=cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
tp=cv2.cvtColor(tp,cv2.COLOR_BGR2GRAY)
tpp=cv2.cvtColor(tpp,cv2.COLOR_BGR2GRAY)

while True:

    img=diffimg(t,tp,tpp)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(img, "Motion has detected", (50,460), font, 1, (12,12,249), 2)
    
    cv2.imshow("motion Detect", img)

    res,img = cap.read()
    t=tp
    tp=tpp
    tpp=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    key = cv2.waitKey(10)

    if key ==27:
        cv2.destroyAllWindows()
        break


cv2.destroyAllWindows()
cap.release()"    
        
