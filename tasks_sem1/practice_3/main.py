'''
1. Разработать программу для отображения прямоугольника при помощи pygame
2. Разработать программу, которая будет по потокам:
    - Принимать сообщения о положении робота по mqtt
    - Отображать положение робота на экран
'''

import sys
import time

import pygame
import paho.mqtt.client as mqtt
from threading import *

ip_to = "127.0.0.1"
port_to = 1883
topic_to = "test/topic"

screen = pygame.display.set_mode((800, 500))

def draw_a_rect():
    pygame.init()
    clock = pygame.time.Clock()
    done = False

    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

    while not done:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()

def pygame_thread():
    pygame.init()
    clock = pygame.time.Clock()
    done = False

    while not done:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()

def draw_robot_rect(coords):
    offset = 20
    x, y = coords

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x - offset, y - offset, x + offset, y + offset))

def on_message(client, userdata, msg):
    payload = (int(x) for x in msg.payload.split(' '))
    draw_robot_rect(payload)

if __name__ == '__main__':
    #draw_a_rect()

    t1 = Thread(target=pygame_thread())
    t1.start()

    client = mqtt.Client("subscriber")
    client.on_message = on_message
    client.connect(ip_to, port_to)

    client.loop(60)
