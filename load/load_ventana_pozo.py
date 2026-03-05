from PyQt5 import QtWidgets, uic
from clases.pozo import Pozo


class VentanaPozo(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_pozo.ui", self)
        self.show()

        self.btn_calcular.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):

        profundidad = int(self.lineEdit_profundidad.text())
        energia = int(self.lineEdit_energia.text())

        pozo = Pozo(profundidad, energia)

        tiempo = pozo.calcular()

        self.label_tiempo.setText(str(tiempo))