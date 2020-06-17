import numpy as np
import cv2


# 定义一个3维数组,相当于是画布,大小H*W,,初始化白色
canvas=np.zeros((400,600,3),dtype=np.uint8)+255

# 画一条纵向的正中央的黑色分界线
cv2.line(canvas, pt1=(300, 0), pt2=(300, 399), color=(0, 0, 0), thickness=1)

# 画一条右半部份画面以150为界的横向分界线
cv2.line(canvas, pt1=(300, 149), pt2=(599, 149), color=(0, 0, 0), thickness=2)

# 左半部分的右下角画个红色的圆
cv2.circle(canvas, center=(200, 300), radius=75, color=(0, 0, 255), thickness=5)

# 定义两个三角形，并执行内部填充
triangles = np.array([[(200, 240), (145, 333), (255, 333)],[(60, 180), (20, 237), (100, 237)]])
cv2.fillPoly(canvas, triangles, (255, 0,255))
cv2.polylines(canvas, triangles, isClosed=True, color=(255, 0,0),thickness=2)

# 画一个黄色五角星
# 第一步通过旋转角度的办法求出五个顶点
phi = 4 * np.pi / 5
rotations = [[[np.cos(i * phi), -np.sin(i * phi)], [i * np.sin(phi), np.cos(i * phi)]] for i in range(1, 5)]
pentagram = np.array([[[[0, -1]] + [np.dot(m, (0, -1)) for m in rotations]]], dtype=np.float)

# 定义缩放倍数和平移向量把五角星画在左半部分画面的上方
pentagram = np.round(pentagram * 80 + np.array([160, 120])).astype(np.int)

# 将5个顶点作为多边形顶点连线，得到五角星
cv2.polylines(canvas, pentagram, True, (0, 255, 255),thickness=3)

for x in range(302, 600):
    color_pixel = np.array([[[round(180*float(x-302)/298), 255, 255]]], dtype=np.uint8)
    line_color = [int(c) for c in cv2.cvtColor(color_pixel, cv2.COLOR_HSV2BGR)[0][0]]
    cv2.line(canvas, (x, 0), (x, 147), line_color)

# 如果定义圆的线宽大于半径，则等效于画圆点，随机在画面右下角的框内生成坐标
np.random.seed(42)
n_pts = 30
pts_x = np.random.randint(310, 590, n_pts)
pts_y = np.random.randint(160, 390, n_pts)
pts = zip(pts_x, pts_y)

# 画出每个点，颜色随机
for pt in pts:
    pt_color = [int(c) for c in np.random.randint(0, 255, 3)]
    cv2.circle(canvas, pt, radius=1, color=pt_color, thickness=2)

# 在左半部分最上方打印文字
text="Python-OpenCV Drawing Example"
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas,text,(5, 15),font,0.5,(0, 0, 0),1)

# 调整窗口
cv2.namedWindow('EXAMPLE',cv2.WINDOW_NORMAL)
cv2.imshow('EXAMPLE', canvas)
cv2.waitKey()