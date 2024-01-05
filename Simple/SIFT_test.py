import cv2

# 传入要辨别的照片
image = cv2.imread(r"C:\Users\20995\Desktop\cat.jpg", cv2.IMREAD_GRAYSCALE)

#创建一个SIFT的项目
sift = cv2.SIFT_create()

#检测关键的点
keypoints, descriptors = sift.detectAndCompute(image, None)

# 把这些关键点画在图上
output_image = cv2.drawKeypoints(image, keypoints, None)

# 将图片呈现出来
cv2.imshow('SIFT Keypoints', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
