import face_recognition
import cv2
import os
import numpy as np

def get_face_encodings(image, path=False):
    if path:
        image = face_recognition.load_image_file(image)
        my_face_encoding = face_recognition.face_encodings(image)[0]
        return my_face_encoding

#my_image = face_recognition.load_image_file("ashish.jpg")
#my_face_encoding = face_recognition.face_encodings(my_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = []
known_face_names = []
for i in os.listdir('known_faces'):
	if i.endswith('.jpg') or i.endswith('.png'):
		name = i.split('.')[0]
		encoding = get_face_encodings(os.path.join('known_faces', i), path=True)
		#print(len(encoding))
		known_face_names.append(name)
		known_face_encodings.append(encoding)
'''
print("Done")
print(len(known_face_encodings))
print(known_face_names)
'''
print([i.shape for i in known_face_encodings])
face_locations = []
face_encodings = []
face_names = []
process_this_frame = 0

video_capture=cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    frame=cv2.flip(frame,1)

    small_frame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame%20==0:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        #print

        face_names = []
        for face_encoding in face_encodings:
            #print(type(face_encoding))
            
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            #print(matches)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            else:
                text = input('Unknown face would you like to add this into known faces? ')
                if text.startswith('y'):
                    name = input('What is the name of this person: ')
                    encoding = get_face_encodings(small_frame)
                    known_face_encodings.append(encoding)
                    known_face_names.append(name)
                    path = os.path.join('known_faces', name+'.jpg')
                    cv2.imwrite(path, small_frame)
            face_names.append(name)
                    
    process_this_frame = process_this_frame+1
    for (top, left, bottom, right), name in zip (face_locations, face_names ):
        top *= 2
        left *= 2
        bottom *= 2
        right *= 2

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0,255), 2)
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (right+6, bottom-6), font, 0.75, (255, 255, 255), 1)

	
	
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()





    
