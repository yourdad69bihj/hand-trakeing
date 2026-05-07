import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

cap = cv2.VideoCapture(0)

print("Jordan Elite System Starting...")

while cap.isOpened():
    success, img = cap.read()
    if not success: break

    # Flip image for mirror effect
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # DRAW SKELETON LINES
            mp_draw.draw_landmarks(
                img, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=(255, 255, 0), thickness=4, circle_radius=4), # Bones
                mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)    # Joints
            )
            
            # GET PALM COORDINATES FOR EFFECTS
            h, w, c = img.shape
            cx, cy = int(hand_landmarks.landmark[0].x * w), int(hand_landmarks.landmark[0].y * h)
            cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED) # Magic Orb in palm

    cv2.imshow("Jordan Elite Desktop Tracker", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()