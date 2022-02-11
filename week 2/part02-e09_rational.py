
class Rational(object):

    def __init__(self, osoittaja, nimittäjä):
        self.osoittaja = osoittaja
        self.nimittäjä = nimittäjä

    def __mul__(self, other):
        osoittaja = self.osoittaja*other.osoittaja
        nimittäjä = self.nimittäjä*other.nimittäjä
        return Rational(osoittaja, nimittäjä)

    def __truediv__(self, other):
        osoittaja = self.osoittaja*other.nimittäjä
        nimittäjä = self.nimittäjä*other.osoittaja
        return Rational(osoittaja, nimittäjä)

    def __add__(self, other):
        osoittaja = self.osoittaja * other.nimittäjä + other.osoittaja * self.nimittäjä
        nimittäjä = self.nimittäjä * other.nimittäjä
        return Rational(osoittaja, nimittäjä)

    def __sub__(self, other):
        osoittaja = self.osoittaja * other.nimittäjä - other.osoittaja * self.nimittäjä
        nimittäjä = self.nimittäjä * other.nimittäjä
        return Rational(osoittaja, nimittäjä)

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented

        return self.osoittaja == other.osoittaja and self.nimittäjä == other.nimittäjä

    def __gt__(self, other):
        return (self.osoittaja*other.nimittäjä > other.osoittaja*self.nimittäjä)

    def __lt__(self, other):
        return (self.osoittaja*other.nimittäjä < other.osoittaja*self.nimittäjä)

    def __str__(self):
        return str((self.osoittaja, self.nimittäjä))


def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
