from PyQt5 import QtWidgets,uic
from load.load_ventana_calculadora import VentanaCalculadora
from load.load_ventana_celsius import VentanaCelsius
from load.load_ventana_galones import VentanaGalones
from load.load_ventana_pozo import VentanaPozo



class MenuPrincipal(QtWidgets.QMainWindow): 
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui",self)
        self.showMaximized()

        self.actionCalculadora.triggered.connect(self.ingresarCalculadora)
        self.actionGalones_a_Litros.triggered.connect(self.ingresarGalones)
        self.actionPozo.triggered.connect(self.ingresarPozo)
        self.actionCelsius_a_F.triggered.connect(self.IngresarCelsius)

        self.actionSalir.triggered.connect(self.salir)

    def ingresarCalculadora(self):
        calculadora = VentanaCalculadora()
        calculadora.exec()
    def ingresarGalones(self):
        galones = VentanaGalones()
        galones.exec()
    def ingresarPozo(self):
        pozo = VentanaPozo()
        pozo.exec()
    def IngresarCelsius(self):
        celsius = VentanaCelsius()
        celsius.exec()            


    def salir(self):
        self.close()

