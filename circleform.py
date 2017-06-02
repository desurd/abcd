import sys
from PyQt4 import QtGui, QtCore

from abcdforminterface import FormInterface

class CircleForm(FormInterface):
    def __init__(self, x1, y1, rx, ry, color=QtGui.QColor(0, 0, 0)):
        #super(FormInterface, self).__init__()
        FormInterface.__init__(self, color)

        self.define(x1, y1, rx, ry)

    ################
    # define origine of circle
    ################
    def define(self, x1, y1, rx, ry):
        self._origin = (x1, y1)
        self._rx = rx
        self._ry = ry

    ###################
    # move form
    ###################
    def isOver(self, x, y):
        print ('inside circle isover')
        assert (self._origin is not None)
        x_range = (self._origin[0] - self._rx, self._origin[0] + self._rx)
        y_range = (self._origin[1] - self._ry, self._origin[1] + self._ry)
        return (x >= x_range[0]) and (x <= x_range[1]) and (y >= y_range[0]) and (y <= y_range[1])

    def move(self, x, y):
        self._origin = (x, y)


    def createForm(self, form):
        """goal define and draw the rectangle form"""
        form.setPen(QtCore.Qt.green)
        form.drawEllipse(self._origin[0], self._origin[1], self._rx, self._ry)




if __name__=="__main__":
    """local app to draw a rectangle"""
    app = QtGui.QApplication(sys.argv)
    CircleD = CircleForm()
    sys.exit(app.exec_())