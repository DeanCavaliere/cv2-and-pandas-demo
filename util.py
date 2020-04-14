import cv2

def showImage(imgfile, motor, servo):
    print('Servo Data '+ str(servo), '   Motor Data:'+ str(motor))

    hold = cv2.imread(imgfile)
    # Resize the image to 640 x 320
    img = cv2.resize(hold, (int(640), int(320)))

    # Set Start and end point
    start_pt = (150, 300)
    end_x = int((servo)*1000)
    end_pt = (end_x, 200)

    # Define some line properties
    color = (0, 0, 255) # corona red
    thicc = 5

    # Make the line
    cv2.line(img, start_pt, end_pt, color, thicc)

    # Set up the text
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    fontScale = 2
    colorT = (69, 255, 69)
    start_ptT = (95,300)
    cv2.putText(img, str(servo), start_ptT, font, fontScale, colorT, thicc)

    # Output the image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()