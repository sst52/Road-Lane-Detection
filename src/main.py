import cv2

if __name__ == "__main":
    testing_image = cv2.imread("RoadImage.jpg")
    cv2.imshow("Image", testing_image)
    cv2.waitKey(0)
