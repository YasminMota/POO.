class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def qualQuadrante(self, x, y):

        if (x > 0 and y > 0):
            return 1
        if (x < 0 and y > 0):
            return 2
        if (y < 0 and x < 0):
            return 3
        if (y < 0 and x > 0):
            return 4
        if (y == 0 and x == 0):
            return 'Origem'

class Quadrilatero():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def contidoEmQ(self, a):
        if (a.getX () <= a.p2.getX()
            & a.getX() >= a.p1.getX()
            & a.getY() <= a.p1.getY()
            & a.getY() >= a.p2.getY()):
            return True
        else:
            return False


