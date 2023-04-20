from login.models import *
import face_recognition
from django.shortcuts import render,redirect
from login.models import *
from django.contrib.auth.models import User ,auth 
import cv2
import numpy as np
from collections import defaultdict
import os
import datetime
from django.utils import timezone
from django.http import JsonResponse
from base64 import b64decode
from PIL import Image
import io
video_capture = cv2.VideoCapture(0)
def def_value():
    return 0
cost=defaultdict(def_value)
cost = {'station1Etostation2X':20, 'station2Etostation1X':20,'station1Etostation1X':10, 'station2Etostation2X':10,
        }
# Load a sample picture and learn how to recognize it.
passen=passenger.objects.all()
encodings=[]
passenger_name=[]
passenger_user=[]
for passe in passen:
    image=face_recognition.load_image_file(passe.photo)
    encodings.append(face_recognition.face_encodings(image)[0])
    passenger_name.append(passe.user_name)
    passenger_user.append(passe.user)

def upload(request):
    if request.method == 'POST' and request.FILES.get('image'):
        file = request.FILES['image']
        cam_name=request.user.username
        #print(station_name)
        img = Image.open(io.BytesIO(file.read()))
        # img.show()
        image_np=np.array(img.convert('RGB'))
        myName="capturing"
        mySec="User"
        stat="e"
        face_locations = face_recognition.face_locations(image_np)
        if(face_locations!=[]):
            encoding=face_recognition.face_encodings(image_np,face_locations)[0]
            matches = face_recognition.compare_faces(encodings, encoding)
            name = "capturing"
            face_encoding = []
            face_names = []
            face_distances = face_recognition.face_distance(encodings, encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                    name = passenger_name[best_match_index]
                    myName=name
                    print(cam_name)
                    print(passenger_user[best_match_index].passenger.last_visited_station)
                    print(passenger_user[best_match_index].passenger.status)
                    if(passenger_user[best_match_index].passenger.last_visited_station!=cam_name):
                        if(passenger_user[best_match_index].passenger.status=="NOT Travelling"):
                            if passenger_user[best_match_index].passenger.balance <20:
                                   myName = "nobal"
                                   mySec=name
                            else:
                                passenger_user[best_match_index].passenger.status="Travelling"
                                passenger_user[best_match_index].passenger.last_visited_station=cam_name
                                j=journey(user=passenger_user[best_match_index],entry_location=cam_name[0:8],entry_time=timezone.now(),exit_time=timezone.now(),
                                        exit_location="-",fare=0)
                                j.save()
                            # passenger_user[best_match_index].passenger.status="Travelling"
                            # passenger_user[best_match_index].passenger.last_visited_station=cam_name
                            # j=journey(user=passenger_user[best_match_index],entry_location=cam_name[0:8],entry_time=timezone.now(),exit_time=timezone.now(),
                            #           exit_location="-",fare=0)
                            # j.save()
                        else:
                            stat="x"
                            jo=passenger_user[best_match_index].passenger.last_visited_station+'to'+cam_name
                            passenger_user[best_match_index].passenger.balance-=cost[jo]
                            passenger_user[best_match_index].passenger.status="NOT Travelling"
                            passenger_user[best_match_index].passenger.last_visited_station=cam_name
                            j=journey.objects.filter(user=passenger_user[best_match_index],exit_location="-")
                            j.update(exit_time=timezone.now(),exit_location=cam_name[0:8],fare=cost[jo])
                        passenger_user[best_match_index].passenger.save()
            else:
                myName="unknown"
            face_distances = face_recognition.face_distance(encodings, encoding)
            face_match_percentage = (1-face_distances[0])*100
            print (np.round(face_match_percentage,4))
        r={'name':myName , 'sec':mySec,'stat':stat}
        print(r)
        return JsonResponse(r)
    return render(request,'adminCamera.html') 
    
def signup(request):
     if request.method=="POST":
          username=request.POST['username']
          firstname=request.POST['firstname']
          last_name=request.POST['lasttname']
          email=request.POST['email']
          sex=request.POST['sex']
          password=request.POST['password']
          image=request.FILES['photo']
          age=request.POST['age']
          phone=request.POST['phone']
          aadhar=request.POST['aadhar']
          place=request.POST['place']
          last_vistied_station=place
          user=User.objects.create_user(username=username,email=email,password=password)
          i=passenger(user_name=firstname,last_name=last_name,photo=image,sex=sex,status="NOT Travelling",balance=0,password=password,user=user,
                      age=age,phone=phone,aadhar=aadhar,place=place,last_visited_station=last_vistied_station)
          i.save()
          img=face_recognition.load_image_file(i.photo)
          encodings.append(face_recognition.face_encodings(img)[0])
          passenger_name.append(i.user_name)
          passenger_user.append(i.user)
          return redirect('/home')
     return render(request,'adminHome.html') 
# def sample(request):
# # Initialize some variables
#  face_locations = []
#  face_encodings = []
#  face_names = []
#  process_this_frame = True

#  while True:
#     # Grab a single frame of video
#     ret, frame = video_capture.read()

#     # Only process every other frame of video to save time
#     if process_this_frame:
#         # Resize frame of video to 1/4 size for faster face recognition processing
#         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#         rgb_small_frame = small_frame[:, :, ::-1]
        
#         # Find all the faces and face encodings in the current frame of video
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

#         face_names = []
#         for face_encoding in face_encodings:
#             # See if the face is a match for the known face(s)
#             matches = face_recognition.compare_faces(encodings, face_encoding)
#             name = "Unknown"

#             # # If a match was found in known_face_encodings, just use the first one.
#             # if True in matches:
#             #     first_match_index = matches.index(True)
#             #     name = known_face_names[first_match_index]

#             # Or instead, use the known face with the smallest distance to the new face
#             face_distances = face_recognition.face_distance(encodings, face_encoding)
#             best_match_index = np.argmin(face_distances)
#             if matches[best_match_index]:
#                 name = passenger_name[best_match_index]

#             face_names.append(name)

#     process_this_frame = not process_this_frame


#     # Display the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Draw a label with a name below the face
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#     # Display the resulting image
#     cv2.imshow('Video', frame)

#     # Hit 'q' on the keyboard to quit!
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#  # Release handle to the webcam
#  video_capture.release()
#  cv2.destroyAllWindows()