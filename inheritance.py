class ikan:
    def __init__(self , Daerahpenyebaran,warna,ukuran,habitat):
        self.Daerahpenyebaran = Daerahpenyebaran
        self.warna = warna
        self.ukuran = ukuran
        self.habitat = habitat

    def printname(self):
        print(self.Daerahpenyebaran)
        print(self.warna)
        print(self.ukuran)
        print(self.habitat)

class demersal(ikan):
    def __init__(self , Daerahpenyebaran,warna, ukuran,habitat):
        ikan.__init__(self, Daerahpenyebaran, warna,ukuran,habitat)
        self.jenis = "Ikan Peperek"

    def tampilandemersal(self):
        print("Jenis Ikan Demersal      : ",self.jenis)
        print("Daerah Penyebaran        : ",self.Daerahpenyebaran)
        print("warna                    : ",self.warna)
        print("ukuran                   : ",self.ukuran)
        print("habitat                  : ",self.habitat)

class pelagis(ikan):
    def __init__(self , Daerahpenyebaran,warna, ukuran,habitat):
        ikan.__init__(self, Daerahpenyebaran, warna,ukuran,habitat)
        self.jenis = "Ikan Tongkol"

    def tampilanpelagis(self):
        print("Jenis Ikan Demersal      : ",self.jenis)
        print("Daerah Penyebaran        : ",self.Daerahpenyebaran)
        print("warna                    : ",self.warna)
        print("ukuran                   : ",self.ukuran)
        print("habitat                  : ",self.habitat)
        
a =  demersal("seluruh perairan pantai Indonesia", "keperak-perakan", "6-10 cm", "perairan pantai kedalaman 40m")
b = pelagis("Perairan selatan Jawa-Bali", "biru gelap metalik", "40cm", "perairan laut kedalaman 50 cm ")

a.tampilandemersal()
b.tampilanpelagis()

