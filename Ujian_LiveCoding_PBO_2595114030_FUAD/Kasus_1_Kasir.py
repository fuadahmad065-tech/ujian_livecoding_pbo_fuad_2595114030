class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga, jumlah):
        self.pelanggan = pelanggan
        self.barang = barang
        self.harga = harga if harga > 0 else 1  # Validasi
        self.jumlah = jumlah if jumlah > 0 else 1  # Validasi

    def hitung_total(self):
        subtotal = self.harga * self.jumlah
        if subtotal >= 500000: diskon = 0.15
        elif subtotal >= 250000: diskon = 0.10
        elif subtotal >= 100000: diskon = 0.05
        else: diskon = 0
        
        potongan = subtotal * diskon
        total = subtotal - potongan
        return subtotal, diskon, potongan, total

    def cetak_struk(self):
        sub, disk, pot, tot = self.hitung_total()
        print("\n=== STRUK PEMBAYARAN ===")
        print(f"Pelanggan : {self.pelanggan}\nBarang    : {self.barang}")
        print(f"Subtotal  : Rp{sub:,.0f}\nDiskon    : {disk*100:.0f}%".replace(",", "."))
        print(f"Potongan  : Rp{pot:,.0f}\nTotal bayar : Rp{tot:,.0f}".replace(",", "."))

print("=== KASIR MINIMARKET ===")
nama = input("Nama pelanggan : ")
brg = input("Nama barang    : ")
hrg = float(input("Harga barang   : "))
jml = int(input("Jumlah barang  : "))

kasir = TransaksiKasir(nama, brg, hrg, jml)
kasir.cetak_struk()

