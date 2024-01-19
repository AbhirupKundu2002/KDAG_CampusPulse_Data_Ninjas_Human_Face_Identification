## KDAG_CampusPulse_Data_Ninjas_Human_Face_Identification

The project is a submission to the event "Campus Pulse" organised by KDAG, IIT Kharagpur.
It attempts to solve the problem of long library queues at the Central Library , IIT Kharagpur bu automating the log entry of student details and their laptop brand name.
# Overview
This model uses a CNN based face-detection and identification algorithm and subsequent logging, and a laptop brand logo identifier to speeden the entry and exit process

# Implementation Approach and Highlights

The model achieves face identification after training on a single image for each training class(students in our case), thus byepassing any possible hindrance due to availability of a single image per student in the Institute database

We have utilised the **face_recognition module** in Python for identification of images. The training images are converted to face encodings or an embedding vector and stored. 
The model then captures frames from real time camera via OpenCV functions. It detects landmarks of faces in the image, converts them into embeddings and finds similiarity scores with each database element and for above a specifiable "tolerance" value, maps the person with an existing database. 

The logo detection code works by first creating a map between brand names and their logo imageset. It uses a Neural Network Architecture with**4 convolutional layers, 1 dense layer and an output layer with softmax activation**, returning probabilities of the test dataset of belonging to any of the training classes. We output the brand name with the highest probability 
The dataset for laptop logos were generated through bing-image-downloader, which can be installed by
```
pip install bing-image-downloader
```

The name, timestamp and other details gets logged into **"Log.csv".**
The exit code works similiarly, finding and deleting the record from the CSV upon face identification.




