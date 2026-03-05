from load.load_ventana_celsius import VentanaCelsius
from PyQt5 import QtWidgets
import sys


def main():

    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaCelsius()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()