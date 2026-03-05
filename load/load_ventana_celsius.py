from PyQt5 import QtWidgets, uic
from clases.conversor_temperatura import ConversorTemperatura


class VentanaCelsius(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        uic.loadUi("gui/ventana_celsius.ui", self)
        self.show()

        self.btn_convertir.clicked.connect(self.botonConvertirClick)

    def botonConvertirClick(self):

        celsius = float(self.edit_celsius.text())

        conversor = ConversorTemperatura()
        resultado = conversor.celsius_a_fahrenheit(celsius)

        self.label_resultado.setText(str(resultado) + " °F")