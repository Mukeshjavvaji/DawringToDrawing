import json
from django.shortcuts import render
import pyautogui
from django.conf import settings
import cv2
import tensorflow as tf
import numpy as np
import json

# Create your views here.


def index(request):
    images = {1: 'Representations/white.jpg', 2: 'Representations/white.jpg', 3: 'Representations/white.jpg',
              4: 'Representations/white.jpg', 5: 'Representations/white.jpg', 6: 'Representations/white.jpg'}
    return render(request, 'index.html', {'predictions': images})


def predict(request):
    if request.method == "POST":
        ss = pyautogui.screenshot(region=(130, 260, 650, 650))
        img = 'myimg.png'
        resized_img = ss.resize((28, 28))
        resized_img.save(settings.STATICFILES_DIRS[0]/img)
        path = settings.STATICFILES_DIRS[0]/img
        im = cv2.imread(str(path))
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im_gray = np.array(im_gray)
        im_gray = im_gray.astype(np.float32)
        im_gray = im_gray.reshape((-1, 28, 28, 1))
        model = tf.keras.models.load_model(
            './whiteboard/models/models/model_20220814-115719/')
        prediction = model([im_gray])
        f = open(
            './whiteboard/models/labels.json')
        labels = json.load(f)
        predictions = np.argsort(prediction)
        predictions = predictions.reshape(-1)
        predictions = predictions[-6:]
        predictions = predictions[::-1]
        images = {}
        c = 1
        for i in predictions:
            path = 'Representations/'+str(labels[str(i)])+".jpg"
            images[c] = path
            c += 1
        print(images)

        return render(request, 'index.html', {'predictions': images})
