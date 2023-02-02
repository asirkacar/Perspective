import cv2
import numpy as np

img2 = cv2.imread("sw.jpg")
row2, cols2 = img2.shape[:2]
click_count = 0
a = []
dst_points2 = np.float32([[0, 0],
                         [cols2-1, 0],
                         [0, row2-1],
                         [cols2-1, row2-1]])
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
def draw(event, x, y, flags, param):
    global click_count, a

    if click_count < 4:
        if event == cv2.EVENT_LBUTTONDBLCLK:
            click_count += 1
            a.append((x,y))
    else:
        src = np.float32([
            [a[0][0], a[0][1]],   #a nın ilk tıklamasının xinin 0ıncısı ve ilk tıklamasının ysinin 0ıncısı
            [a[1][0], a[1][1]],   #a nın ikinci tıklamasının xinin ikinicisi ve ikinici tıklamasının ysinin ikinicisi
            [a[2][0], a[2][1]],   #a nın soldakileri tıklanma sayısını sağdakilerde x ve ysini belirtiyo x=0 y=1 anlamında
            [a[3][0], a[3][1]]])
        click_count = 0
        a = []

        M = cv2.getPerspectiveTransform(src, dst_points2)
        output1 = cv2.warpPerspective(img2, M, (cols2, row2))
        cv2.imshow("output", output1)
cv2.setMouseCallback("img",draw)

while(1):
    cv2.imshow("img", img2)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()