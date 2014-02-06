import os
import cv

__all__ = ['findboobs']

rel = lambda *p: os.path.join(os.path.dirname(__file__), *p)

def findboobs(image_path):
    hc = cv.Load(rel('res/data.xml'))
    img = cv.LoadImage(image_path)

    coords = []
    for [x, y, w, h], n in cv.HaarDetectObjects(img, hc, cv.CreateMemStorage()):
        coords.append([x, y, x + w, y + h])

    return coords

