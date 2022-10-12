# Assignment 6 <hr>

### Website Link: [ruby-pbp.herokuapp.com/todolist](https://ruby-pbp.herokuapp.com/todolist)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Code yang dijalankan secara asynchronous dapat berjalan secara paralel, sedangkan code yang dijalakan menggunakan synchronous berjalan satu per satu.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven progamming adalah eksekusi program yang ditentukan berdasarkan action yang dilakukan user, seperti click, drag, keypress, dsb. Salah satu contohnya pada tugas ini adalah button create task yang membuka modal berisi form.

## Jelaskan penerapan asynchronous programming pada AJAX.

AJAX secara bersamaan memulai permintaan JavaScript dan XML yang lebih mudah diurai. Hal ini mengurangi waktu membuka halaman website serta meningkatkan kinerja. Dengan AJAX menjalankan protokol HTTP pada url yang sudah. Hal ini memungkinkan data diperbarui secara real-time dengan mulus. Dengan demikian, menghapus komunikasi sinkron sisi klien-ke-server default yang memerlukan proses untuk dijalankan secara berkala, dan seperti namanya – Asynchronus.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Buat view show_todolist_json.
2. Buat function dengan menggunakan ajax untuk meng-GET data dari view json yang sudah dibuat sebelumnya.
3. Tambahkan modal dan buat tombol create task yang berfungsi untuk men-toggle modal tersebut.
4. Pastikan modal berisi form yang sesuai untuk membuat task.
5. Buat function AJAX yang bersesuaian:
   - getTodolist: menampilkan semua todolist user yang sudah login
   - openModal: membuka modal --> ketika button create task di click
   - delete_todolist(id): menghapus task sesuai dengan id yang di-pass melalui paramater id
   - toggle_finish(id): mengubah status task sesuai dengan id
6. Deploy ke heroku
