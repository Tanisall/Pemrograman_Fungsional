# Function hitung
def hitung_nilai_akhir(nilai_uts, nilai_uas):
    return (nilai_uts + nilai_uas) / 2


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


def main():
    data_mahasiswa = {
        "Tanis Alhariroh": {"nilai uts": 85, "nilai uas": 90},
        "John Doe": {"nilai uts": 78, "nilai uas": 88},
        # Tambahkan data mahasiswa lainnya
    }

    # Menghitung nilai akhir semua mahasiswa
    data_nilai_akhir = {}
    for nama, data in data_mahasiswa.items():
        nilai_uts = data["nilai uts"]
        nilai_uas = data["nilai uas"]
        nilai_akhir = hitung_nilai_akhir(nilai_uts, nilai_uas)
        data_nilai_akhir[nama] = nilai_akhir

    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()
