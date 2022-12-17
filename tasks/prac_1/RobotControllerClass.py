import time
from paho.mqtt import client as mqtt

from CommandClass import Command


class RobotController:
    ip_to = None  # broker mqtt IP
    port_to = None  # port
    topic_to = None  # topic name
    v = None  # velocity
    w = None  # angular velocity
    filename = None  # coordinates filename

    cmdStack = [None]  # command sequence

    client = None  # mqtt client

    def __init__(self, args):
        self.ip_to = args[0]
        self.port_to = int(args[1])
        self.topic_to = args[2]
        self.v = float(args[3])
        self.w = float(args[4])
        self.filename = args[5]

        assert (sys.path.exists(self.filename))

        with open(self.filename, 'r') as file:
            lines = file.readlines()

            prev_line = [0, 0]  # предполагаем, что изначально робот в (0,0) и направлен по оси ОХ
            prev_ang = 0
            for line in lines:
                self.cmdStack.append(Command(prev_ang, prev_line, line))

                prev_line = line
                prev_ang = self.cmdStack[-1].current_angle
        file.close()

    def connect(self):
        self.client = mqtt.Client("publisher")
        self.client.connect(self.ip_to, self.port_to)

    def run(self):
        for cmd in self.cmdStack:
            t1, t2 = cmd.angle / self.w, cmd.distance / self.v
            msg = r"{\"rotate\": {}, \"move\" {}}".format(t1, t2)
            print("[DEBUG] Command to send: [{}]".format(msg))

            self.client.publish(self.topic_to, msg)
            time.sleep(t1 + t2 + 2)     # ждем завершения работы команд
            time.sleep(2)               # ждем чтобы робот постоял в точке (по ТЗ)