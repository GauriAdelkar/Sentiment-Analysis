import cv2
from deepface import DeepFace
from textblob import TextBlob

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save frame for analysis
    cv2.imwrite("temp.jpg", frame)
    
    try:
        # Analyze emotion (CV)
        result = DeepFace.analyze("temp.jpg", actions=["emotion"])
        emotion = result[0]["dominant_emotion"]
        
        # Generate response (NLP)
        if emotion == "happy":
            response = "You look happy! What's making you smile today?"
        elif emotion == "sad":
            response = "You seem sad. Would you like to talk about it?"
        else:
            response = f"I see you're feeling {emotion}. How can I help?"

        # Display emotion + response
        cv2.putText(frame, f"Emotion: {emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Bot: {response}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    except:
        cv2.putText(frame, "No face detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Emotion Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
