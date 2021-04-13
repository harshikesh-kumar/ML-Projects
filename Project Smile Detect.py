import cv2
smilecascade=cv2.CascadeClassifier('haarcascade\\haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img=cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smiles = smilecascade.detectMultiScale(img, 1.3,50 )

    for (x,y,w,h) in smiles:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 2)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
