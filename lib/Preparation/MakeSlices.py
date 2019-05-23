import numpy as np
import pyautogui
import imutils
import cv2
import image_slicer

# take a screenshot of the screen and store it in memory, then
# convert the PIL/Pillow image to an OpenCV compatible NumPy array
# and finally write the image to disk
def getSlices():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    template = cv2.imread('templates/fieldTemplate.png')
    print(image)
    # Convert to grayscale
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Find template
    result = cv2.matchTemplate(imageGray,templateGray, cv2.TM_CCOEFF)
    print(result)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h,w = templateGray.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)
    roi = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    cv2.imwrite("tmp/croppedField.png", roi)
    image_slicer.slice('tmp/croppedField.png', 6)
