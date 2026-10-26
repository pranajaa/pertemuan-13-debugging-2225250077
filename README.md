# Pertemuan 13 - Debugging dan Testing

**Nama:** Hitana Rifa Pranaja 

**NIM:** 2225250077

**Kelas:** 3A

## Kasus
Program mengolah nilai mahasiswa dengan tiga fungsi, yaitu menghitung rata-rata, menentukan status kelulusan, dan mencari nilai tertinggi. Debugging dilakukan untuk memperbaiki kesalahan pembagi rata-rata, batas kelulusan, dan pencarian nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` (rata-rata) | 75.0 | 60.0 | Berhasil |
| T2 | `[100, 80]` (rata-rata) | 90.0 | 36.0 | Berhasil |
| T3 | `60` (status) | Lulus | Tidak lulus | Berhasil |
| T4 | `59` (status) | Tidak lulus | Tidak lulus | Berhasil |
| T5 | `[80, 60, 90, 70]` (tertinggi) | 90 | 0 | Berhasil |

## Bug Report

**B01 - Kesalahan perhitungan rata-rata**
- Gejala: Hasil rata-rata tidak sesuai.
- Lokasi: Fungsi `hitung_rata_rata()`.
- Akar penyebab: Pembagi menggunakan angka tetap `5`, bukan jumlah data.
- Perbaikan: Mengganti pembagi dengan `len(nilai)`.

**B02 - Kesalahan batas kelulusan**
- Gejala: Nilai 60 dinyatakan tidak lulus.
- Lokasi: Fungsi `status()`.
- Akar penyebab: Kondisi menggunakan `nilai > 60`.
- Perbaikan: Mengganti kondisi menjadi `nilai >= 60`.

**B03 - Kesalahan pencarian nilai tertinggi**
- Gejala: Fungsi mengembalikan nilai yang salah.
- Lokasi: Fungsi `nilai_tertinggi()`.
- Akar penyebab: Kondisi perbandingan menggunakan operator yang terbalik.
- Perbaikan: Mengganti `x < tertinggi` menjadi `x > tertinggi`.

## Retest

Setelah perbaikan, seluruh lima test case dijalankan kembali dan menghasilkan output sesuai expected result. Semua test case dinyatakan **PASS**.

## Cara Menjalankan

```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah pengujian menggunakan test case karena dapat menunjukkan perbedaan antara hasil yang diharapkan dan hasil aktual. Dengan menelusuri fungsi dan memperbaiki kode secara minimal, kesalahan dapat ditemukan dan diperbaiki tanpa mengubah bagian program yang sudah benar.
