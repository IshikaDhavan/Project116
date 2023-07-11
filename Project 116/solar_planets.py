import cv2

img = cv2.imread("D:\Python\Project 116\PRO-C116-project-image-main-main\PRO-C116-project-image-main-main\solar-system.jpg")

cv2.putText(
    img,
    'Sun',
    (20,300),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.75,
    (225,225,225)
)

cv2.putText(
    img,
    'Mercury',
    (115,250),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.54,
    (219,206,202)
)

cv2.putText(
    img,
    'Venus',
    (200,255),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.6,
    (225,225,225)
)

cv2.putText(
    img,
    'Earth',
    (285,258),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.5,
    (225,225,225)
)

cv2.putText(
    img,
    'Mars',
    (385,250),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.5,
    (225,225,225)
)

cv2.putText(
    img,
    'Jupiter',
    (580,305),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.6,
    (225,225,225)
)

cv2.putText(
    img,
    'Saturn',
    (800,286),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.6,
    (225,225,225)
)

cv2.putText(
    img,
    'Neptune',
    (975,270),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.6,
    (225,225,225)
)

cv2.putText(
    img,
    'Uranus',
    (1105,270),
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    0.6,
    (225,225,225)
)

cv2.imshow("Output..." , img)
cv2.waitKey(0)

cv2.imwrite("SolarSystemwithname.jpg",img)
