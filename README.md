# ColorIt: Colorize B/W Images
Colorization of old black and white images nowadays is usually done manually by using popular photo editing software like Photoshop. This process is generally a very demanding job that requires extensive research to properly organize the layers of color and the proper shading of these images. This task is very tiring and can take a huge amount of time. However, with the help of various Deep Learning models, it is possible to gradually speed up and even automate this task, whilst producing results similar to those of a professional editor.

The input is given in the form of a black and white image and the output obtained are the 3 channels of the RGB components of the same black and white image. This is achieved with the help of Autoencoders.

In this project, I have developed an autoencoder that tries to recolorize the images present in the grayscale format.

The dataset of images used in this project, containing images of different art styles, can be viewed [here](https://www.kaggle.com/thedownhill/art-images-drawings-painting-sculpture-engraving/version/2). Apart from this, I have added more images from Google to the dataset to make the model more efficient and robust. In the proposed Autoencoder Architecture, there is an encoder and a decoder. The encoder has 8 convolution layers while the decoder has 5 convolution layers consisting of filters of different sizes. The model took around 5K seconds to train. The training accuracy is obtained to be 83.50%.

### Mobile Android Application
[Click here](https://youtu.be/iviUiaPFw7U) to watch the video.

### Web Application
[Click here](https://colorit-from-bnw.herokuapp.com/) to go to the website.

### Autoencoder Model Architecture
![Autoencoder Model](https://i.ibb.co/Wxjpg1R/1-nqz-Wupx-C60i-AH2d-Yr-FT78-Q.png "Autoencoder Model")

### Python Notebook
The .ipynb notebook can be accessed [here](https://nbviewer.org/github/lakkshh/ColorIt-Colorize-BW-Images/blob/master/ColorIt%20Color%20BW%20Photographs.ipynb).

### Novelty
There are a few re-coloring deep learning models which make use of Inception-Resnet-v2 pre-trained model for feature extraction or other highly complex mechanisms. I have tried to achieve the same using a comparitively simpler encoder-decoder architecture using the convolution layers only and obtain the same results as the other models. It is observed that the results obtained are quite good and can further improve if trained with an even larger dataset.

- Built the Autoencoder Architecture from scratch and Hyper-Parameter Tuning
    - Built the Autoencoder (Encoder-Decoder) architecture from scratch using trial and error for the number of convolution layers in the econder part and the decoder part, filter size, epochs etc. thus, achieving a train accuracy of 83.50%.
- Optimizations
    - Downloaded and added images to the existing dataset to make it more robust
    - Used concepts of caching, shuffling and prefetching to optimize the tensorflow input pipeline performance while handling the large dataset
    - Applied Data Augmentation to generate new training examples from existing training set using transformations like Flipping and Roation to prevent overfitting and increase robustibility

### Methodology Flow Chart
![Methodology](https://i.ibb.co/6N6G4qV/Copy-of-Add-a-heading.png "Methodology")

### I/O Screenshots (Web App)
- Home Page Layout
![Layout 1](https://i.ibb.co/ZNKycyT/Screenshot-214.png "Layput 1")
![Layout 2](https://i.ibb.co/PGdXgG5/Screenshot-215.png "Layput 2")

- Upload Image
![Upload Image](https://i.ibb.co/R39zCG4/Screenshot-216.png "Upload Image")

- Colorize
![Colorize](https://i.ibb.co/2kNrscQ/Screenshot-217.png "Colorize")

### I/O Screenshots (Android App)
- Home Page Layout
<img src="https://i.ibb.co/2YMGz3q/Screenshot-20211015-211834.jpg" height="800">
<img src="https://i.ibb.co/87WNXWr/Screenshot-20211015-211840.jpg" height="800">

- Upload Image
<img src="https://i.ibb.co/4j9MfRV/Screenshot-20211015-211853.jpg" height="800">

- Colorize
<img src="https://i.ibb.co/2Z2fT0b/Screenshot-20211015-211917.jpg" height="800">
