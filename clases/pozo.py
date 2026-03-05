class Pozo:

    def __init__(self, profundidad, energia):
        self.profundidad = profundidad
        self.energia = energia

    def calcular(self):

        d = 1
        ascenso = 0
        tiempo = 0

        while True:
            ascenso += self.energia
            tiempo += 1

            if ascenso >= self.profundidad:
                break

            ascenso -= d
            tiempo += 1

        return tiempo