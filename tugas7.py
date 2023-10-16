def show_data():
    if len(buku) <= 0:
        print("belum ada data")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

buku = ["ayah", "ibu", "kakak", "adek"]
show_data()