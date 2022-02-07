from object_tracker import object_tracker

classes_count_dict = object_tracker(video = "data/video/Secuencia 01_1.mp4", output = "outputs/demo.avi", score = 0.9)
print(classes_count_dict)