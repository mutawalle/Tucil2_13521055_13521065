# Closest Pair of Points
Disusun untuk memenuhi Tugas Kecil 2 IF2211 Strategi Algoritma "Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer"

## Daftar Isi
* [Deskripsi Singkat Program](#deskripsi-singkat-program)
* [Struktur Program](#struktur-program)
* [Requirement Program](#requirement-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Screenshot](#screenshot)
* [Author](#author)

## Deskripsi Singkat Program
Pencarian 2 titik terdekat merupakan salah satu permasalahan klasik. Pada program ini, masalah tersebut diselesaikan menggunakan pendekatan divide and conquer.
Pada mulanya kumpulan titik akan akan dibagi menjadi dua bagian. Kemudian setiap bagian akan dicari jarak dua titik terkceilnya. Solusi tiap bagian akan dibandingkan dan yang paling rendahh akan menjadi solusi untuk permaslahan yang utama.


## Struktur Program
```
.
├─── .gitignore
├─── README.md
│     
├─── doc
│     └─── Tucil2_13521055_13521065.pdf
│
├─── img
│     ├─── plot1.jpg	
│     ├─── plot2.jpg	
│     ├─── test1.jpg
│     ├─── test2.jpg		
│     └─── test3.jpg
│
└─── src
      ├─── main.py
      ├─── type.py
      ├─── algorithm.py
      └─── ioProcedure.py
```

## Requirement Program
* Python versi 3.8.5 atau lebih baru. Pastikan pula terdapat package PyPi (PIP) pada Python Anda.
* Matplotlib untuk visualisasi

## Cara Menjalankan Program
1. Jalankan main.py yang berada pada folder src dengan mengetik `python main.py`

## Screenshot
### TC1 (n = 16, d = 3)
<p align="center">
    <img src="https://github.com/mutawalle/Tucil2_13521055_13521065/blob/main/img/test1.jpg" height="300">
    <img src="https://github.com/mutawalle/Tucil2_13521055_13521065/blob/main/img/plot1.jpg" height="300">
</p>

### TC2 (n = 100, d = 2)
<p align="center">
    <img src="https://github.com/mutawalle/Tucil2_13521055_13521065/blob/main/img/test2.jpg" height="300">
    <img src="https://github.com/mutawalle/Tucil2_13521055_13521065/blob/main/img/plot2.jpg" height="300">
</p>

### TC3 (n = 1000, d = 10)
<p align="center">
    <img src="https://github.com/mutawalle/Tucil2_13521055_13521065/blob/main/img/test3.jpg" height="300">
</p>

## Author
* Nama: Muhammad Bangkit Dwi Cahyono <br />
  NIM: 13520055 <br />
  Prodi/Jurusan: STEI/Teknik Informatika <br />
  Profile GitHub: [bangkitdc](https://github.com/bangkitdc)

* Nama: Mutawally Nawwar <br />
  NIM: 13520065 <br />
  Prodi/Jurusan: STEI/Teknik Informatika <br />
  Profile GitHub: [mutawalle](https://github.com/mutawalle)
