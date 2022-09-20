# Assignment 2

### Website Link: [ruby-pbp.herokuapp.com](https://ruby-pbp.herokuapp.com/)

## Django Client Server Lifecycle

![Client Server Lifecycle](/public/images/client-server.png)  
_reference: [learnbatta.com](https://learnbatta.com/course/django/understanding-request-response-lifecycle-in-django/)_

Penjelasan:

1. Ketika client melakukan request, URL path dari request tersebut akan disesuaikan dengan URL patterns.
2. Lalu, request akan diteruskan ke views yang bersesuaian.
3. Di dalam views, request akan diproses dan dirender berdasarkan templates (.html).
4. User akan menerima response berupa render HTML beserta data yang diambil.

## Why do we use virtual environment?

Virtual environment atau yang disingkat virtualenv merupakan suatu alat yang digunakan untuk membuat suatu lingkungan yang terisolasi dalam project Django. Setiap virtual environment memiliki dependencies dan libraries yang digunakan dalam project tersebut. Dependencies dan libraries yang dimaksud dapat berupa version Python atau Django yang digunakan, requirements external library yang perlu di-download, dll

_reference: [www.petanikode.com](https://www.petanikode.com/python-virtualenv/)_

Bagaimana jika kita tidak menggunakan virtual enviroment dalam sebuah project Django?
Selama ada Python dan Django yang terinstall dalam sistem operasi komputer, suatu project Django masih dapat berjalan tanpa menggunakan virtual environment. Namun, dalam project ini dependencies dan libraries tidak dapat dipisahkan secara eksklusif, sehingga akan bertabrakan dengan project Django lainnya.  
Tidak hanya itu, jika ada beberapa project Django dengan versi Python maupun Django yang berbeda-beda, maka akan terjadi error karena pasti ada perbedaan dalam setiap versinya.

## Mengimplementasi views dan template pada project Django.

1. Buat fungsi show_catalog untuk mengambil semua object katalog.  
   Fungsi ini mengambil semua data dengan model CatalogItem dengan menggunakan method objects.All().  
   Kemudian, menambahkan data tersebut ke context beserta data nama dan student_id.
2. Menambahkan route '' (route ini relatif terhadap 'katalog/') pada urls.py di project katalog. Route ini akan menampilkan data sesuai dengan data yang diambil pada view show_catalog. Lalu, menambahkan route 'katalog/' pada urls.py yang ada di project root.

3. Untuk memetakan data ke dalam template 'katalog.html', gunakan for loop dengan sintaks

   ```python
   {% for ... %}
   <!-- tampilkan data -->
   {{ data yang ingin di tampilkan }}
   {% endfor %}
   ```

4. Untuk deployment, buat project baru di heroku. Lalu, connect ke repository github untuk assignment PBP dan deploy websitenya.
