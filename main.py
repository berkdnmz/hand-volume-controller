import cv2
import mediapipe as mp
import numpy as np
from fontTools.ufoLib import convertFontInfoValueForAttributeFromVersion3ToVersion2
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import math


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

minVol, maxVol, _ = volume.GetVolumeRange()

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cam.read()
    if not ret:
        break
    frame = cv2.flip(frame,1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = frame.shape

            x1 = int(hand_landmarks.landmark[4].x * w)
            y1 = int(hand_landmarks.landmark[4].y * h)
            x2 = int(hand_landmarks.landmark[8].x * w)
            y2 = int(hand_landmarks.landmark[8].y * h)

            mesafe = math.hypot(x2 - x1, y1 - y2)

            minVol = volume.GetVolumeRange()[0]  # genelde -65.25
            maxVol = volume.GetVolumeRange()[1]  # genelde 0.0
            vol = np.interp(mesafe, [30, 200], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)

            try:
                volume.SetMasterVolumeLevel(vol, None)
            except Exception as e:
                print(f"Ses ayarlanamadı: {e}")

            # Görsel çizim
            cv2.circle(frame, (x1, y1), 8, (255, 0, 255), -1)
            cv2.circle(frame, (x2, y2), 8, (255, 0, 255), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)

            # Ses yüzdesini hesapla ve yaz
            ses_yuzde = int(np.interp(mesafe, [30, 200], [0, 100]))
            cv2.putText(frame, f"Ses: {ses_yuzde}%", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            for id, lm in enumerate(hand_landmarks.landmark):

                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.putText(frame, str(id), (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cam.release()
cv2.destroyAllWindows()