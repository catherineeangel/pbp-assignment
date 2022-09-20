<!-- Membuat sebuah README.md yang berisi tautan menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:
 Jelaskan perbedaan antara JSON, XML, dan HTML!
 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
 Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon HTTP 200 OK
 -->

# Assignment 3

### Website Link: [ruby-pbp.herokuapp.com](https://ruby-pbp.herokuapp.com/)

## Perbedaan JSON, XML, dan HTML

- JSON merupakan singkatan dari Javascript Object Notation. Format data yang tersimpan dalam JSON berupa object yang memiliki key dan value.  
  contoh:

```
  {
  "mywatchlist":
      {
  "watched": true,
  "title": "500 Days of Summer",
  "rating": 4,
  "release_date": "2009-07-17",
  "review": "With its very catchy storyline, this movie is one of the best movies in the 'Romance' genre. With lots of highs and lows, the movie is unpredictable and interesting right till the end. Joseph Levitt who plays Tom Hansen falls in love with a girl named Summer(Zooey Deschanel) who doesn't quite believe in love and relationships. But being one-sided love relationship it doesn't work out for them. The climax of the story is when Tom finds out that the girl like Summer who doesn't even believes in the idea of relationships got married to some other guy which really got him thinking and decides to start over a new life and perceive his passion for Architecture."
      }
  }
```

&emsp; \_penjelasan: pada contoh JSON di atas, key adalah yang berada di sebelah kiri ':' dan value-nya adalah yang berada di sebelah kanan ':'\*

Untuk penulisan kode JSON lebih ringkas dan sederhana daripada XML maupun HTML serta tidak memerlukan tag untuk setiap data. Oleh karena itu, file JSON memiliki ukuran file yang lebih kecil dan lebih cepat untuk me-loading data.

- XML merupakan singkatan dari Extensible Markup Language. XML dibuat oleh World Wide Web Consortium (W3C) untuk menstandardisasi proses transfer data yang dilakukan pada server. Sekilas format XML terlihat mirip dengan HTML yang menggunakan tag-tag tertentu untuk menyimpan data, tetapi ada beberapa hal yang hanya berlaku untuk XML, antara lain:
  &emsp;- XML bersifat case sensitive
  &emsp;- XML memiliki fungsi untuk menyimpan dan mengirim data antar server
  &emsp;- XML bersifat dinamis
  &emsp;- XML terdiri dari data struktural
  &emsp;- Tag dalam XML bebas dan dapat dibuat sesuai kebutuhan (dapat di-custom)

  contoh:

```
<?xml version="1.0" encoding="UTF-8"?>
<watchlist>
  <watched>True</watched>
  <title>Barbie in A Mermaid Tale</title>
  <rating>5</rating>
  <release_date>2022-03-02</release_date>
  <review>
   I will say that this movie is busting! I hope I got that right haha! Anywhow, this movie is one of my angels' favorite movies. No hat!! It is totally radical! The plot is so funny, I laugh my led lights off! For real For real! I am so glad my kids have watched this film. They informed me about it during a Starbucks run in my honda civic. My husband doesn't know, unfortunately, because he was with his business. (She and he are very loyal, so I didn't question it when they went upstairs alone! ) Now that I am done with this totes awesome review, I will go ahead and speed walk my daily miles with my friend Betty and Barbra, and make myself a healthy snack alternative! BET!
   </review>
</watchlist>
```

- HTML merupakan singkatan dari Hypertext Markup Language. Berbeda dengan JSON dan XML, HTML tidak dapat menyimpan dan mengirim data. HTML digunakan hanya untuk menampilkan data. Berikut merupakan beberapa hal yang identik dengan HTML:  
  &emsp;- HTML bersifat case insensitive  
  &emsp;- HTML tidak terdiri dari data struktural  
  &emsp;- HTML bersifat statis karena fungsi utamanya untuk menampilkan data  
  &emsp;- Penggunakan tag tertentu sesuai dengan format

  contoh:

  ```
  <html>
   <ul>
      <li>Title</li>
      <li>Watched</li>
      <li>Release Date</li>
      <li>Rating</li>
      <li>Review</li>
    </ul>
  </html>
  ```

## Mengapa perlu data delivery?

Dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuknya. Beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON. Implementasi data delivery dalam bentuk HTML sudah kamu pelajari pada tutorial sebelumnya. Pada tutorial ini akan diajarkan terkait XML dan JSON.

## Cara implementasi

1. Buat app 'mywatchlist'dengan command:

```
django-admin create-app mywatchlist
```

Lalu, tambahkan app 'mywatchlist' pada list INSTALLED_APPS di settings.py.

2. Buat model WatchList pada file models.py.

3. Buka views.py yang ada pada folder wishlist dan buatlah 3 fungsi yang menerima parameter request.  
   a. Fungsi show_mywatchlist untuk menampilkan data dengan format HTML.  
   b. Fungsi show_mywatchlist_xml untuk menampilkan data dengan format XML.  
   c. Fungsi show_mywatchlist_json untuk menampilkan data dengan format JSON.

4. Tambahkan url 'mywatchlist/' untuk app mywatchlist di urls.py pada project_django. Selanjutnya, tambahkan urls yang bersesuaian di file urls.py pada mywatchlist sebagai berikut:  
   a. 'html/'  
   b. 'xml/'  
   c. 'json/'

5. Jalankan proyek Django-mu dengan perintah python manage.py runserver dan bukalah http://localhost:8000/mywatchlist/{html/xml.json}/ (sesuaikan dengan path url yang dibuat) di browser untuk melihat hasilnya.

## Postman

1. HTML
   ![/mywatchlist/html](/public/images/mywatchlist_html.png)
2. XML
   ![/mywatchlist/xml](/public/images/mywatchlist_xml.png)
3. JSON
   ![/mywatchlist/json](/public/images/mywatchlist_json.png)

```

```
