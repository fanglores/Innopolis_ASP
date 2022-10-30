'''
1. Разработать программу, которая будет читать данные из файла по строкам и публиковать их в топике MQTT при помощи вызова system и mosquito_pub
2. Разработать программу, которая будет подписываться на топик и вычислять скользящее среднее (v[t]*0.6+v[t-1]*0.3+v[t-2]*0.1) по переменной
и выводить текущее значение на экран
'''
import os
import paho.mqtt.client as mqtt

ip_to = "127.0.0.1"
port_to = 1883
topic_to = "test/topic"

def read_and_publish(path):
    client = mqtt.Client("publisher")
    client.connect(ip_to, port_to)
    f = open(path, "r")
    
    lines = f.readlines()
    for line in lines:
        client.publish(topic_to, line)

v = []
def print_avg(vt):
    if(len(v) <= 0):
        return -1
    
    if(len(v) == 1):
        print(v[0]*0.6)
        return 0
    
    if(len(v) == 2):
        print(v[1]*0.6 + v[0]*0.3)
        return 0
    
    print(v[2]*0.6 + v[1]*0.3 - v[0]*0.1)
    return 0

def on_message(client, userdata, msg):
    if(len(v) == 3):
        v.pop(0)
        v.append(float(msg.payload))
        print_avg(v)
        return 0

    v.append(float(msg.payload))
    print_avg(v)
    return 0
        
def subscribe_and_print():
    client = mqtt.Client("subscriber")
    client.on_message = on_message
    client.connect(ip_to, port_to)
    
    client.loop(60)


if __name__ == '__main__':
  read_and_publish("text.txt")
  subscribe_and_print()
