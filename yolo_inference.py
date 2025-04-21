from ultralytics import YOLO

# model = YOLO('models/best.pt')

# result = model.predict('./input_videos/image.png', save=True)
# result = model.predict('./input_videos/input_video.mp4',conf = 0.25, save=True)
# print(result)
# print ('boxes')
# for box in result[0].boxes:
#     print(box)

#for tracking the objects in the video

model = YOLO('yolov8x')

result = model.track('./input_videos/image.png', save=True)
result = model.track('./input_videos/input_video.mp4',conf = 0.25, save=True)
# print(result)
# print ('boxes')
# for box in result[0].boxes:
#     print(box)