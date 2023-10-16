buku = ["laskar pelangi", "laskar pelangi 2", "laskar pelangi 3", "laskar pelangi 4"]
def show_data():
    if len(buku) <= 0:
        print("belum ada data")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))
show_data()
