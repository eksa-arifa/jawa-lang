
# Bahasa Pemrogramman Jawa (Jawa Programming Language)

Bahasa pemrogramman berbasis python yang dibuat dengan latar belakang gabut,iseng,biar logika coding nggak ilang dikala bingung mau bikin project apaan.


## Authors

- [@eksa-arifa](https://www.github.com/eksa-arifa)


## Installation

Petunjuk Instalasi

```bash
  git clone github.link
  cd jawa-lang
```
Jalankan program pertamamu
```bash
  python3 jawa example/print.jawa
```
    
## Usage/Examples

Cobalah untuk meng outputkan sesuatu dengan perintah "tokke"

```
tokke "ini-contoh-string"
```
lihatlah, string tidak boleh memakai spasi, ini adalah salah satu aturan jawa programming language.

selanjutnya, bagaimana dengan variable?

```
jane b iku "ini-variable-b"
```
lihat kode di atas, jane adalah keyword untuk mendeklarasikan variable di jawa programming language, dengan b sebagai key dan string setelah iku sebagai value.

if else steatment

```
jane b iku 10

nek b iku 10
    tokke "b-iku-10"
nekora
    tokke "b-udu-10"
wes

```

lihat syntax diatas, saya mendeklarasikan variable b dengan nilai 10.
kemudian say cek apakah variable b == 10? Jika ya keluarkan "b-iku-10",
jika tidak keluarkan output "b-udu-10". Dengan nek sebagai if, iku sebagai ==, nekora sebagai else, dan wes sebagai endif.

bagaimana dengan elif?

```
jane b iku 10

nek b iku 10
    tokke "b-iku-10"
po b iku 15
    tokke "b-iku-15"
nekora
    tokke "mbuh"
wes
```
Lihat kode diatas, kalian bisa menuliskan elif steatment dengan keyword "po".


Bagaimana dengan function? Lihat kode dibawah
```
lelakon apik(params)
    tokke params
wes

lakoni apik("joss-tenan")
```
Lihat kode diatas, kalian bisa mendeklarasikan function dengan keyword lelakon diikuti nama function dan parameter.

kalian juga dapat memanggil function tersebut dengan menggunakan keyword lakoni diikuti nama function dan beri parameter jika ada.

Bagaimana dengan looping di jawa programming language?


```
jane i iku 0

baleni nek i kurangSekoPodoKaro 10
    tokke i

    ganti i dadi i+1
wes

```

Lihat, anda dapat menggunakan keyword baleni diikuti keyword nek -> variable increment -> operator -> nilai kondisi ketika, untuk melakukan looping.

Tambahan, input

```
pitakonan key "Parameter"

tokke key
```

Saya juga menambahkan keyword pitakonan diikuti key -> Params, untuk menginputkan sesuatu agar bahasa ini bisa lebih berguna. 
## Operator List



| Operator | E     | Description                |
| :-------- | :------- | :------------------------- |
| `iku` | `==` | Persamaan |
| `udu` | `!=` | Pertidaksamaan |
| `luwihSeko` | `>` | Perbandingan lebih dari |
| `kurangSeko` | `<` | Perbandingan kurang dari |
| `luwihSekoPodoKaro` | `>=` | Perbandingan lebih dari sama dengan |
| `kurangSekoPodoKaro` | `<=` | Perbandingan kurang dari sama dengan |




## Support

For support, belikan saya kopi

- [@trakteer](https://trakteer.id/eksa_arifa/tip?quantity=1)
## License

[MIT](https://choosealicense.com/licenses/mit/)

