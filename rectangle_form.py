import sys
from PyQt4 import QtGui, QtCore

from abcdforminterface import FormInterface

class RectangleForm(FormInterface):
    def __init__(self, x1, y1, width, height, color=QtGui.QColor(0, 0, 0)):
        #super(FormInterface, self).__init__()
        FormInterface.__init__(self, color)

        self.define(x1, y1, width, height)

    def define(self, x1, y1, width, height):
        """
        Draw the current rectangle.
        :param x1:
        :param y1:
        :param width:
        :param height:
        """
        self._origin = (x1, y1)
        self.__width = width
        self.__height = height

    def createForm(self, form):
        """goal define and draw the rectangle form"""
        #form.setPen(QtCore.Qt.red)
        form.setPen(self._color)
        form.drawRect(self._origin[0], self._origin[1], self.__width, self.__height)

    def isOver(self, x, y):
        assert (self._origin is not None)
        x_range = (self._origin[0], self._origin[0] + self.__width)
        y_range = (self._origin[1], self._origin[1] + self.__height)
        return (x >= x_range[0]) and (x <= x_range[1]) and (y >= y_range[0]) and (y <= y_range[1])

    def move(self, x, y):
        self._origin = (x, y)




if __name__=="__main__":
    """local app to draw a rectangle"""
    app = QtGui.QApplication(sys.argv)

    """creation fenetre pour Test Unitaire
     creation d'une Fixture - etat initiale du test
    """
    rectD = RectangleForm()
    rectD.setGeometry(300, 300, 350, 100)
    rectD.setWindowTitle('rectangle')
    rectD.show()
    sys.exit(app.exec_())