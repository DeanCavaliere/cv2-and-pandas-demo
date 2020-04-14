import cv2
import pandas as pd
import util as util

# Pull in the data from the csv files
data = pd.read_csv("./data/output_0.csv")
siz = len(data['image'])

for i in range(1, siz-1):
    util.showImage(data['image'][i], data['motor'][i], data['servo'][i])
