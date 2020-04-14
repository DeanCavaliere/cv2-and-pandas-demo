import cv2
import pandas as pd
import util as util

# Pull in the data from the csv files
data = pd.read_csv("./data/output_0.csv")
siz = len(data['image'])

# Bring in some extra cool pictures
#blueshell = cv2.imread('./blueshell2.png')
#mario = cv2.imread('./mario.png')

for i in range(1, siz-1):

    print('Servo Data ' + str(data['servo'][i]), '   Motor Data:' + str(data['motor'][i]))

    hold = cv2.imread(data['image'][i])

    # Resize the image to 640 x 320
    img = cv2.resize(hold, (int(640), int(320)))

    # Merge some pictures
    # img = cv2.addWeighted(img, 0.7, blueshell, 0.7, 0)
    # img = cv2.addWeighted(img, 0.7, mario, 0.7, 0)

    # Set Start and end point
    start_pt = (150, 300)
    end_x = int((data['servo'][i]) * 1000)
    end_pt = (end_x, 200)

    # Define some line properties
    color = (0, 0, 255)  # corona red
    thicc = 5

    # Make the line
    cv2.line(img, start_pt, end_pt, color, thicc)

    # Set up the text
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    fontScale = 2
    colorT = (69, 255, 69)
    start_ptT = (95, 300)
    cv2.putText(img, str(data['servo'][i]), start_ptT, font, fontScale, colorT, thicc)

    # Output the image
    image = cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()