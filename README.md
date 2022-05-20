# Face-Match

# Project Name: Which Bollywood Celebrity You look like

A Deep learning based streamlit web app which can tell with which bollywood celebrity your face resembles.

Face recognition is the problem of identifying and verifying people in a photograph by their face.
It is a task that is trivially performed by humans, even under varying light and when faces are changed by age or obstructed with accessories and facial hair. Nevertheless, it is remained a challenging computer vision problem for decades until recently.

Deep learning methods are able to leverage very large datasets of faces and learn rich and compact representations of faces, allowing modern models to first perform as-well and later to outperform the face recognition capabilities of humans.

In this project, you will discover the problem of face recognition and how deep learning methods can achieve superhuman performance to identify similar faces.

## Original repo:
https://github.com/Sukruth097/Face-Match


This is a methods of identifying similar faces check various aspects on pictures, including: face shape, nose, eyes and mouth; face position in the picture; skin color (including the lighting of the photo); color and hair and cosine_similarity.

# Dataset has been used:
https://www.kaggle.com/sushilyadav1998/bollywood-celeb-localized-face-dataset


# Some Real Time Demo:

Web app look

![image](https://user-images.githubusercontent.com/65019778/169478823-332110b9-0aaa-412d-a6de-a6c8bb83bac4.png)

Lets check some of images

![WhatsApp Image 2022-05-19 at 10 05 35 PM](https://user-images.githubusercontent.com/65019778/169477875-cf6f4f8d-9f38-446d-ace2-dad428c0bdfc.jpeg)

![image](https://user-images.githubusercontent.com/65019778/169477982-9a5f0e53-1273-478b-84be-17dee35028d2.png)


# STEPS to run this project:

You can also use others images instead of bollywood actorss

## STEP 01: 
Clone the repository

```bash
git clone https://github.com/entbappy/Which-Bollywood-Celebrity-You-look-like.git
```

## STEP 02: 
Create an environment


```bash
conda create -n celebrity python=3.7 -y
```

## STEP 03: 
Install the requirements


```bash
pip install -r requirements.txt
```

## STEP 04: 
Download the data from the link and keep it in your project directory. Make sure all the actress folder should be in just one folder called data, like that

<img src="demo/data.png" alt="workflow" width="70%">

## STEP 05: 
Just execute this command one time if you are not changing the data


```bash
python run.py
```

## STEP 06: 
Now to start the webapp run the following command


```bash
streamlit run app.py
```

yes!! Now you can start predicting 🙂

# Authors:
```bash
Author: Sukruth A V
Data Scientist
Email: sukruthav007@gmail.com
```

