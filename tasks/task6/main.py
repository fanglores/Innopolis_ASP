'''
Разработать программу, которая будет реализовывать следующие функции:

1. Отображать на экране видео с web камеры или из файла (источник видео должен передаваться через параметры командной строки)
2. Отлавливать нажатия левой клавиши мыши на изображении с камеры и отображать при помощи отрисовки прямоугольника места нажатий
3. Подписываться на топик position в MQTT и передавать туда строку с координатами всех нажатых точек
4. По нажатию кнопки С или сбрасывать все отмеченные точки (после сброса точки не отображаются на экране и не передаются по MQTT)
5. По нажатию кнопки Q или кнопки tkinter завершать приложение
'''

import sys
import os
import cv2

WINDOW_NAME = 'OpenCV feat. MQTT'
RECTS = []
IMAGE_REF = None

def draw_all_rects(img):
    offset = 5
    for rect in RECTS:
        x, y = rect
        cv2.rectangle(img, (x - offset, y - offset), (x + offset, y + offset), (0, 255, 0), 1)

def clear_all_rects():
    RECTS.clear()

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        RECTS.append((x, y))

if __name__ == '__main__':
    assert (len(sys.argv) - 1 > 0)  # source name
    filename = sys.argv[1]

    assert (os.path.exists(filename))

    img = cv2.imread(filename)
    IMAGE_REF = img.copy()

    cv2.namedWindow(WINDOW_NAME)
    cv2.setMouseCallback(WINDOW_NAME, click_event)

    while cv2.getWindowProperty(WINDOW_NAME, 0) >= 0:
        draw_all_rects(img)
        cv2.imshow(WINDOW_NAME, img)

        k = cv2.waitKey(1) & 0xFF

        if k == ord('c'):
            print("[DEBUG] Key 'c' was pressed")
            img = IMAGE_REF.copy()
            clear_all_rects()

        if k == ord('q'):
            print("[DEBUG] Key 'q' was pressed")
            break

    cv2.destroyAllWindows()
