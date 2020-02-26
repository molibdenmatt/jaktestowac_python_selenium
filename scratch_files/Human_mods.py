class Czlowiek():
    def __init__(self, imie, kolor_wlosow):
        self.imie = imie
        self.kolor_wlosow = kolor_wlosow
        self.wiek = 0

    def urodziny(self):  # metoda wywoływana podczas urodzin
        print('Urodziny' + self.imie)
        self.wiek = self.wiek + 2

    def przedstaw_sie(self):  # metoda służąca do przedstawiania się przez danego człowieka
        print('Mam na imie', self.imie, 'i mam lat', self.wiek)


# w jakimś miejscu w czasie i przestrzeni następują narodziny Ali...
Ala = Czlowiek('Ala', 'czarne')
# mija trochę czasu i...
Ala.urodziny()
# w jakimś miejscu w czasie następują narodziny Adama...
Adam = Czlowiek('Adam', 'blond')
# mija jeszczę trochę czasu i...
Ala.urodziny()
Adam.urodziny()
# mija jeszcze więcej czasu i...
Ala.urodziny()
Adam.urodziny()
# w końcu Ala zapytana jest o przedstawienie się...
Ala.przedstaw_sie()
# a następnie Adam...
Adam.przedstaw_sie()