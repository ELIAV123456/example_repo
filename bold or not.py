import cv2
import numpy as np

# 1. טעינת המודל
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# משתנה להחלקת התוצאה (כדי שהמספרים לא יקפצו משוגע)
smooth_score = 0
# כוון את הרגישות כאן: מספר גבוה יותר = צריך יותר "בלאגן" כדי שיחשב שיער
THRESHOLD = 15

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # זיהוי פנים
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        # --- הגדרת אזור השיער ---
        # אנחנו לוקחים ריבוע קטן בחלק העליון של הראש
        # שיניתי את המיקום כדי שיהיה מעל המצח
        roi_y_start = y
        roi_y_end = y + int(h * 0.25)  # 25% העליונים של הפנים
        roi_x_start = x + int(w * 0.2)  # מצמצמים מהצדדים כדי לא לתפוס רקע
        roi_x_end = x + w - int(w * 0.2)

        # בדיקת גבולות כדי למנוע קריסה (Bug Fix)
        if roi_y_start < 0: roi_y_start = 0

        # חיתוך האזור לבדיקה
        roi = gray[roi_y_start:roi_y_end, roi_x_start:roi_x_end]

        if roi.size > 0:
            # --- לב האלגוריתם: זיהוי קצוות (Edges) ---
            # הפקודה הזו הופכת את התמונה לשחור-לבן כאשר רק "שינויים חדים" (שיער) נצבעים בלבן
            edges = cv2.Canny(roi, 50, 150)

            # ספירת הפיקסלים הלבנים (כמה "בלאגן" יש בשיער)
            edge_count = np.count_nonzero(edges)

            # חישוב הצפיפות (ביחס לגודל הריבוע, כדי שמרחק מהמצלמה לא ישנה)
            area = roi.shape[0] * roi.shape[1]
            density = (edge_count / area) * 1000  # מכפילים לסקלה נוחה

            # --- החלקה (Smoothing) ---
            # אנחנו לוקחים 80% מהערך הקודם ו-20% מהחדש כדי למנוע קפיצות
            smooth_score = (smooth_score * 0.8) + (density * 0.2)

            # --- קבלת החלטה ---
            if smooth_score > THRESHOLD:
                status = f"Hair Detected ({int(smooth_score)})"
                color = (0, 255, 0)  # ירוק
            else:
                status = f"Bald / Smooth ({int(smooth_score)})"
                color = (0, 0, 255)  # אדום

            # ציור על המסך
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.rectangle(frame, (roi_x_start, roi_y_start), (roi_x_end, roi_y_end), (255, 255, 0),
                          1)  # האזור הנבדק (תכלת)
            cv2.putText(frame, status, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            # --- הצגת חלון דיבאג (כדי שתבין מה המחשב רואה) ---
            # מציג את "מפת הקווים" בחלון קטן בצד
            cv2.imshow('Debug: What Computer Sees', edges)

    cv2.imshow('Main Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()