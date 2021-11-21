from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras import models, layers
from keras.preprocessing.image import img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb
from PIL import Image
import numpy as np
import cv2
import shutil

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

model = models.load_model('bestmodel.h5')
def colorize(model, img1_color):
    output1 = model.predict(img1_color)
    output1=output1*128
    result = np.zeros((256,256,3))
    result[:,:,0] = img1_color[0][:,:,0]
    result[:,:,1:] = output1[0]
    img = lab2rgb(result)
    img_path2 = 'static/img2.jpg'
    im = Image.fromarray((img * 255).astype(np.uint8))
    im.save(img_path2)
    #cv2.imwrite(img_path,img)


@app.route('/')
def index():
	return render_template("index.html")


@app.route("/submit", methods=["POST"])
def prediction():
    img1_color=[]
    img=request.files['img']
    img_path1 = 'static/img1.jpg'
    img.save(img_path1)

    img = img_to_array(
        load_img(img_path1,target_size=(256,256,3))
    )/255

    img1_color.append(img)
    img1_color = rgb2lab(img1_color)[:,:,:,0]
    img1_color = img1_color.reshape(img1_color.shape+(1,))

    colorize(model, img1_color)

    #image=cv2.imread(img_path)
    return render_template("index.html", img_path1=img_path1, img_path2='static/img2.jpg')


if __name__ == "__main__":
	app.run(debug=True)
