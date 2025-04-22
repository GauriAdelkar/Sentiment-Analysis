# Sentiment-Analysis from Facial Expression

PROJECT DONE BY


Gauri Mahesh Adelkar [ku2407u401]
Prachi Ranjan [ku2407u433]
Rishu Pandey [ku2407u436]


OBJECTIVE OF THE PROJECT


The objective of this project is to develop an AI-based system that can accurately detect and classify human sentiments (such as happiness, sadness, anger, surprise, etc.) by analyzing facial expressions from images or real-time video. The system aims to leverage computer vision and machine learning techniques to interpret emotional states, enhancing applications in human-computer interaction, mental health monitoring, and customer experience analysis.


TOOLS AND LIBRARIES USED


OpenCV  	        Captures webcam video and displays results.
DeepFace	        Analyzes facial emotions from a snapshot.
TextBlob	        (Currently unused) Can analyze or generate text responses.
Python Core	      Error handling and control flow.


EXECUTION STEPS


1. Import required libraries.  
2. Initialize the webcam.  
3. Start reading frames in a loop.  
4. Save the current frame as an image.  
5. Analyze the image using DeepFace for emotion.  
6. Generate a response based on the detected emotion.  
7. Overlay emotion and response on the frame.  
8. Handle cases where no face is detected.  
9. Display the video frame in a window.  
10. Exit loop on key press ('q').  
11. Release the webcam and close windows.


SUMMARY OF RESULTS


* Real-time emotion detection: The program identifies the dominant facial emotion (e.g., happy, sad, angry) from the webcam feed using DeepFace.
  
* Dynamic response generation: Based on the detected emotion, a personalized bot message is generated to simulate empathy or engagement.
  
* Live overlay: Both the emotion label and bot response are displayed in real time on the video frame.
  
* Error handling: If no face is detected, the program gracefully shows a "No face detected!" message instead of crashing.


CHALLENGES FACED


* Face Detection Failures

DeepFace may fail to detect a face in low light, blurry frames, or with extreme facial angles.

* Performance Issues

Real-time emotion analysis can lag due to high computational demands, especially on low-end systems.

* Emotion Prediction Accuracy

DeepFace predictions may sometimes be inaccurate, especially with subtle or mixed emotions.

* Static Image Dependency

The use of cv2.imwrite() to save frames slows down the process and isn’t ideal for real-time applications.

* Webcam Access Conflicts

Conflicts may arise if other apps or threads are using the webcam simultaneously.
