import cv2,os

video_path=input("Video Yolu : ")
vidcap = cv2.VideoCapture(video_path)               
shutter = int(input("Kaç Framede bir resim alacaksiniz? :")) 

success,image = vidcap.read()
count = 0
success = True

if os.path.isdir("jpgs"):
  pass
else:
  os.mkdir("jpgs")

while success:
  success,image = vidcap.read()
  if count % shutter == 0:
    cv2.imwrite("jpgs/frame%d.jpg" % count, image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                          # exit if Escape is hit
          break
  count += 1
print("finished")
#test