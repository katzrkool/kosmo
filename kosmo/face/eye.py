from .servo import BaseServo


class Eye:
    xMin = -50
    xMax = 50
    yMin = -90
    yMax = 50
    # The yMin and yMax haven't been finalized, the 50s are just place holders

    def __init__(self, side: str, xPin: int, yPin: int, xMin: float = xMin, xMax: float = xMax,
                 yMin: float = yMin, yMax: float = yMax):
        self.x = BaseServo(xPin, xMin, xMax)
        self.y = BaseServo(yPin, yMin, yMax)
        self.side = side

    def setX(self, angle: float):
        self.x.setPosition(angle)

    def setY(self, angle: float):
        self.y.setPosition(angle)

    def getConfig(self):
        return {'side': self.side, 'part': 'eye', 'xPin': self.x.pin, 'yPin': self.y.pin, 'xMin': self.x.angMin,
                'xMax': self.x.angMax, 'yMin': self.y.angMin, 'yMax': self.y.angMax}

    def getAngles(self):
        return {'x': self.x.getAngle(), 'y': self.y.getAngle()}