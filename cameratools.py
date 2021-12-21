import numpy as np
import face_recognition as fr
import cv2
import glob

def log_new_face():
    video_capture = cv2.VideoCapture(0)
    directory = "faces\\"
    print("What is the name you would like to see?")
    name = input("Write here:")
    print("Press 'k' to take a picture of yourself!")
    print("Make sure you're the only person in the scene, and please center yourself!")
    while True:
        ret, frame = video_capture.read()
        cv2.imshow("Sample Output", frame)
        if cv2.waitKey(1) & 0xFF == ord('k'):
            cv2.imwrite(directory + str(name) + '.png', frame)
            break

    del video_capture
    print("Picture taken!")

def get_faces_from_file():
    faces = glob.glob(R"faces\*.png")
    known_face_names = []
    known_face_encodings = []
    for face in faces:
        image = fr.load_image_file(face)
        face_encoding = fr.face_encodings(image)[0]

        known_face_encodings.append(face_encoding)
        known_face_names.append(str(face.split('.')[0].split("\\")[1]))

    return known_face_names, known_face_encodings

def get_live_face_readings():
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    known_face_names, known_face_encodings = get_faces_from_file()
    while True: 
        ret, frame = video_capture.read()

        rgb_frame = frame[:, :, ::-1]

        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = fr.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            face_distances = fr.face_distance(known_face_encodings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('[OUTPUT]:', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # log_new_face()
    get_live_face_readings()
