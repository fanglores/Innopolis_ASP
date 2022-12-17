import math


class Command:
    current_position = None
    current_angle = None
    angle = None
    distance = None

    def __init__(self, ang, c1, c2):
        self.current_position = c1
        self.current_angle = ang

        x1, y1 = c1
        x2, y2 = c2
        self.distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.angle = math.atan2(y2 - y1, x2 - x1) - ang