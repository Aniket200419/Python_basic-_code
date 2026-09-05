import cv2
import os
# -----------------------------
# Load Haar Cascade
# -----------------------------
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
# Check if cascade loaded
if face_cascade.empty():
    print("Error: Haar Cascade file could not be loaded.")
    exit()
# -----------------------------
# Create folder for captured faces
# -----------------------------
save_folder = "captured_faces"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)
# -----------------------------
# Open webcam
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

img_count = 0

print("Webcam started successfully.")
print("Press 'C' to capture a face.")
print("Press 'Q' to quit.")

# -----------------------------
# Main loop
# -----------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    # Flip camera image for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(80, 80)
    )

    # Draw rectangle around detected faces
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Face Detected",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Display webcam
    cv2.imshow(
        "AI Face Capture - Press C to Capture | Q to Quit",
        frame
    )

    # Read keyboard
    key = cv2.waitKey(1) & 0xFF

    # -----------------------------
    # Capture face
    # -----------------------------
    if key == ord("c"):

        if len(faces) > 0:

            # Capture first detected face
            x, y, w, h = faces[0]

            face = frame[y:y + h, x:x + w]

            img_count += 1

            filename = os.path.join(
                save_folder,
                f"face_{img_count}.jpg"
            )

            cv2.imwrite(filename, face)

            print("Face Captured:", filename)

        else:
            print("No face detected. Please look at the camera.")

    # -----------------------------
    # Quit
    # -----------------------------
    elif key == ord("q"):
        break

# -----------------------------
# Release resources
# -----------------------------
cap.release()
cv2.destroyAllWindows()

print("Program closed.")