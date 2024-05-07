class Masin():
    def __init__(self, marka, reng, suret, silindir):
        self.marka = marka
        self.reng = reng
        self.suret = suret
        self.silindir = silindir

    def yukseksuretli(self):
        if self.suret > 200:
            return "{} yüksek hızda gidiyor.".format(self.marka)
        else:
            return "{} normal hızda gidiyor.".format(self.marka)

    
    def suret_artir(self, artis):
        self.suret += artis
        return "{} masinin sureti {}-dir.".format(self.marka, self.suret)

    def rengi_guncelle(self, yeni_reng):
        self.reng = yeni_reng
        return "{} masinin yeni rengi {}-dir.".format(self.marka, self.reng)

Mercedes = Masin("Mercedes", "qara", 250, 4)

BMW = Masin("BMW", "ag", 230, 4)
RangeRover = Masin("Range Rover", "qirmizi", 180, 4)

print("{}-in {} var ve max sureti {}-dir. Onun {} silindiri var".format(Mercedes.marka, Mercedes.reng, Mercedes.suret, Mercedes.silindir))

print(Mercedes.rengi_guncelle("mavi"))

print(RangeRover.suret_artir(20))
