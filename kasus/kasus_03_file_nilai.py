def baca_nilai(nama_file):
    with open(nama_file, "r") as file:
        for baris in file:
            print(baris.strip())


baca_nilai("nilai_mahasiswa.txt")