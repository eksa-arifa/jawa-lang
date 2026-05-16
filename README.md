# Bahasa Pemrogramman Jawa (Jawa Programming Language)

Bahasa pemrogramman berbasis python yang dibuat dengan latar belakang gabut,iseng,biar logika coding nggak ilang dikala bingung mau bikin project apaan. Belum diuji coba di os windows, saya baru mengujinya di linux mint.


## Authors

- [@eksa-arifa](https://www.github.com/eksa-arifa)


## Installation

Paling gampang instal langsung lewat pip:

```bash
pip install hidup-jawa
```

Atau kalau mau instal manual dari source:

```bash
git clone https://github.com/eksa-arifa/jawa-lang.git
cd jawa-lang
pip install -e .
```

## Cara Menjalankan

Setelah instalasi selesai, kamu bisa menjalankan file `.jawa` langsung menggunakan perintah `jawa`:

```bash
jawa example/print.jawa
```

Untuk mengecek versi:
```bash
jawa --version
```

## Usage/Examples

Cobalah untuk mengoutputkan sesuatu dengan perintah "tokke". Sekarang sudah bisa menggunakan spasi!

```
tokke "halo dunia sego pecel"
```

Selanjutnya, bagaimana dengan variabel?

```
jane b iku "iki variabel b"
```
Lihat kode di atas, `jane` adalah keyword untuk mendeklarasikan variabel, dengan `b` sebagai key dan string setelah `iku` sebagai value.

### If Else Statement

```
jane b iku 10

nek b iku 10
    tokke "b iku sepuluh"
nekora
    tokke "b dudu sepuluh"
wes
```

Dengan `nek` sebagai **if**, `iku` sebagai **==**, `nekora` sebagai **else**, dan `wes` sebagai **endif**.

### Elif Statement

```
jane b iku 10

nek b iku 10
    tokke "b iku 10"
po b iku 15
    tokke "b iku 15"
nekora
    tokke "mbuh ora weruh"
wes
```
Kalian bisa menuliskan elif statement dengan keyword `po`.

### Function

```
lelakon apik(params)
    tokke params
wes

lakoni apik("joss tenan")
```
Deklarasikan fungsi dengan `lelakon` dan panggil dengan `lakoni`.

### Looping

```
jane i iku 0

baleni nek i kurangSekoPodoKaro 10
    tokke i
    ganti i dadi i+1
wes
```
Gunakan `baleni nek` untuk melakukan perulangan.

## Operator List



| Operator | E     | Description                |
| :-------- | :------- | :------------------------- |
| `iku` | `==` | Persamaan |
| `udu` | `!=` | Pertidaksamaan |
| `luwihSeko` | `>` | Perbandingan lebih dari |
| `kurangSeko` | `<` | Perbandingan kurang dari |
| `luwihSekoPodoKaro` | `>=` | Perbandingan lebih dari sama dengan |
| `kurangSekoPodoKaro` | `<=` | Perbandingan kurang dari sama dengan |

### Tipe Data

Karena `jawa-lang` berjalan di atas Python, kamu bisa menggunakan semua tipe data Python secara langsung:

- **String**: `jane jeneng iku "Eksa Arifa"`
- **Angka**: `jane umur iku 20`
- **List**: `jane buah iku ["Mangga", "Apel", "Jeruk"]`
- **Dictionary**: `jane data iku {"id": 1, "status": "aktif"}`
- **Boolean**: `jane bener iku True`

Contoh penggunaan List:
```
jane daftar iku [1, 2, 3]
tokke daftar[0]
wes
```


## Support

For support, belikan saya kopi

- [@trakteer](https://trakteer.id/eksa_arifa/tip?quantity=1)
## License

[MIT](https://choosealicense.com/licenses/mit/)


