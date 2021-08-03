import cv2

camera = cv2.VideoCapture(0)
for i in range(15):
    return_value, image = camera.read()
    print(return_value, image.shape)
    cv2.imwrite('iloveyou'+str(i)+'.jpg', image)
del(camera)