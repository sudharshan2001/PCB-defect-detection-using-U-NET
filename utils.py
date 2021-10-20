import cv2
import glob
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm 
import os 
import pickle
from PIL import Image
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from tensorflow.keras.models import  load_model

path = './'
image_path = os.path.join(path, 'VOC_PCB/JPEGImages') # Path to each images
annotate_path = os.path.join(path, 'VOC_PCB/Annotations') # Path to the Annotations

# mapping each defects to a certain number
def mapping(x):
    if x =='missing_hole':
        return 1
    elif x == 'mouse_bite':
        return 2
    elif x == 'open_circuit':
        return 3
    elif x == 'short':
        return 4
    elif x == 'spurious_copper':
        return 5
    elif x == 'spur':
        return 6


total_xml_list = [] #Used to store the info parsed from xml file
i=0
# Iterating through directories 
for i in sorted(os.listdir(annotate_path)):
    xml_doc = annotate_path +f'/{i}'
    # Array to store all bounding box details in a file temporarily 
    xml_list=[]
    tree = ET.parse(xml_doc)
    root = tree.getroot()
    # Iterating throught all the object in the xml file
    for member in root.findall('object'):
        value=[
               int(member[4][0].text), #To find xmin
               int(member[4][1].text), #To find ymin
               int(member[4][2].text), #To find xmax
               int(member[4][3].text), #To find ymax
               mapping(member[0].text) #To find Name of it and mapping it to a number
               ]

        xml_list.append(value)
    total_xml_list.append(xml_list)


# Converting image into grayscale, resizing it to 128X128 and storing it in an array
bbox_for_all_image = []
for img_path in tqdm(sorted(os.listdir(image_path)),total=len(os.listdir(image_path))):
    img = cv2.imread(os.path.join(image_path,img_path), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img,(128,128)) #resizing 
    bbox_for_all_image.append(img)


boxarr = [] # Used to store the Bounding Box image
# iterating through the total_xml_list
for i in tqdm(range(len(total_xml_list))): 
    # Creating a 600X600 image (zero for black color)
    narr = np.zeros((600,600,1)) 
    # iterating thorugh the i-th file in total_xml_list 
    for j in range(len(total_xml_list[i])): 
        # Getting annotations for bounding box from the j-th array
        x1,y1,x2,y2,d = total_xml_list[i][j]
        # Using the annotation to draw on the blank image we created earlier
        narr = cv2.rectangle(narr,(x1,y1),(x2,y2),d,-1)
    # Ressizing it to 128X128 to feed it to the model
    narr = cv2.resize(narr,(128,128))
    boxarr.append(narr)
boxarr = np.array(boxarr)