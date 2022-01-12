
# <center>**Neural Style Transfer**</center>

## **Table of Contents**

**1.**  [**Introduction**](#Section1)
**2.**  [**Imported Libraries**](#Section2)
**3.**  [**Output from Fast Style Transfer**](#Section3)
**4.**  [**Output from Manual Optimization**](#Section4)
**5.**  [**Applications**](#Section5)

<a id=Section1></a>

## **1. Introduction**


- Neural style transfer is an optimization technique used to take two images — a content image and a style reference image (such as an artwork by a famous painter) — and blend them together so the output image looks like the content image, but **“painted”** in the style of the style reference image.

<center><img  src="https://github.com/insaid2018/project-gallery/blob/main/AI/Neural%20Style%20Transfer/Images/styletransfer.jpg?raw=true" width=75%></center>

- This is implemented by optimizing the output image to match the content statistics of the content image and the style statistics of the style reference image.

- These statistics are extracted from the images using a convolutional network.

<a  id=Section2></a>

## **2. Imported Libraries**

The following libraries have been imported in the notebook:


- **Pandas**: Importing for panel data analysis
- **PIL**: PIL is an imaging library for Python programming language.
- **Numpy**: For numerical python operations
- **Matplotlib (Pyplot)**: A popular plotting library used along with pandas
- **Tensorflow**: TensorFlow is an end-to-end open source platform for machine learning.
- **Keras**: Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow.
- **Other Libraries**: time, os, and functools have been imported as well.

<a  id=Section3></a>

## **3. Output from Fast Style Transfer**

- We are taking the following images for content and style for our study:

<center><img  src="https://github.com/insaid2018/project-gallery/blob/main/AI/Neural%20Style%20Transfer/Images/content%20and%20style%20image.jpeg?raw=true" width=75%></center>

- We get the following output after applying fast style transfer:

<center><img  src="https://github.com/insaid2018/project-gallery/blob/main/AI/Neural%20Style%20Transfer/Images/fast_st.png?raw=true" width=75%></center>


<a  id=Section4></a>

## **4. Output from Manual Optimization**

- We are again taking the same content and style images:

<center><img  src="https://github.com/insaid2018/project-gallery/blob/main/AI/Neural%20Style%20Transfer/Images/content%20and%20style%20image.jpeg?raw=true" width=75%></center>

- We get the following output after applying manually optimizing the style transfer:

<center><img  src="https://github.com/insaid2018/project-gallery/blob/main/AI/Neural%20Style%20Transfer/Images/stylized-image.png?raw=true" width=75%></center>

<a id=Section5></a>

## **5. Applications**

- CNN, transfer learning, and style tranfer could be very useful in various applications.
- We can use **MobileNetV2** with **TFLite** to implement the style transfer in **mobile devices** with ARM processors.
- Apps like **Prisma** have been using neural style transfer in their apps to provide good filters for images.
- Style transfer can also be used for **text style transfer** (for handwriting), for **hairstyle swaps**, etc.
- **Generative Adversial Networks (GANs)** can also be used for a more advanced level of style transfer.


