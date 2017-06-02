import sys
from PyQt4 import QtGui, QtCore

class FormInterface(QtGui.QWidget):
    def __init__(self, color):
        """
        Initialize.
        """
        super(FormInterface, self).__init__()
        self._origin = None
        self._color = color

    ##############
    # painter definition
    ##############
    def paintEvent(self, event):
        """function which will draw the form
        event dedicated to manage the draw
        """
        # definition of painter
        self.qp = QtGui.QPainter()
        self.qp.begin(self)
        self.addForm(self.qp)
        self.qp.end()


    def createForm(self, form):
        """add the form defined by the class by using the Qpainter"""
        # rajouter un raise not implemented si fonction non utilise dans la classe
        # if this function is called directly by the mother class, an error message will appear
        raise NotImplementedError()

    ##############
    # definition of form origin
    ##############
    @property
    def origin(self):
        return self._origin


    ################
    # move function
    ################
    def isOver(self, x, y):
        raise NotImplementedError()

    def move(self, x, y):
        raise NotImplementedError()

    def shift(self, dx, dy):
        raise NotImplementedError()


class Selection(object):
    """
    Class that represents any selected shape(s)
    """

    def __init__(self, shape, position):
        self.__shape = shape
        self.__pos = position
        self._origin = self.__shape.origin

    def move(self, position):
        delta = position - self.__pos
        self.__shape.move(self._origin[0] + delta.x(), self._origin[1] + delta.y())



    # def mouseDown(self, event):
    #    "Operation a effectuer quand le bouton gauche de la souris est enfonce"
    #    self.currObject = None
    #    # event.x et event.y contiennent les coordonnees du clic effectue :
    #    self.x1, self.y1 = event.x, event.y
    #    # <find_closest> renvoie la reference du dessin le plus proche :
    #    self.selObject = self.find_closest(self.x1, self.y1)
    #    # modification de l epaisseur du contour du dessin :
    #    self.itemconfig(self.selObject, width=2)
    #    # <lift> fait passer le dessin a l'avant-plan :
    #    self.lift(self.selObject)

    # def mouseMove(self, event):
    #    "Op. a effectuer quand la souris se deplace, bouton gauche enfonce"
    #    x2, y2 = event.x, event.y
    #    dx, dy = x2 - self.x1, y2 - self.y1
    #    if self.selObject:
    #        self.move(self.selObject, dx, dy)
    #        self.x1, self.y1 = x2, y2

    # def mouseUp(self, event):
    #    "Op. a effectuer quand le bouton gauche de la souris est relache"
    #    if self.selObject:
    #        self.itemconfig(self.selObject, width=1)
    #        self.selObject = None