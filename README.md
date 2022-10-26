# P1_Komnum_B4

- Muhammad Zikri Ramadhan (5025211085)

- Alfadito Aulia Denova (5025211157)

- Ligar Arsa Arnata (5025211244)



Pada program kami, kami menggunakan contoh fungsi yang ada pada soal Tugas 1 Nomor 3C, yaitu
10^x = 100 - 2x

Kemudian fungsi ini kami ubah agar salah satu ruas menjadi 0, sehingga fungsi bberbentuk
10^x + 2x - 100 = 0

Bentuk fungsi ini lah yang kami gunakan dalam program kami, yaitu func(n) = pow(10, n) + 2*n - 100

Lalu sesuai dengan metode bolzano, pertama user akan menginputkan perkiraan 2 nilai awal untuk x. Nilai perkiraan ini diharapkan agar left berada di kiri x penyelesaian, dan right ada di kanan x penyelesaian

Dengan memanfaatkan perubahan tanda, maka kita bisa mengetahui apakah nilai x yang kita cari sudah berada di antara left dan right kita
sehingga jika kondisi itu belum terpenuhi, maka program akan meminta user menginputkan 2 bilangan baru sebagai perkiraan baru dari nilai x

Berikutnya program akan melakukan iterasi sebanyak 10 kali menggunakan metode bolzano, dimana nilai tengah dari left dan right sekarang akan
menggantikan left atau right sebelumnya tergantung kondisi mana yang memenuhi terjadinya perubahan tanda antara func(mid) dengan func(left) dan func(right)

Setelah 10 kali iterasi, maka nilai left dan right akan semakin dekat, dengan mencari nilai y manakah antara left dan right yang lebih mendekati 0,
kita bisa memperkirakan penyelesaian fungsi kita sebelumnya
