from PyQt5 import QtWidgets, uic
from clases.galones import Galones


class VentanaGalones(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_galones.ui", self)
        self.show()

        self.btn_convertir.clicked.connect(self.botonConvertirClick)

    def botonConvertirClick(self):

        gal = float(self.lineEdit_galones.text())

        galones = Galones(gal)

        litros = galones.convertir()

        self.label_resultado.setText(str(litros))