class calculadora1:
    PI = 3.14
    def circunferencia(self,raio) -> float:
        return 2 * self.PI * raio
    def area(self, raio) -> float:
        return self.PI *  raio ** 2