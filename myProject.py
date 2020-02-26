from magicwand import SelectionWindow
import cv2 as cv

img = cv.imread("image.jpg")
window = SelectionWindow(img)
window.show()


print(f"Selection mean: {window.mean[:, 0]}.")