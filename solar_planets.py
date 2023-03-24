import cv2

img = cv2.imread("solar-system.jpg")

txt1 = "Mercury"
cv2.putText(
            img,
            txt1,
            (90,170),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )

txt2 = "Venus"
cv2.putText(
            img,
            txt2,
            (180,270),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )

txt3 = "Earth"
cv2.putText(
            img,
            txt3,
            (270,170),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )

txt4 = "Mars"
cv2.putText(
            img,
            txt4,
            (380,270),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )

txt5 = "Jupiter"
cv2.putText(
            img,
            txt5,
            (540,70),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )

txt6 = "Saturn"
cv2.putText(
            img,
            txt6,
            (720,270),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )

txt7 = "Uranus"
cv2.putText(
            img,
            txt7,
            (940,130),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )

txt8 = "Neptune"
cv2.putText(
            img,
            txt8,
            (1100,280),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,
            color= (255,255,255)
           )
finalIMG=cv2.imwrite("solar-system.jpg",img)

cv2.imshow("output",img)
#print(img)
cv2.waitKey(0)
